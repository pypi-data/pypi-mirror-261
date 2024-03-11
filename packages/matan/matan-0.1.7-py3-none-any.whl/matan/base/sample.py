import numpy as np
import pandas as pd

from typing import Union
import importlib
from .. import tensile


class sample:
    def __init__(
        self,
        name: str,
        comments: str = None,
        manufactured_method: str = None,
    ):
        """class to manage your specimen parameters

         This is actually base MatAn's class, used to manage your specimens parameters and tests

         Parameters
         ----------
         name : str
             name of the sample
        comments : str
            comments to describe the sample
        manufactured_method : str
            manufactured method of the sample

        Raises
        ------
        NameError
            if name is not defined

        Examples
        --------
        FIXME: Add docs.

        """

        self.name = name
        self.comments = comments
        self.tensile_test = tensile.test(self.name)

    def composition_from_name(self, delimiter: str = "-", percent_sign="p"):
        """Method to obtain material ingridiens from name, as I usually name files extracted from machine with code allowing me to get that information from filename. For example you can name you sample 10pFDM-20pPET, and it will mean there is 20percent of addition PET as well as 10 percent of Polyolefin Elastometer addition. It can be also 90pPC-10pPET.
        Parameters
        ----------
        delimiter: str
                It is the sign that delimits your composition, in default it is - sign.
        percent_sign: str
                It is the sign takes everything before as percent, like in example 90pPC, so int before (90) will be int in your composition.

        Returns:
                Sets the composition variable into a dicts of your composition. For example from 90pPC-10pPET it will return a dict {PC: 90, PET: 10}
        """

        from .files import files

        name = self.name
        self.composition = files.find_composition(name, delimiter, percent_sign)
        return self.composition

    def modification_from_name(self, mods: list, place: int = 0):
        """Function that finds if the sample was somehow modified, for example by thermal annealing

        This can be useful in case you are testing modified samples, and you marked your filename with the letter
        describing it.  By default describing letter is

        Parameters
        ----------
        mods : list
            that is the list of potential modification you have used, for example A for annealing
        place : int
            That is placement of your describing letter in the modification name. By default it is 0, so for **A**nnealing it will be A

        Examples
        --------
        FIXME: Add docs.

        """
        from files.files import find_modification

        try:
            self.modification = find_modification(self.name, mods, place)
        except NameError:
            raise NameError("Sample name is not defined")

    def method_from_name(self, delimiter: str = "-", placement: int = 0):
        """Find the technique how the material was created

        Find the method how the material was created, what methods were used to modify it, etc. To do so it is using
        first letters of filename, so for extruded parts you can use EXT, for annealed extruded parts you can use aEXT
        etc.
                    For example if you obtained your material by FDM method containing 90pPET10prPET, you can use FDM-90pPET10prPET name, and it will set instance method variable to FDM

        Parameters
        ----------
        methods : list
            what methods you have used on your set
        delimiter : str
            what sign you wanna use to finish your method string. By default it is -

        Examples
        --------
        FIXME: Add docs.

        """
        try:
            self.method = self.name.split(delimiter)[placement]
            return self.method
        except NameError:
            raise NameError("Sample name is not defined")
