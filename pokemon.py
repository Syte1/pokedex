from pokedex_object import PokedexObject


class Pokemon(PokedexObject):
    """
    A class representing a Pokémon in the Pokémon universe.

    Attributes:
    -----------
    name : str
        The name of the Pokémon.
    id : int
        The ID number of the Pokémon.
    height : float
        The height of the Pokémon.
    weight : float
        The weight of the Pokémon.
    stats : dict
        A dictionary of the Pokémon's base stats, keyed by stat name (e.g. "hp").
    types : list of str
        A list of the types of the Pokémon.
    abilities : list of Ability
        A list of the Pokémon's abilities.
    moves : list of Move
        A list of the moves the Pokémon can learn.

    Methods:
    --------
    __init__(self, name=None, id=None, height=None, weight=None, stats=None,
             types=None, abilities=None, moves=None):
        Initializes a new Pokemon object with the given attributes.
    __str__(self):
        Returns a string representation of the Pokemon object, including its name, ID, height, weight, types,
        stats, abilities, and moves.
    """

    def __init__(self, name=None, id=None, height=None, weight=None, stats=None,
                 types=None, abilities=None, moves=None):
        """
        Initializes a new Pokemon object with the given attributes.

        Parameters:
        -----------
        name : str
            The name of the Pokémon.
        id : int
            The ID number of the Pokémon.
        height : float
            The height of the Pokémon.
        weight : float
            The weight of the Pokémon.
        stats : dict
            A dictionary of the Pokémon's base stats, keyed by stat name (e.g. "hp").
        types : list of str
            A list of the types of the Pokémon.
        abilities : list of Ability
            A list of the Pokémon's abilities.
        moves : list of Move
            A list of the moves the Pokémon can learn.
        """
        super().__init__(name, id)
        self._height = height
        self._weight = weight
        self._stats = stats
        self._types = types
        self._abilities = abilities
        self._moves = moves

    @property
    def height(self):
        """
        float: The height of the Pokémon.
        """
        return self._height

    @height.setter
    def height(self, height):
        """
        Set the height of the Pokémon.

        Parameters:
        -----------
        height : float
            The new height value to set.
        """
        self._height = height

    @property
    def weight(self):
        """
        float: The weight of the Pokémon.
        """
        return self._weight

    @weight.setter
    def weight(self, weight):
        """
        Set the weight of the Pokémon.

        Parameters:
        -----------
        weight : float
            The new weight value to set.
        """
        self._weight = weight

    @property
    def stats(self):
        """
        dict: A dictionary of the Pokémon's base stats, keyed by stat name (e.g. "hp").
        """
        return self._stats

    @stats.setter
    def stats(self, stats):
        """
        Set the base stats of the Pokémon.

        Parameters:
        -----------
        stats : dict
            A dictionary of the Pokémon's base stats, keyed by stat name (e.g. "hp").
        """
        self._stats = stats

    @property
    def types(self):
        """
        list of str: The types of the Pokémon.
        """
        return self._types

    @types.setter
    def types(self, types):
        """
        Set the types of the Pokémon.

        Parameters:
        -----------
        types : list of str
            The new list of types to set.
        """
        self._types = types

    @property
    def abilities(self):
        """
        list of Ability: The abilities of the Pokémon.
        """
        return self._abilities

    @abilities.setter
    def abilities(self, abilities):
        """
        Set the abilities of the Pokémon.

        Parameters:
        -----------
        abilities : list of Ability
            The new list of abilities to set.
        """
        self._abilities = abilities

    @property
    def moves(self):
        """
        list of Move: The moves that the Pokémon can learn.
        """
        return self._moves

    @moves.setter
    def moves(self, moves):
        """
        Set the moves that the Pokémon can learn.

        Parameters:
        -----------
        moves : list of Move
            The new list of moves to set.
        """
        self._moves = moves

    def __str__(self):
        """
        Return a string representation of the Pokemon object.

        Returns:
        --------
        str
            A string representation of the Pokemon object, including its name, ID, height, weight, types,
            stats, abilities, and moves.
        """
        return f"Name: {self.name}\nID: {self.ID}\nHeight: {self.height}\nWeight: {self.weight}\nTypes: {self.types}\n\nStats:\n------\n{self.stats}\n\nAbilities:\n------\n{self.abilities}\n\nMoves:\n------\n\n{self.moves}"