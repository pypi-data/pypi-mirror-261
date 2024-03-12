__all__ = [
    "STP",
    "Password",
    "RandomPassword",
]

from .password import *
from .random import *
from .constants import *


def STP(size=12, level=6, times=100, SuperLevel=8):
    """
    Sixty-Two Password.
    Parameters:
        size: The length of the password.
        level: The random level of the password.
        times: The times of repeated random loops of the password.
        SuperLevel: Random level of password re-picking.
    """
    return RandomPassword(words=ST62, size=size, level=level, times=times, SuperLevel=SuperLevel)


if __name__ == '__main__':
    STP(25).printf()
