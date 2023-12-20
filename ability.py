from pokedex_object import PokedexObject


class Ability(PokedexObject):
    """
    A class representing an ability in the Pokémon universe.

    Attributes:
    -----------
    name : str
        The name of the ability.
    id : int
        The ID number of the ability.
    generation : str
        The generation of Pokémon games in which the ability was introduced.
    effect : str
        A description of the ability's effect.
    effectShort : str
        A short description of the ability's effect.
    pokemon : str
        The name of a Pokémon that can have this ability.

    Methods:
    --------
    __init__(self, name=None, id=None, generation=None, effect=None, effectShort=None, pokemon=None):
        Initializes a new Ability object with the given attributes.
    __str__(self):
        Returns a string representation of the Ability object, including its name, ID, generation, effect,
        short effect, and Pokémon.
    """

    def __init__(self, name=None, id=None, generation=None, effect=None, effectShort=None, pokemon=None):
        """
        Initializes a new Ability object with the given attributes.

        Parameters:
        -----------
        name : str
            The name of the ability.
        id : int
            The ID number of the ability.
        generation : str
            The generation of Pokémon games in which the ability was introduced.
        effect : str
            A description of the ability's effect.
        effectShort : str
            A short description of the ability's effect.
        pokemon : str
            The name of a Pokémon that can have this ability.
        """
        super().__init__(name, id)
        self._generation = generation
        self._effect = effect
        self._effectShort = effectShort
        self._pokemon = pokemon

    @property
    def generation(self):
        """
        str: The generation of Pokémon games in which the ability was introduced.
        """
        return self._generation

    @generation.setter
    def generation(self, value):
        """
        Set the generation of Pokémon games in which the ability was introduced.

        Parameters:
        -----------
        value : str
            The new generation value to set.
        """
        self._generation = value

    @property
    def effect(self):
        """
        str: A description of the ability's effect.
        """
        return self._effect

    @effect.setter
    def effect(self, value):
        """
        Set the description of the ability's effect.

        Parameters:
        -----------
        value : str
            The new effect value to set.
        """
        self._effect = value

    @property
    def effectShort(self):
        """
        str: A short description of the ability's effect.
        """
        return self._effectShort

    @effectShort.setter
    def effectShort(self, value):
        """
        Set the short description of the ability's effect.

        Parameters:
        -----------
        value : str
            The new effectShort value to set.
        """
        self._effectShort = value

    @property
    def pokemon(self):
        """
        str: The name of a Pokémon that can have this ability.
        """
        return self._pokemon

    @pokemon.setter
    def pokemon(self, value):
        """
        Set the name of a Pokémon that can have this ability.

        Parameters:
        -----------
        value : str
            The new pokemon value to set.
        """
        self._pokemon = value

    def __str__(self):
        return f"{self.name} is not valid" if self.name == "" else \
            f"Name:{self.name}\n" \
            f"ID: {self.ID}\n" \
            f"Generation: {self.generation}\n" \
            f"Effect: {self.effect}\n" \
            f"Effect (Short): {self.effectShort}\n" \
            f"Pokemon: {self.pokemon}\n\n"
