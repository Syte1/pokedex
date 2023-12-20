class Request:
    """
       A class representing a request to the Poke-Dex API.

       Attributes:
           poke_dex_mode (str): The Poke-Dex mode of the request. Can be "normal", "shiny", or "gender".
           data_input (str): The input data for the request. Can be a Pokemon name or ID, or a comma-separated list of names or IDs.
           expanded (bool): Whether to include extra information in the response. Defaults to False.
           input_type (str): The type of input data provided. Can be "pokemon", "ability", "move", "item", or "location".
           output_type (str): The type of output data requested. Can be "pokemon", "ability", "move", "item", or "location".
           pokemon_info (list): A list of Pokemon objects containing information about the requested Pokemon.
           entity (str): The entity targeted by the request. Can be "pokemon", "ability", "move", "item", or "location".
           result (list): A list of objects containing information about the requested entity.
       """

    def __init__(self):
        self.poke_dex_mode = None
        self.data_input = None
        self.expanded = None
        self.input_type = None
        self.output_type = None
        self.pokemon_info = []
        self.entity = None
        self.result = []

    def __str__(self):
        return f"Poke-Dex-Mode: {self.poke_dex_mode}\nData-Input: {self.data_input}\nExpanded: {self.expanded}" \
               f"\nInput-Type: {self.input_type}\nOutput-Type: {self.output_type}\nPokemon-Info: {self.pokemon_info}" \
               f"\nEntity: {self.entity}"
