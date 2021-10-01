import json
import random
from typing import List, Tuple

from fastapi import APIRouter, HTTPException, Header
from pydantic import BaseModel

from config import DATA_PATH, SECRET_TOKEN

v1_router = APIRouter(
    prefix="/v1/facts", tags=["facts"], responses={"404": {"description": "Not found"}}
)


class Fact(BaseModel):
    """Represents a dog fact"""

    description: str


def get_data() -> Tuple[dict, int]:
    """
    Extract data from the data file.
    :return the loaded data and the number of entries there are
    """
    data_file = open(DATA_PATH, "r")
    data = json.load(data_file)
    random.shuffle(data)
    num_of_entry = len(data)
    return data, num_of_entry


@v1_router.get("/{number}")
async def get_facts(number: int) -> dict:
    """
    Get dog facts randomly.
    """
    data, num_of_entry = get_data()

    if 0 < number < num_of_entry:
        return {"facts": [entry.get("fact") for entry in data[:number]]}
    else:
        raise HTTPException(
            status_code=400,
            detail=f"Number of facts should be in range of 1 to {num_of_entry}. You requested {number}",
        )


def update_data(new_data: List[dict]) -> None:
    data_file = open(DATA_PATH, "w")
    json.dump(new_data, data_file, indent=4)


def is_duplicate(new_entry: Fact, data: List[dict]) -> bool:
    return any(
        new_entry.description.lower() == each.get("fact").lower() for each in data
    )


@v1_router.post("/new")
async def create_fact(entry: Fact, x_token: str = Header(...)) -> Fact:
    """
    Create a new dog fact entry.
    """
    if x_token != SECRET_TOKEN:
        raise HTTPException(status_code=400, detail="X-Token header invalid")

    data, _ = get_data()
    if is_duplicate(entry, data):
        raise HTTPException(status_code=400, detail="Fact already existed")

    data.append({"fact": entry.description})
    update_data(data)
    return entry
