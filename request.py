import datetime
import os
from typing import List

import requests
from dotenv import load_dotenv

load_dotenv()

API_URL = os.environ.get("API_URL")
API_KEY = os.environ.get("API_KEY")
DATA_SOURCE = "Shared"
DB_NAME = "dev"
COLLECTION_NAME = "inclusion"


def save_inclusion_result(
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
    headers = {
        "API-KEY": API_KEY,
    }

    body = {
        "dataSource": DATA_SOURCE,
        "database": DB_NAME,
        "collection": COLLECTION_NAME,
        "document": {
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
        },
    }

    response = requests.post(f"{API_URL}/action/insertOne", headers=headers, json=body)

    return response.json()["insertedId"]
