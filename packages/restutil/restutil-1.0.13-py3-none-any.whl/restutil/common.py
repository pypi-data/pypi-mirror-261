#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'adions025@gmail.com'

from os import name
from copy import deepcopy
from restutil.operations import ResOperationType as resType
from restutil.decorators import Decorest
from restutil.result import ResData

import os

class Common(object):
    """
        Class with common methods/functions
    """

    deco = Decorest()

    def __init__(self):
        """
            Basic constructor
        """
        pass

    def get_slash(self):
        """
            Reference of S.O. returned values '\\' - Windows or '/' - Linux
        """
        if name == 'nt':
            return '\\'
        else:
            return '/'

    def do_extra_logger(self, app_name: str, method_name: str, class_name: str, inherited_from: str, *args, **kwargs):
        """
            Public method used for construct dictionary with extra information for send to logger.
            :param app_name: string
            :param method_name: string
            :param class_name: string
            :param inherited_from: string
            :param args: extra data
            :param kwargs: extra dictionary
        """
        extra = dict()
        extra["AppName"] = app_name
        extra["Class"] = class_name
        extra["Method"] = method_name
        extra["inheritedFrom"] = inherited_from
        if kwargs:
            extra.update(kwargs['kwargs'])
        return extra

    def remove_property(self, target: dict, prop: []) -> dict:
        """
            Method used for remove properties from a dictionary
            :param target: dict. Dictionary over that we can do changes
            :para prop: []. Properties of dictionary that we will remove inside.
        """
        try:
            for p in prop:
                del target[p]
        except Exception:
            pass
        return target

    def object_to_dictionary(self, model: object) -> dict:
        """
        Method used for convert model into dictionary
        :param model: object. Object over that we can do conversion to
        dictionary. Previously we do a copy and convert this copy.
        """
        result: dict = dict()
        try:
            bck_model = deepcopy(model)
            result = bck_model.__dict__
        except Exception:
            pass
        return result

    @deco.try_log
    def create_dir(self, path: str, name: str, exist: bool = True) -> ResData:
        result: ResData = ResData()
        if name and os.path.exists(path):
            os.makedirs(f'{path}/{name}', exist_ok=exist)
            result.content = os.path.join(path, name)
            result.add_result(message="ok", res_type=resType.SUCCESS)
        else:
            result.content = None
            result.add_result(message="Check name||path ", res_type=resType.WARNING)
        return result
