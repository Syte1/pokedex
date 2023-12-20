from abc import ABC


class PokedexObject(ABC):
    """
    An abstract base class representing an object in the Pokédex.

    Attributes:
    -----------
    name : str
        The name of the object.
    ID : int
        The ID number of the object.

    Methods:
    --------
    __init__(self, name, ID):
        Initializes a new PokedexObject with the given name and ID.
    """

    def __init__(self, name, ID):
        """
        Initializes a new PokedexObject with the given name and ID.

        Parameters:
        -----------
        name : str
            The name of the object.
        ID : int
            The ID number of the object.
        """
        self._name = name
        self._ID = ID

    @property
    def name(self):
        """
        str: The name of the object.
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Set the name of the object.

        Parameters:
        -----------
        name : str
            The new name value to set.
        """
        self._name = name

    @property
    def ID(self):
        """
        int: The ID number of the object.
        """
        return self._ID

    @ID.setter
    def ID(self, ID):
        """
        Set the ID number of the object.

        Parameters:
        -----------
        ID : int
            The new ID number value to set.
        """
        self._ID = ID