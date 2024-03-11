# -*- coding: utf-8 -*-
from typing import Dict
from pymongo import MongoClient
from pymongo.database import Database

DEFAULT_NAME = 'default'


class MongoClientFactory:
    _name2conf: Dict[str, Dict] = dict()
    _name2db: Dict[str, Database] = dict()

    @classmethod
    def init_mongo_clients(cls, configuration: dict):
        for name, conf in configuration.items():
            client = MongoClient(**conf)
            db = client[conf['authSource']]

            cls._name2conf[name] = conf
            cls._name2db[name] = db

    @classmethod
    def get_db(cls, name: str = None):
        if name is None:
            name = DEFAULT_NAME

        db = cls._name2db.get(name)
        if db is None:
            raise AssertionError(f"Invalid mongo client [{name}]")

        return db
