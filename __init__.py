#!/usr/bin/python3
# -*- coding: utf-8 -*-

import json
import os


class jsonf(object):
    __k_encoding = "utf-8"

    @staticmethod
    def save_s(obj)-> str:
        json_str = json.dumps(obj, sort_keys=False, ensure_ascii=False, indent=4, separators=(",", ": "))
        return json_str

    @staticmethod
    def save(obj, file_path):
        with open(file_path, "w", encoding=jsonf.__k_encoding) as file:
            file.write(jsonf.save_s(obj))

    @staticmethod
    def load_s(json_str)-> str:
        json_obj = json.loads(json_str)
        return json_obj

    @staticmethod
    def load(file_path) -> json:
        json_obj = {}
        if os.path.isfile(file_path):
            with open(file_path, "r", encoding=jsonf.__k_encoding) as file:
                file_contents = file.read()
                if file_contents:
                    json_obj = jsonf.load_s(file_contents)
        return json_obj
