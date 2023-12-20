from pokedex_object import PokedexObject


class Stats(PokedexObject):
    """
      A class representing the stats of a Pokémon.

      Attributes:
          name (str): The name of the Pokémon.
          ID (int): The ID number of the Pokémon in the Pokédex.
          is_battle (bool): Whether the Pokémon can be used in battles.
          move_damage_class (str): The damage class of the Pokémon's moves.

      Inherited Attributes:
          description (str): A brief description of the Pokémon.
          types (list): A list of the Pokémon's types.
          abilities (list): A list of the Pokémon's abilities.
          height (float): The height of the Pokémon in meters.
          weight (float): The weight of the Pokémon in kilograms.
      """

    def __init__(self, name=None, ID=None, is_battle=None, move_damage_class=None):
        """
                Initialize a new Stats object with the given parameters.

                Args:
                    name (str, optional): The name of the Pokémon. Defaults to None.
                    ID (int, optional): The ID number of the Pokémon in the Pokédex. Defaults to None.
                    is_battle (bool, optional): Whether the Pokémon can be used in battles. Defaults to None.
                    move_damage_class (str, optional): The damage class of the Pokémon's moves. Defaults to None.
                """
        super().__init__(name, ID)
        self._is_battle = is_battle
        self._move_damage_class = move_damage_class

    @property
    def is_battle(self):
        return self._is_battle

    @is_battle.setter
    def is_battle(self, is_battle):
        self._is_battle = is_battle

    @property
    def move_damage_class(self):
        return self._move_damage_class

    @move_damage_class.setter
    def move_damage_class(self, move_damage_class):
        self._move_damage_class = move_damage_class

    def __str__(self):
        return f"\nName: {self.name}\n" \
               f"ID: {self.ID}\n" \
               f"Is_Battle_Only: {self.is_battle}\n" \
               f"Move Damage Class: {self.move_damage_class}\n"
