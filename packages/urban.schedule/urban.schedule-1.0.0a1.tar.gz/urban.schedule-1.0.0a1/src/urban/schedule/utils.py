# -*- coding: utf-8 -*-

from collective.exportimport.import_content import ImportContent
from enum import Enum
from plone import api
from zope.component.hooks import getSite

import json
import os


class ExistingContent(Enum):
    SKIP = 0
    REPLACE = 1
    UPDATE = 2
    IGNORE = 3


def remove_uid(data):
    new_data = []

    for item in data:
        if "UID" in item:
            del item["UID"]
        new_data.append(item)

    return new_data


def remove_none(data):
    return [{k: v for k, v in item.items() if v is not None} for item in data]


def import_json_config(
    json_path,
    context,
):

    if not os.path.isfile(json_path):
        raise ValueError("{} does not exist".format(json_path))

    with open(json_path, "r") as f:
        data = json.load(f)

    portal = api.portal.get()

    if isinstance(context, str):
        context = portal.restrictedTraverse(context)

    request = getattr(context, "REQUEST", None)

    if request is None:
        request = portal.REQUEST

    import_content = ImportContent(context, request)

    import_content.import_to_current_folder = False
    import_content.handle_existing_content = ExistingContent.SKIP
    import_content.limit = None
    import_content.commit = None
    import_content.import_old_revisions = False

    data = remove_uid(data)
    data = remove_none(data)

    import_content.start()
    import_content.do_import(data)
    import_content.finish()


def import_all_config(
    base_json_path="./profiles/config",
    base_context_path="portal_urban",
    config_type="schedule",
):
    directory_path = os.path.dirname(os.path.realpath(__file__))

    licences_types = os.walk(
        os.path.normpath(os.path.join(directory_path, base_json_path))
    )

    root_site = getSite()

    for root, dirs, files in licences_types:
        if files == []:
            continue
        for file in files:
            json_path = os.path.join(root, file)
            licence_type = root.split('/')[-1]
            context_plone = os.path.normpath(
                os.path.join(root_site.id, base_context_path, licence_type, config_type)
            )
            import_json_config(
                json_path=json_path,
                context=context_plone,
                existing_content=ExistingContent.SKIP,
            )
