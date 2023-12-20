import abc
import asyncio
import aiohttp
import json
from abc import ABC

import requests

from ability import Ability
from move import Move
from pokemon import Pokemon
from stats import Stats
from request import Request
import requests as pokeapi


class Handler(ABC):
    """
    An abstract base class for creating handlers that process requests in a chain.

    :param next_handler: The next handler in the chain.
    :type next_handler: Handler or None
    """

    def __init__(self, next_handler=None):
        """
         Constructor for the Handler class.

         :param next_handler: The next handler in the chain.
         :type next_handler: Handler or None
         """
        self._next_handler = next_handler

    def set_next_handler(self, next_handler):
        """
        Sets the next handler in the chain.

        :param next_handler: The next handler in the chain.
        :type next_handler: Handler
        """
        self._next_handler = next_handler

    @abc.abstractmethod
    def handle(self, request):
        """
        Sets the next handler in the chain.

        :param next_handler: The next handler in the chain.
        :type next_handler: Handler
        """
        pass


class GetRequestsHandler(Handler):
    """
    A handler class for getting data from the PokeAPI.
    """
    API_URL = "https://pokeapi.co/api/v2/"

    async def handle(self, request):
        """
        Handle the request by fetching data from the PokeAPI for each input value.

        :param request: The request object containing input data.
        """
        tasks = [self.get_request(request.poke_dex_mode.value, single_input) for single_input in request.data_input]
        results = await asyncio.gather(*tasks, return_exceptions=True)
        request.pokemon_info.extend([result for result in results])
        await self._next_handler.handle(request)

    @classmethod
    async def get_request(cls, mode, single_input):
        """
        Make an asynchronous request to the PokeAPI for a single input value.

        :param mode: The API mode to use for the request.
        :param single_input: The input value to request data for.
        :return: The JSON response for the request, or None if an error occurred.
        """
        end_point = f"{mode}/{single_input}"
        async with aiohttp.ClientSession() as session:
            try:
                async with session.get(f"{cls.API_URL}{end_point}") as response:
                    response.raise_for_status()
                    content = await response.read()
                    return json.loads(content.decode('utf-8'))
            except aiohttp.ClientResponseError as e:
                return None


class CreateEntityHandler(Handler):
    """
    A handler class for creating entities based on the request mode.
    """
    MAP = {
        "pokemon": Pokemon,
        "move": Move,
        "ability": Ability,
        "stat": Stats
    }

    async def handle(self, request):
        """
        Handle the request by creating entities based on the mode.

        :param request: The request object containing input data and mode.
        """
        # print(request.pokemon_info)
        tasks = [asyncio.create_task(self.create_entity(None if info is None else request.poke_dex_mode.value)) for info
                 in request.pokemon_info]
        request.result = await asyncio.gather(*tasks)
        await self._next_handler.handle(request)

    async def create_entity(self, mode):
        """
        Create an entity based on the given mode.

        :param mode: The mode to create an entity for.
        :return: A new entity object or None if the mode is not valid.
        """
        if mode is None:
            return None
        return self.MAP[mode]()


class PopulatePokemonHandler(Handler):
    """
    A handler class for populating Pokemon entities with data from the PokeAPI.
    """

    async def handle(self, request: Request):
        """
        Handle the request by populating the Pokemon entities with data.

        :param request: The request object containing input data and the list of Pokemon entities.
        """
        for index, entity in enumerate(request.result):
            if entity is None:
                request.result[index] = f"\n\n{request.data_input[index]} is not valid. Skipping this request.\n"
            else:
                entity.name = request.pokemon_info[index]["name"]
                entity.ID = request.pokemon_info[index]["id"]
                entity.height = request.pokemon_info[index]["height"]
                entity.weight = request.pokemon_info[index]["weight"]
                entity.stats = "".join(
                    [f'{(stat["stat"]["name"], stat["base_stat"])}\n' for stat in request.pokemon_info[index]["stats"]])
                entity.types = ", ".join(
                    [specific_type["type"]["name"] for specific_type in request.pokemon_info[index]["types"]])
                entity.abilities = "\n\n".join(
                    [ability["ability"]["name"] for ability in request.pokemon_info[index]["abilities"]])
                entity.moves = "".join([
                    f'(\'Move name: {move["move"]["name"]}\','
                    f' \'Level acquired: {move["version_group_details"][0]["level_learned_at"]}'
                    f'\')\n\n'
                    for move in request.pokemon_info[index]["moves"]])
        await self._next_handler.handle(request)


class PopulateAbilityHandler(Handler):
    """
    A handler class for populating Ability entities with data from the PokeAPI.
    """

    async def handle(self, request):
        """
        Handle the request by populating the Ability entities with data.

        :param request: The request object containing input data and the list of Ability entities.
        """
        for index, entity in enumerate(request.result):
            if entity is None:
                request.result[index] = f"\n{request.data_input[index]} is not valid. Skipping this request.\n"
            else:
                entity.name = request.pokemon_info[index]["name"]
                entity.ID = request.pokemon_info[index]["id"]
                entity.generation = request.pokemon_info[index]["generation"]['name']
                entity.effect = "".join(
                    [effect_entry["effect"] for effect_entry in request.pokemon_info[index]["effect_entries"] if
                     effect_entry["language"]["name"] == "en"])
                entity.pokemon = ", ".join(
                    [f"{pokemon['pokemon']['name']}" for pokemon in request.pokemon_info[index]["pokemon"]])

        await self._next_handler.handle(request)


