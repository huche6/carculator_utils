from .default_parameters import DEFAULT, EXTRA
from klausen import NamedParameters
import sys


class CarInputParameters(NamedParameters):
    """
    A class used to represent vehicles with associated type, size, technology, year and parameters.

    This class inherits from NamedParameters, located in the *klausen* package.
    It sources default parameters for all vehicle types from a dictionary in
    default_parameters and format them into an array following the structured described
    in the *klausen* package.


    :ivar sizes: List of string items e.g., ['Large', 'Lower medium', 'Medium', 'Mini', 'SUV', 'Small', 'Van']
    :vartype sizes: list
    :ivar powertrains: List of string items e.g., ['BEV', 'FCEV', 'HEV-p', 'ICEV-d', 'ICEV-g', 'ICEV-p', 'PHEV-c', 'PHEV-e']
    :vartype powertrains: list
    :ivar parameters: List of string items e.g., ['Benzene', 'CH4', 'CNG tank mass intercept',...]
    :vartype parameters: list
    :ivar years: List of integers e.g., [2017, 2040]
    :vartype years: list
    :ivar metadata: Dictionary for metadata.
    :vartype metadata: dict
    :ivar values: Dictionary for storing values, of format {'param':[value]}.
    :vartype values: dict
    :ivar iterations: Number of iterations executed by the method stochastic().
        None if static() used instead.
    :vartype iterations: int


    """

    def __init__(self):
        """Create a `klausen <https://github.com/cmutel/klausen>`__ model with the car input parameters."""
        super().__init__(None)

        parameters = DEFAULT
        extra = EXTRA

        # Ensure parameters are of valid type
        if not isinstance(parameters, dict) or not isinstance(extra, set):
            print("It seems that the passed parameters are not of dictionary type")
            sys.exit(1)

        self.sizes = sorted(
            {size for o in parameters.values() for size in o.get("sizes", [])}
        )
        self.powertrains = sorted(
            {pt for o in parameters.values() for pt in o.get("powertrain", [])}
        )
        self.parameters = sorted(
            {o["name"] for o in parameters.values()}.union(set(extra))
        )
        self.years = sorted({o["year"] for o in parameters.values()})

        self.add_car_parameters(parameters)

    def add_car_parameters(self, parameters):
        """
        Split data and metadata according to ``klausen`` convention.

        The parameters are split into the *metadata* and *values* attributes
        of the CarInputParameters class by the add_parameters() method of the parent class.

        :param parameters: A dictionary that contains parameters.
        :type parameters: dict


        """
        KEYS = {"kind", "uncertainty_type", "amount", "loc", "minimum", "maximum"}

        reformatted = {}
        for key, dct in parameters.items():
            reformatted[key] = {k: v for k, v in dct.items() if k in KEYS}
            reformatted[key]["metadata"] = {
                k: v for k, v in dct.items() if k not in KEYS
            }

        self.add_parameters(reformatted)
