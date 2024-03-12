# SPDX-FileCopyrightText: 2024 Georg-August-Universität Göttingen
#
# SPDX-License-Identifier: LGPL-3.0-or-later

import os

import click
from tgclients.config import DEV_SERVER, PROD_SERVER
from tgclients import (
    TextgridConfig,
    TextgridAuth,
    TextgridSearch,
    TextgridCrud,
    TextgridCrudRequest,
)

from tgclients.databinding import Object as TextgridObject, MetadataContainerType

from xsdata.formats.dataclass.context import XmlContext
from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.formats.dataclass.serializers import XmlSerializer

import xml.etree.ElementTree as ET
import lxml.etree
import lxml.builder

import re
from xml.dom.minidom import parse
from concurrent.futures import ThreadPoolExecutor, as_completed

from jinja2 import Environment, BaseLoader, Template


class TGclient(object):
    def __init__(self, sid, server):
        # TODO: init on demand, otherwise every call will create a soap client etc
        self.sid = sid
        self.config = TextgridConfig(server)
        self.tgauth = TextgridAuth(self.config)
        self.tgsearch = TextgridSearch(self.config, nonpublic=True)
        self.crud_req = TextgridCrudRequest(self.config)
        self.crud = TextgridCrud(self.config)
        context = XmlContext()
        self.parser = XmlParser(context=context)
        self.serializer = XmlSerializer(context=context)


pass_tgclient = click.make_pass_decorator(TGclient)


@click.group()
@click.option(
    "-s",
    "--sid",
    default=lambda: os.environ.get("TEXTGRID_SID", ""),
    required=True,
    help="A textgrid session ID. Defaults to environment variable TEXTGRID_SID",
)
@click.option(
    "--server",
    default=PROD_SERVER,
    help="the server to use, defaults to " + PROD_SERVER,
)
@click.option("--dev", is_flag=True, help="use development system: " + DEV_SERVER)
@click.pass_context
def cli(ctx, sid, server, dev):
    """Helper cli tool to list or create TextGrid projects"""

    authz = "textgrid-esx2.gwdg.de"
    if dev:
        server = DEV_SERVER
        authz = "textgrid-esx1.gwdg.de"

    if sid == "":
        click.secho(
            f"""Please provide a textgrid session ID. Get one from
        {server}/1.0/Shibboleth.sso/Login?target=/1.0/secure/TextGrid-WebAuth.php?authZinstance={authz}
        and add with '--sid' or provide environment parameter TEXTGRID_SID
        """,
            fg="red",
        )
        exit(0)

    ctx.obj = TGclient(sid, server)


@cli.command()
@click.option(
    "--urls", "as_urls", help="list projects as urls for staging server", is_flag=True
)
@pass_tgclient
def list(client, as_urls):
    """List existing projects."""

    projects = client.tgauth.list_assigned_projects(client.sid)

    for project_id in projects:
        desc = client.tgauth.get_project_description(project_id)
        if as_urls:
            click.secho(
                f"https://staging.textgridrep.org/project/{project_id} : {desc.name}"
            )
        else:
            click.secho(f"{project_id} : {desc.name}")


@cli.command()
@click.option("-d", "--description", help="project description")
@click.argument("name")
@pass_tgclient
def create(client, name, description):
    """Create new project with name "name"."""

    project_id = client.tgauth.create_project(client.sid, name, description)
    click.secho(f"created new project with ID: {project_id}")


@cli.command()
@click.argument("project_id")
@pass_tgclient
def contents(client, project_id):
    """list contents of project"""

    contents = client.tgsearch.search(
        filters=["project.id:" + project_id], sid=client.sid, limit=100
    )

    click.echo(f"project {project_id} contains {contents.hits} files:")

    for tgobj in contents.result:
        title = tgobj.object_value.generic.provided.title
        tguri = tgobj.object_value.generic.generated.textgrid_uri.value
        format = tgobj.object_value.generic.provided.format

        click.echo(f" - {tguri}: {title} ({format})")


@cli.command()
@click.option(
    "--clean",
    "do_clean",
    help="call clean automatically if project not empty",
    is_flag=True,
)
@click.option(
    "--limit",
    help="how much uris to retrieve for deletion in one query (if called with --clean) (Default: 100)",
    default=100,
)
@click.confirmation_option(prompt="Are you sure you want to delete the project?")
@click.argument("project_id")
@pass_tgclient
def delete(client, project_id, do_clean, limit):
    """Delete project with project id "project_id"."""

    contents = client.tgsearch.search(
        filters=["project.id:" + project_id], sid=client.sid
    )
    if int(contents.hits) > 0:
        click.echo(
            f"project {project_id} contains {contents.hits} files. Can not delete project (clean or force with --clean)"
        )
        if do_clean:
            clean_op(client, project_id, limit)
        else:
            exit(0)

    res = client.tgauth.delete_project(client.sid, project_id)
    click.secho(f"deleted, status: {res}")


