import json
import random
from typing import List, Tuple

from fastapi import APIRouter, HTTPException, Header
from pydantic import BaseModel

from config import DATA_PATH, SECRET_TOKEN

v1_router = APIRouter(
    prefix="/api/v1/facts",
    tags=["facts"],
    responses={"404": {"description": "Not found"}},
)


class Fact(BaseModel):
    """Represents a dog fact"""

    description: str


class FactResponse(BaseModel):
    """Represents the response from the API"""

    facts: List[str]


def get_data(shuffle: bool) -> Tuple[dict, int]:
    """
    Extract data from the data file.
    :return the loaded data and the number of entries there are
    """
    data_file = open(DATA_PATH, "r")
    data = json.load(data_file)
    if shuffle:
        random.shuffle(data)
    num_of_entry = len(data)
    return data, num_of_entry


@v1_router.get("/all", response_model=FactResponse)
async def get_all_facts() -> any:
    """
    Get all dog facts.
    """
    data, _ = get_data(shuffle=False)
    return FactResponse(facts=[entry.get("fact") for entry in data])


@v1_router.get("/", response_model=FactResponse)
async def get_facts(number: int) -> any:
    """
    Get a number of dog facts randomly.
    """
    data, num_of_entry = get_data(shuffle=True)

    if 0 < number < num_of_entry:
        return FactResponse(facts=[entry.get("fact") for entry in data[:number]])
    else:
        raise HTTPException(
            status_code=400,
            detail=f"Number of facts should be in range of 1 to {num_of_entry}. You requested {number}",
        )


def update_data(new_data: List[dict]) -> any:
    data_file = open(DATA_PATH, "w")
    json.dump(new_data, data_file, indent=4)


def is_duplicate(new_entry: Fact, data: List[dict]) -> bool:
    return any(
        new_entry.description.lower() == each.get("fact").lower() for each in data
    )


@v1_router.post("/new", response_model=Fact)
async def create_fact(entry: Fact, x_token: str = Header(...)) -> any:
    """
    Create a new dog fact entry.
    """
    if x_token != SECRET_TOKEN:
        raise HTTPException(status_code=400, detail="X-Token header invalid")

    data, _ = get_data(shuffle=False)
    if is_duplicate(entry, data):
        raise HTTPException(status_code=400, detail="Fact already existed")

    data.append({"fact": entry.description})
    update_data(data)
    return entry
