import datetime
import enum

from bson import Timestamp
from pymongo import MongoClient
from typing import Any, List, Dict
import traceback


class LogLevel(enum.Enum):
    INFO = "Information"
    WARNING = "Warning"
    CRITICAL = "Critical"
    ERROR = "Error"


class MongoDBLogger:
    _instance = None

    def __new__(cls, mongo_uri: str, db_name: str, collection_name: str, replica_set: str = None):
        if cls._instance is None:
            cls._instance = super(MongoDBLogger, cls).__new__(cls)
            cls._mongo_uri = mongo_uri
            cls._db_name = db_name
            cls._collection_name = collection_name
            cls._client = MongoClient(mongo_uri, replicaset=replica_set) if replica_set else MongoClient(mongo_uri)
            cls._db = cls._client[db_name]
            cls._collection = cls._db[collection_name]
        return cls._instance

    def log(self, message: str, args: Dict[str, Any] = {}):
        log_entry = {
            'message': message,
            'additional_info': args,
            'time_created': Timestamp(datetime.datetime.now(), inc=0)
        }
        self._collection.insert_one(log_entry)

    def log_exception(self, e: Exception, level: LogLevel = LogLevel.ERROR, args: Dict[str, Any] = {}):
        exception_info = {
            'level': level.value,
            'type': type(e).__name__,
            'message': str(e),
            'traceback': traceback.format_exc(),
            'additional_info': args,
            'time_created': Timestamp(datetime.datetime.now(), inc=0)
        }
        self._collection.insert_one(exception_info)
