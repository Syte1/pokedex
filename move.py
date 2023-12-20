from pokedex_object import PokedexObject


class Move(PokedexObject):
    """
     A class representing a move in the Pokémon games.

     Attributes:
     ----------
     name : str
         The name of the move.
     id : int
         The ID number of the move.
     generation : int
         The generation in which the move was introduced.
     accuracy : int
         The accuracy of the move, represented as a percentage (0 to 100).
     pp : int
         The number of times the move can be used before needing to be recharged.
     power : int
         The base power of the move.
     type : str
         The type of the move (e.g. "Electric", "Water", etc.).
     damage_class : str
         The category of the move (e.g. "Physical", "Special", "Status").
     effect : str
         A description of any additional effects the move may have.

     Methods:
     -------
     __init__(self, name=None, id=None, generation=None, accuracy=None, pp=None, power=None, type=None,
              damage_class=None, effect=None):
         Initializes a Move object with the specified attributes.

     """

    def __init__(self, name=None, ID=None, generation=None, accuracy=None, pp=None, power=None, type=None,
                 damage_class=None, effect=None):
        super().__init__(name, ID)
        self._generation = generation
        self._accuracy = accuracy
        self._pp = pp
        self._power = power
        self._type = type
        self._damage_class = damage_class
        self._effect = effect

    # Getter and setter methods for generation
    @property
    def generation(self):
        return self._generation

    @generation.setter
    def generation(self, generation):
        self._generation = generation

    # Getter and setter methods for accuracy
    @property
    def accuracy(self):
        return self._accuracy

    @accuracy.setter
    def accuracy(self, accuracy):
        self._accuracy = accuracy

    # Getter and setter methods for pp
    @property
    def pp(self):
        return self._pp

    @pp.setter
    def pp(self, pp):
        self._pp = pp

    # Getter and setter methods for power
    @property
    def power(self):
        return self._power

    @power.setter
    def power(self, power):
        self._power = power

    # Getter and setter methods for type
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, type):
        self._type = type

    # Getter and setter methods for damage_class
    @property
    def damage_class(self):
        return self._damage_class

    @damage_class.setter
    def damage_class(self, damage_class):
        self._damage_class = damage_class

    # Getter and setter methods for effect
    @property
    def effect(self):
        return self._effect

    @effect.setter
    def effect(self, effect):
        self._effect = effect

    def __str__(self):
        """
        Returns a formatted string representation of the object, including the
        name, ID, generation, accuracy, PP, power, type, damage class, and effect
        of the move.

        Returns:
        str: A string representation of the object with the following format:
             Name: [name]
             ID: [ID]
             Generation: [generation]
             Accuracy: [accuracy]
             PP: [pp]
             Power: [power]
             Type: [type]
             Damage Class: [damage_class]
             Effect (Short): [effect]
        """
        return f"Name: {self.name}\n" \
               f"ID: {self.ID}\n" \
               f"Generation: {self.generation}\n" \
               f"Accuracy: {self.accuracy}\n" \
               f"PP: {self.pp}\n" \
               f"Power: {self.power}\n" \
               f"Type: {self.type}\n" \
               f"Damage Class: {self.damage_class}\n" \
               f"Effect (Short): {self.effect}\n\n"