@cli.command()
@click.argument("project_id")
@click.option(
    "--limit",
    help="how much uris to retrieve for deletion in one query (Default: 100)",
    default=100,
)
@click.option(
    "--threaded", help="use multithreading for crud delete requests", is_flag=True
)
@pass_tgclient
def clean(client, project_id, limit, threaded):
    """Delete all content from project with project id "project_id"."""

    clean_op(client, project_id, limit, threaded)


def clean_op(
    client: TGclient, project_id: str, limit: int = 100, threaded: bool = False
):
    """delete all objects belonging to a given project id

    Args:
        client (TGClient): instance of tglcient
        project_id (str): the project ID
        limit (int): how much uris to retrieve for deletion in one query
        threaded (bool): wether to use multiple threads for deletion
    """

    contents = client.tgsearch.search(
        filters=["project.id:" + project_id], sid=client.sid, limit=limit
    )

    click.echo(f"project {project_id} contains {contents.hits} files:")

    for tgobj in contents.result:
        title = tgobj.object_value.generic.provided.title
        tguri = tgobj.object_value.generic.generated.textgrid_uri.value

        click.echo(f" - {tguri}: {title}")

    if int(contents.hits) > limit:
        click.echo(f" ...and ({int(contents.hits) - limit}) more objects")

    if not click.confirm("Do you want to delete all this objects"):
        exit(0)
    else:

        with click.progressbar(
            length=int(contents.hits),
            label="deleting object",
            show_eta=True,
            show_pos=True,
            item_show_func=lambda a: a,
        ) as bar:

            # iterate with paging
            nextpage = True
            while nextpage:

                if not threaded:
                    for tgobj in contents.result:
                        result = _crud_delete_op(client, tgobj)
                        bar.update(1, result)
                else:
                    with ThreadPoolExecutor(max_workers=limit) as ex:
                        futures = [
                            ex.submit(_crud_delete_op, client, tgobj)
                            for tgobj in contents.result
                        ]

                        for future in as_completed(futures):
                            result = future.result()
                            bar.update(1, result)

                if int(contents.hits) < limit:
                    # stop if there are no more results left
                    nextpage = False
                else:
                    # get next page of results from tgsearch
                    contents = client.tgsearch.search(
                        filters=["project.id:" + project_id],
                        sid=client.sid,
                        limit=limit,
                    )


def _crud_delete_op(client, tgobj):
    tguri = tgobj.object_value.generic.generated.textgrid_uri.value
    title = tgobj.object_value.generic.provided.title
    res = client.crud.delete_resource(client.sid, tguri)
    if res.status_code == 204:
        return f"deleted {tguri}: {title}"
    else:
        return f"error deleting {tguri}: {title}"


@cli.command()
@click.argument("project_id")
@click.argument("the_data", type=click.File("rb"))
@click.argument("metadata", type=click.File("rb"))
@pass_tgclient
def put(client, project_id, the_data, metadata):
    """put a file with metadata online"""

    res = client.crud_req.create_resource(
        client.sid, project_id, the_data, metadata.read()
    )
    click.echo(res)


@cli.command()
@click.argument("textgrid_uri")
@click.argument("the_data", type=click.File("rb"))
@pass_tgclient
def update_data(client, textgrid_uri, the_data):
    """update a file"""

    metadata = client.crud.read_metadata(textgrid_uri, client.sid)
    client.crud.update_resource(client.sid, textgrid_uri, the_data, metadata)


@cli.command()
@click.argument("imex", type=click.File("rb"))
@click.argument("folder_path")
@click.option(
    "--newrev", "make_revision", help="to update data as new revisions", is_flag=True
)
@pass_tgclient
def update_imex(client, imex, folder_path: str, make_revision: bool = True):
    """update from imex, argument 1 is the IMEX file, argument 2 the path where the data
    is located, as the imex has only relative paths.
    """

    namespaces = {"ore": "http://www.openarchives.org/ore/terms/"}

    imex_map = imex_to_dict(imex, path_as_key=True)

    with click.progressbar(imex_map.items()) as bar:
        for path, textgrid_uri in bar:
            with open(folder_path + "/" + path, "rb") as the_data:
                metadata = client.crud.read_metadata(textgrid_uri, client.sid)
                # rev uri, because we may have base uris, but metadata will have latest rev
                revision_uri = (
                    metadata.object_value.generic.generated.textgrid_uri.value
                )

                # aggregations contains local path on disk, but we need the textgrid-baseuri instead
                if "tg.aggregation" in metadata.object_value.generic.provided.format:
                    rdf_resource = (
                        "{http://www.w3.org/1999/02/22-rdf-syntax-ns#}resource"
                    )
                    the_dataXML = ET.parse(the_data)
                    the_dataXML_root = the_dataXML.getroot()
                    title = metadata.object_value.generic.provided.title[0]
                    click.echo(f'\nrewriting {revision_uri} ("{title}"):')
                    for ore_aggregates in the_dataXML_root.findall(
                        ".//ore:aggregates", namespaces
                    ):
                        resource_path = ore_aggregates.attrib[rdf_resource]
                        resource_uri = base_uri_from(imex_map[resource_path])
                        ore_aggregates.set(rdf_resource, resource_uri)
                        click.echo(f"  {resource_path}  -> {resource_uri}")
                    the_data = ET.tostring(
                        the_dataXML_root, encoding="utf8", method="xml"
                    )

                client.crud.update_resource(
                    client.sid,
                    revision_uri,
                    the_data,
                    metadata,
                    create_revision=make_revision,
                )


