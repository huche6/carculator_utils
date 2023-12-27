import numpy as np
import xarray as xr


def isarray(x):
    """Convert input to a NumPy array if it is not already.

    Parameters
    ----------
    x : array-like or numpy.ndarray
        Input data.

    Returns
    -------
    numpy.ndarray
        NumPy array representation of the input data.

    Notes
    -----
    If the input `x` is not already a NumPy array, it will be converted using
    `numpy.asarray`. If `x` is already a NumPy array, it will be returned as is.

    Examples
    --------
    >>> isarray([1, 2, 3])
    array([1, 2, 3])

    >>> isarray(np.array([4, 5, 6]))
    array([4, 5, 6])

    """
    return np.asarray(x) if not isinstance(x, np.ndarray) else x


def replace_values_in_array(x, functions):
    """Replace by 1 in the input array the values where the functions return True.

    Parameters
    ----------
    x : array-like or numpy.ndarray
        Input data.

    Returns
    -------
    numpy.ndarray
        An array where the input are replaced with 1 according to functions.

    """
    return np.where(functions, 1, x)


def extract_values_from_datarray(x):
    """Extract values from xarray.DataArray if applicable.

    Parameters
    ----------
    x : xarray.DataArray or any
        Input data.

    Returns
    -------
    xarray.DataArray or any
        If the input is an xarray.DataArray, returns its values; otherwise,
        returns the input unchanged.

    Examples
    --------
    >>> extract_values(xr.DataArray([1, 2, 3]))
    array([1, 2, 3])

    >>> extract_values([4, 5, 6])
    [4, 5, 6]

    """
    return x.values if isinstance(x, xr.DataArray) else x
