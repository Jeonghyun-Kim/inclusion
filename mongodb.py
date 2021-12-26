import datetime
import os
from typing import List

from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()

MONGO_URI = os.environ.get("MONGO_URI")
DB_NAME = "kay"
COLLECTION_NAME = "inclusion"


class MongoDB:
    def __init__(self):
        self.client = MongoClient(MONGO_URI)
        self.db = self.client[DB_NAME]


def save_mongo(
    mongo: MongoDB,
    site: List[int],
    exit_index: int,
    index: int,
    timer: float,
    start_time: float,
    end_time: float,
    DDD: int,
    RHO: int,
    memo: str = "",
) -> str:
    data = {
        "site": site,
        "exit_index": exit_index,
        "index": index,
        "timer": timer,
        "DDD": DDD,
        "RHO": RHO,
        "memo": memo,
        "started_at": datetime.datetime.fromtimestamp(start_time).isoformat(),
        "ended_at": datetime.datetime.fromtimestamp(end_time).isoformat(),
        "elapsed": end_time - start_time,
        "created_at": datetime.datetime.now().isoformat(),
    }
    return mongo.db[COLLECTION_NAME].insert_one(data).inserted_id
