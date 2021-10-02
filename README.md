# Dog Facts API

An API that will return random facts about dog.

## Inspirations

- The project is a port of [kinduff/dog-api](https://github.com/kinduff/dog-api) using Python with Flask.
- There are way too many APIs supporting cat facts. It is unfair!
- I'm a dog person. Cats are jerks.

## Usage:

- `https://dog-facts-api.herokuapp.com/api/v1/facts/all` to get all the facts at once.
- Change `all` to parameter `{number}` to specify the number of facts you want to receive.

## Rebuild the project:

- Clone the repo.
- `poetry install` to install the dependencies.
- `poetry shell` to activate the virtual environment.
- `poetry run python dog_facts_api/main.py` to start the uvicorn server.

## Example:

- `https://dog-facts-api.herokuapp.com/api/v1/facts/5` returns:

```JSON
{
  "facts": [
    "It is much easier for dogs to learn spoken commands if they are given in conjunction with hand signals or gestures.",
    "The breed of dog with the best sense of smell is the bloodhound.",
    "The oldest dog on record was an Australian cattle dog named Bluey who lived 29 years and 5 months. In human years, that is more than 160 years old.",
    "The Girl Scouts and Boy Scouts both offer merit badges in dog care.",
    "Dogs can learn more than 1000 words."
  ]
}
```