# TODOs
# - use path functions from python
@cli.command()
@click.argument("project_id")
@click.argument("aggregation_file", type=click.File("rb"))
@pass_tgclient
def put_aggregation(client, project_id, aggregation_file):
    """upload an aggregation and referenced objects recursively"""

    imex_map = {}

    namespaces = {"ore": "http://www.openarchives.org/ore/terms/"}
    rdf_resource = "{http://www.w3.org/1999/02/22-rdf-syntax-ns#}resource"

    with open(aggregation_file.name + ".meta", "rb") as agg_meta_file:
        agg_meta: TextgridObject = client.parser.parse(agg_meta_file, TextgridObject)

    if "tg.aggregation" not in agg_meta.generic.provided.format:
        click.echo("not an aggregation")
        return

    # if aggregation is edition then upload related work object
    if agg_meta.generic.provided.format == "text/tg.edition+tg.aggregation+xml":
        work_path = agg_meta.edition.is_edition_of
        tguri = upload_file(client, project_id, work_path)
        imex_map[tguri] = work_path
        agg_meta.edition.is_edition_of = tguri  # update isEditionOf

    agg_xml = ET.parse(aggregation_file)
    agg_xml_root = agg_xml.getroot()
    for ore_aggregates in agg_xml_root.findall(".//ore:aggregates", namespaces):
        data_path = ore_aggregates.attrib[rdf_resource]
        tguri = upload_file(client, project_id, data_path)
        imex_map[tguri] = data_path
        ore_aggregates.set(
            rdf_resource, base_uri_from(tguri)
        )  # update the xml with the uri

    tguri = upload_modified(client, project_id, agg_xml_root, agg_meta)
    imex_map[tguri] = aggregation_file.name

    imex_filename = aggregation_file.name + ".imex"
    write_imex(imex_map, imex_filename)
    click.echo(f"done, find the imex file at {imex_filename}")


def upload_file(client: TGclient, project_id: str, data_path: str):
    """upload an object and its related .meta file to specified project"""

    click.echo(f"uploading unmodified file with meta: {data_path}")

    with open(data_path, "r") as the_data, open(data_path + ".meta", "rb") as metadata:
        mdobj = client.parser.parse(metadata, TextgridObject)
        mdcont = MetadataContainerType()
        mdcont.object_value = mdobj

        res = client.crud.create_resource(
            client.sid, project_id, the_data.read(), mdcont
        )
        return res.object_value.generic.generated.textgrid_uri.value


def upload_modified(client: TGclient, project_id: str, etree_data, metadata):
    """upload in memory xml and it textgrid-metadata (possibly modified) as textgridobject"""

    click.echo(
        f"uploading modified file with meta: {metadata.generic.provided.title[0]}"
    )
    data_str = ET.tostring(etree_data, encoding="utf8", method="xml")

    mdcont = MetadataContainerType()
    mdcont.object_value = metadata

    res = client.crud.create_resource(client.sid, project_id, data_str, mdcont)
    return res.object_value.generic.generated.textgrid_uri.value


def write_imex(imex_map: dict, filename: str):
    """write an .imex file which keeps track of local filenames and their related textgrid uris.
    this is useful for reimporting the data with the same uris (or new revisions of them).
    """

    imex_template = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<importSpec xmlns="http://textgrid.info/import">
  {% for tguri, path in imex.items() -%}
  <importObject textgrid-uri="{{tguri}}" local-data="{{path}}"/>
  {% endfor %}
</importSpec>
"""
    xml = Template(imex_template).render(imex=imex_map)
    with open(filename, "w") as file:
        file.write(xml)


def imex_to_dict(imex, path_as_key: bool = False):
    """parse textgrid_uris and paths from imex file. return a dict with uri as key per default,
    or use path as key if path_as_key is true"""

    imex_map = {}
    imexXML = parse(imex)
    for importObject in imexXML.getElementsByTagName("importObject"):
        textgrid_uri = importObject.getAttribute("textgrid-uri")
        path = importObject.getAttribute("local-data")
        if path_as_key:
            imex_map[path] = textgrid_uri
        else:
            imex_map[textgrid_uri] = path

    return imex_map


def base_uri_from(textgrid_uri):
    return textgrid_uri.split(".")[0]
