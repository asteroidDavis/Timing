"""
Methods for interacting with timing objects in a MySQL DB
"""
from typing import NoReturn

from timing import Timing


def store_timing() -> NoReturn:
    """
    :raises Any errors while writing to the DB
    :return:
    """
    pass


def timing_exists() -> bool:
    pass

def load_timing() -> Timing:
    pass
