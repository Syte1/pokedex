# Professor Oak's Pokedex (Assignment 3)

In this assignment, you will gain first-hand experience writing asynchronous code that creates HTTP client sessions and queries an endpoint with GET HTTP Requests. We will be implementing asyncio tasks and using the aiohttp package to create our very own prototype of Professor Oak's Pokedex.

For those of you who are not into Pokémon, a Pokedex is a device that contains all known information about the Pokémon universe. It is a crucial tool in every Pokémon trainer's toolbox.

We will be querying the PokéAPI, which is a RESTful API. REST stands for REpresentational State Transfer. This is a web application that provides the client (your application) with a Representation of the State of a requested resource. In simpler words, it provides an instantiated object (attributes only).

## Requirements

To complete this assignment, you will need:

- Python 3.7 or higher
- The `aiohttp` package
- The `asyncio` package
- Access to the PokéAPI (https://pokeapi.co)

## Getting Started

1. Clone this repository to your local machine.
2. Install the `aiohttp` package using pip: `pip install aiohttp`
3. Install the `asyncio` package using pip: `pip install asyncio`
3. Update the `config.py` file with your PokéAPI credentials (if necessary).
4. Run the `main.py` file using Python: `python main.py`

## Assignment

Your task is to implement an asynchronous program that queries the PokéAPI for information about Pokémon. The program should take a list of Pokémon names as input and output information about each Pokémon's abilities, moves, stats, and types.

You will need to use the `aiohttp` package to create HTTP client sessions and query the PokéAPI. You will also need to use the `asyncio` package to create asynchronous tasks and manage concurrency.

Your program should be modular and well-organized. You should use classes and functions to encapsulate your code and make it reusable. You should also use good software engineering practices such as error handling, testing, and documentation.

Good luck, and have fun!