class PopulateMovesHandler(Handler):
    """
    A handler class for populating Move entities with data from the PokeAPI.
    """

    async def handle(self, request):
        """
        Handle the request by populating the Move entities with data.

        :param request: The request object containing input data and the list of Move entities.
        """
        for index, entity in enumerate(request.result):
            if entity is None:
                request.result[index] = f"\n{request.data_input[index]} is not valid. Skipping this request.\n"
            else:
                entity.name = request.pokemon_info[index]["name"]
                entity.ID = request.pokemon_info[index]["id"]
                entity.generation = request.pokemon_info[index]["generation"]["name"]
                entity.accuracy = request.pokemon_info[index]["accuracy"]
                entity.pp = request.pokemon_info[index]["pp"]
                entity.power = request.pokemon_info[index]["power"]
                entity.type = request.pokemon_info[index]["type"]["name"]
                entity.damage_class = request.pokemon_info[index]["damage_class"]["name"]
                entity.effect = "".join([effect_entry["short_effect"]
                                         for effect_entry in request.pokemon_info[index]["effect_entries"]
                                         if len(effect_entry) > 0 and effect_entry["language"]["name"] == "en"])

        await self._next_handler.handle(request)


class PopulateExpandedPokemonHandler(Handler):
    """
       A handler to populate Pokemon entities with additional information from API requests.

       Attributes:
       -----------
       _next_handler: Handler
           The next handler in the chain of responsibility pattern.

       Methods:
       --------
       async def handle(self, request: Request):
           Populates the Pokemon entities in the request with additional information from API requests.
           Parameters:
               request (Request): The request object to handle.
           Raises:
               None.
           Returns:
               None.
       """

    async def handle(self, request: Request):
        """
        Updates the `request.result` list with information obtained from external API requests.

        For each entity in `request.result`, this function makes several API requests to obtain information about the
        corresponding Pokémon's abilities, moves, stats, and types. It then updates the `entity` object with this information.

        Args:
            request (Request): An instance of the Request class containing information about the API requests to be made.

        Returns:
            None

        Raises:
            None
        """
        for index, entity in enumerate(request.result):
            if entity is None:
                request.result[index] = f"\n{request.data_input[index]} is not valid. Skipping this request.\n"
                continue

            entity.name = request.pokemon_info[index]["name"]
            entity.ID = request.pokemon_info[index]["id"]
            entity.height = request.pokemon_info[index]["height"]
            entity.weight = request.pokemon_info[index]["weight"]
            # entity.stats = "".join(
            #     [f'{(stat["stat"]["name"], stat["base_stat"])}\n' for stat in request.pokemon_info[index]["stats"]])
            entity.stats = ""
            stats_list = request.pokemon_info[index]["stats"]
            for stat in stats_list:
                inner_response = GetRequestsHandler.get_request("stat", stat["stat"]['name'])
                inner_response = await asyncio.gather(inner_response, return_exceptions=True)
                inner_response = inner_response[0]
                new_stat = Stats()
                new_stat.name = inner_response["name"]
                new_stat.ID = inner_response["id"]
                new_stat.is_battle = inner_response["is_battle_only"]
                new_stat.move_damage_class = inner_response["move_damage_class"]
                entity.stats += f"{new_stat}"

            entity.types = ", ".join(
                [specific_type["type"]["name"] for specific_type in request.pokemon_info[index]["types"]])

            ability_list = request.pokemon_info[index]['abilities']
            entity.abilities = ''
            for ability in ability_list:
                inner_response = GetRequestsHandler.get_request("ability", ability["ability"]['name'])
                inner_response = await asyncio.gather(inner_response, return_exceptions=True)
                inner_response = inner_response[0]
                new_ability = Ability()
                new_ability.name = inner_response["name"]
                new_ability.ID = inner_response["id"]
                new_ability.generation = inner_response["generation"]['name']
                new_ability.pokemon = ", ".join(
                    [f"{pokemon['pokemon']['name']}" for pokemon in inner_response["pokemon"]])
                new_ability.effect = "".join(
                    [effect_entry["effect"] for effect_entry in inner_response["effect_entries"] if
                     effect_entry["language"]["name"] == "en"])
                entity.abilities += f"{new_ability}"

            moves_list = request.pokemon_info[index]['moves']
            entity.moves = ''
            for move in moves_list:
                inner_response = GetRequestsHandler.get_request('move', move["move"]["name"])
                inner_response = await asyncio.gather(inner_response, return_exceptions=True)
                inner_response = inner_response[0]
                new_move = Move()
                new_move.name = inner_response["name"]
                new_move.ID = inner_response["id"]
                new_move.generation = inner_response['generation']['name']
                new_move.accuracy = inner_response['accuracy']
                new_move.pp = inner_response['pp']
                new_move.power = inner_response['power']
                new_move.type = inner_response["type"]["name"]
                new_move.damage_class = inner_response['damage_class']["name"]
                new_move.effect = ''.join([effect_entry["short_effect"]
                                           for effect_entry in inner_response["effect_entries"]
                                           if len(effect_entry) > 0 and effect_entry["language"]["name"] == "en"])
                entity.moves += f"{new_move}"
        await self._next_handler.handle(request)


class OutputHandler(Handler):
    """
    A handler class for outputting the results of the requests, either to a file or to the console.
    """
    async def handle(self, request):
        """
        Handle the request by outputting the results to a file or the console, based on the output_type of the request.
        If there is a next handler in the chain, call its handle method after outputting the results.

        :param request: The request object containing the results and output_type.
        """
        if type(request.output_type) is str:
            with open(request.output_type, 'w+') as file:
                for entity in request.result:
                    file.write(str(entity))
        else:
            for entity in request.result:
                print(entity)
            if self._next_handler:
                await self._next_handler.handle(request)
