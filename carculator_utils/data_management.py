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


def replace_zeros_in_array(x):
    """Replace zeros in the input array with 1.

    Parameters
    ----------
    x : array-like or numpy.ndarray
        Input data.

    Returns
    -------
    numpy.ndarray
        An array where zeros in the input are replaced with 1.


    Examples
    --------
    >>> replace_zeros([0, 2, 0, 4])
    array([1, 2, 1, 4])

    >>> replace_zeros(np.array([0, 0, 3, 0]))
    array([1, 1, 3, 1])

    """
    return np.where(x == 0, 1, x)


# TODO: merge with previous function ?
def replace_zeros_and_nan(x):
    """Replace zeros and NaN values in the input array with 1.

    Parameters
    ----------
    x : array-like or numpy.ndarray
        Input data.

    Returns
    -------
    numpy.ndarray
        An array where zeros and NaN values in the input are replaced with 1.

    Examples
    --------
    >>> replace_zeros_and_nan([0, 2, np.nan, 4])
    array([1., 2., 1., 4.])

    >>> replace_zeros_and_nan(np.array([0, 0, np.nan, 3]))
    array([1., 1., 1., 3.])

    """
    return np.where((x == 0) | (np.isnan(x)), 1, x)


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


def replace_below_one(x):
    """Replace values in the input array below 1 with 1.

    Parameters
    ----------
    x : array-like or numpy.ndarray
        Input data.

    Returns
    -------
    numpy.ndarray
        An array where values below 1 in the input are replaced with 1.


    Examples
    --------
    >>> replace_below_one([0.5, 1.5, 0.3, 2.0])
    array([1. , 1.5, 1. , 2. ])

    >>> replace_below_one(np.array([-0.5, 0.8, 1.2, 1.9]))
    array([1. , 0.8, 1.2, 1.9])

    """
    return np.where(x < 1, 1, x)
