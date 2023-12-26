import numpy as np


def isarray(x):
    """
    Convert input to a NumPy array if it is not already.

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


import numpy as np


def replace_zeros_in_array(x):
    """
    Replace zeros in the input array with 1.

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
