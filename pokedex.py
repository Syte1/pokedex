import json

import requests as pokeapi

from ability import Ability
from enum import Enum
from move import Move
from pokemon import Pokemon
from handlers import CreateEntityHandler, PopulatePokemonHandler, PopulateExpandedPokemonHandler, OutputHandler, \
    PopulateAbilityHandler, GetRequestsHandler, PopulateMovesHandler
from request import Request


class PokedexMode(Enum):
    POKEMON = "pokemon"
    ABILITY = "ability"
    MOVE = "move"


class PokeDex:
    """
    A class representing a Pokédex application.

    Attributes:
    -----------
    ex_pokemon_start_handler : GetRequestsHandler
        The start of the chain of handlers for handling requests for expanded Pokémon information.
    pokemon_start_handler : GetRequestsHandler
        The start of the chain of handlers for handling requests for Pokémon information.
    ability_start_handler : GetRequestsHandler
        The start of the chain of handlers for handling requests for ability information.
    move_start_handler : GetRequestsHandler
        The start of the chain of handlers for handling requests for move information.

    Methods:
    --------
    __init__(self):
        Initializes a new PokeDex object with the necessary handlers for handling requests.
    execute_request(self, request: Request):
        Executes the given request and handles it appropriately based on the specified PokeDex mode.
    """
    def __init__(self):
        """
        Initializes a new PokeDex object with the necessary handlers for handling requests.
        """
        self._start_event_handler = None

        # expanded pokemon chain
        ex_pokemon_handle_get_requests = GetRequestsHandler()
        ex_pokemon_handle_create = CreateEntityHandler()
        ex_pokemon_handle_populate = PopulateExpandedPokemonHandler()
        ex_pokemon_handle_output = OutputHandler()

        # set handlers
        ex_pokemon_handle_get_requests.set_next_handler(ex_pokemon_handle_create)
        ex_pokemon_handle_create.set_next_handler(ex_pokemon_handle_populate)
        ex_pokemon_handle_populate.set_next_handler(ex_pokemon_handle_output)

        # pokemon chain
        pokemon_handle_get_requests = GetRequestsHandler()
        pokemon_handle_create = CreateEntityHandler()
        pokemon_handle_populate = PopulatePokemonHandler()
        pokemon_handle_output = OutputHandler()

        # set handlers
        pokemon_handle_get_requests.set_next_handler(pokemon_handle_create)
        pokemon_handle_create.set_next_handler(pokemon_handle_populate)
        pokemon_handle_populate.set_next_handler(pokemon_handle_output)

        # ability chain
        ability_handle_get_requests = GetRequestsHandler()
        ability_handle_create = CreateEntityHandler()
        ability_handle_populate = PopulateAbilityHandler()
        ability_handle_output = OutputHandler()

        # set handlers
        ability_handle_get_requests.set_next_handler(ability_handle_create)
        ability_handle_create.set_next_handler(ability_handle_populate)
        ability_handle_populate.set_next_handler(ability_handle_output)

        # move chain
        move_handle_get_requests = GetRequestsHandler()
        move_handle_get_create = CreateEntityHandler()
        move_handle_populate = PopulateMovesHandler()
        move_handle_output = OutputHandler()

        # set handlers
        move_handle_get_requests.set_next_handler(move_handle_get_create)
        move_handle_get_create.set_next_handler(move_handle_populate)
        move_handle_populate.set_next_handler(move_handle_output)

        # set start handlers
        self.ex_pokemon_start_handler = ex_pokemon_handle_get_requests
        self.pokemon_start_handler = pokemon_handle_get_requests
        self.ability_start_handler = ability_handle_get_requests
        self.move_start_handler = move_handle_get_requests

    async def execute_request(self, request: Request):
        """
        Executes a request by delegating to the appropriate handler based on the mode specified in the request.

        Parameters:
        -----------
        request : Request
            The request to be executed.

        Raises:
        -------
        None

        Returns:
        --------
        None
        """
        if request.expanded:
            await self.ex_pokemon_start_handler.handle(request)

        elif request.poke_dex_mode == PokedexMode.POKEMON:
            await self.pokemon_start_handler.handle(request)

        elif request.poke_dex_mode == PokedexMode.ABILITY:
            await self.ability_start_handler.handle(request)

        elif request.poke_dex_mode == PokedexMode.MOVE:
            await self.move_start_handler.handle(request)
