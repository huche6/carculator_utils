import warnings
from collections.abc import Mapping

import numpy as np
import stats_arrays as sa


class NamedParameters(Mapping):
    """A class for managing named parameters with associated metadata.

    Parameters
    ----------
    params : dict, optional
        A dictionary containing parameter names and their associated data.

    Attributes
    ----------
    data : dict
        A dictionary to store parameter data.
    metadata : dict
        A dictionary to store metadata associated with each parameter.
    values : dict
        A dictionary to store calculated parameter values.
    iterations : int or None
        Number of iterations for stochastic calculations, set to None by default.

    Methods
    -------
    __getitem__(key)
        Retrieve the value of a parameter.
    __setitem__(key, value)
        Not implemented. Use add_parameters to add new parameters.
    __len__()
        Return the number of parameters.
    __iter__()
        Iterate over parameter names.
    add_parameters(params)
        Add parameters to the NamedParameters instance.
    _get_amount(dct)
        Retrieve the amount from a dictionary, calculating if necessary.
    static()
        Calculate static values for parameters.
    stochastic(iterations)
        Calculate stochastic values for parameters.

    """

    def __init__(self, params=None):
        """Initialize a NamedParameters instance.

        Parameters
        ----------
        params : dict, optional
            A dictionary containing parameter names and their associated data.

        """
        self.data = {}
        self.metadata = {}
        self.values = {}
        self.iterations = None
        if params:
            self.add_parameters(params)

    def __getitem__(self, key):
        """Retrieve the value of a parameter.

        Parameters
        ----------
        key : str
            The name of the parameter.

        Returns
        -------
        float or array
            The calculated value of the parameter.

        """
        TEXT = "No calculated values found; run `.static` or `.stochastic` first"
        if not self.values:
            warnings.warn(TEXT)
        return self.values[key]

    def __setitem__(self, key, value):
        """Not implemented. Use add_parameters to add new parameters.

        Parameters
        ----------
        key : str
            The name of the parameter.
        value : Any
            The value of the parameter.

        Raises
        ------
        NotImplementedError
            Always raised to indicate that this method is not implemented.

        """
        raise NotImplementedError("Use `.add_parameters` to add new parameters")

    def __len__(self):
        """Return the number of parameters.

        Returns
        -------
        int
            The number of parameters.

        """
        return len(self.data)

    def __iter__(self):
        """Iterate over parameter names.

        Returns
        -------
        iter
            An iterator over parameter names.

        """
        return iter(self.data)

    def add_parameters(self, params):
        """Add parameters to the NamedParameters instance.

        Parameters
        ----------
        params : dict
            A dictionary containing parameter names and their associated data.

        """
        for key, value in params.items():
            self.metadata[key] = value.pop("metadata", {})
            self.data[key] = value

    def _get_amount(self, dct):
        """Retrieve the amount from a dictionary, calculating if necessary.

        Parameters
        ----------
        dct : dict
            A dictionary containing parameter data.

        Returns
        -------
        float
            The calculated amount.

        """
        if "amount" in dct:
            return dct["amount"]
        elif dct.get("kind") in ("distribution", None):
            dist = sa.uncertainty_choices[dct["uncertainty_type"]]
            median = float(dist.ppf(dist.from_dicts(dct), np.array((0.5,))))
            dct["amount"] = median
            return median

    def static(self):
        """Calculate static values for parameters."""
        # Stats_arrays parameters
        keys = sorted(
            [
                key
                for key in self.data
                if self.data[key].get("kind") in ("distribution", None)
            ]
        )
        self.values = {key: self._get_amount(self.data[key]) for key in keys}
        self.iterations = None

    def stochastic(self, iterations=1000):
        """Calculate stochastic values for parameters.

        Parameters
        ----------
        iterations : int, optional
            The number of iterations for stochastic calculations. Default is 1000.

        """
        # Stats_arrays parameters
        self.iterations = iterations
        keys = sorted(
            [
                key
                for key in self.data
                if self.data[key].get("kind") in ("distribution", None)
            ]
        )
        array = sa.UncertaintyBase.from_dicts(*[self.data[key] for key in keys])
        rng = sa.MCRandomNumberGenerator(array)
        self.values = {
            key: row.reshape((-1,)) for key, row in zip(keys, rng.generate(iterations))
        }
