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
