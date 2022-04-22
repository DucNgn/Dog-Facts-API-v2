# Dog Facts API

An API that returns random facts about dog.

## Inspirations

- The project is a port of [kinduff/dog-api](https://github.com/kinduff/dog-api) using Python with FastAPI.
- There are way too many APIs supporting cat facts. It is unfair!
- I'm a dog person. Cats are jerks.

## Usage:

- `https://www.dogfactsapi.ducnguyen.dev/docs`: for interactive Swagger UI.
- `https://www.dogfactsapi.ducnguyen.dev/api/v1/facts/all` to get all the facts at once.
- Change `all` to parameter `?number={your_number}` to specify the number of facts you want to receive.

## Rebuild the project locally:

- Clone the repo.
- `poetry install` to install the dependencies.
- `poetry shell` to activate the virtual environment.
- `poetry run python dog_facts_api/main.py` to start the uvicorn server.

## Example:

- `https://www.dogfactsapi.ducnguyen.dev/api/v1/facts/?number=5` returns:

```JSON
{
  "facts": [
    "Chase that tail! Dogs chase their tails for a variety of reasons: curiosity, exercise, anxiety, predatory instinct or, they might have fleas! If your dog is chasing his tail excessively, talk with your vet.",
    "'Frito Feet' is the name of the phenomenon in which the bacteria on a dog's paws cause them to smell like corn chips. Because a pup's feet are in constant contact with the ground, they pick up tons of microorganisms in their paws. When dogs cool off by sweating through the pads of their feet, the combo of moisture and bacteria releaces a nutty, popcorn-like aroma. Basically it's dog B.O.",
    "An African wolf dog known as the Basenji is the only dog in the world that cannot bark.",
    "A dog’s powerful sense of smell is frequently called upon to detect anything from mines and explosives to termites and bed bugs.",
    "Every dog on earth likely descended from a species knows as the Tomarctus – a creature that roamed the earth over 15 million years ago."
  ]
}
```
