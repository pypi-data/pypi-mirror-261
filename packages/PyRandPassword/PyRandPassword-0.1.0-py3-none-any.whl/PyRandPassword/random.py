"""
------ Random ------ *
* by MoYeRanQianZhi. *
* version = 1.0.1    *
* time = 2023-03-19  *
----------------------
"""
from numpy.random import *

from .constants import __chars__
from .password import Password


def HighQualityRandom(level=6):
    """
    Create a high quality random object.

    Parameters:
        level: The random level of the object.
    """
    return default_rng(
        int.from_bytes(
            bytes(2 ** level),
            byteorder='big',
            signed=False
        )
    )


def HighQualityRandomInt(a, b, level=6):
    """
    Return high quality random integer in range [a, b], including both end points.

    Parameters:
        a: The lowest point of the range.
        b: The highest point of the range.
        level: The random level of the password.
    """
    return HighQualityRandom(level=level).integers(low=a, high=b)


def SuperRandomInt(a, b, level=6, times=100, SuperLevel=8):
    """
    Return super random integer in range [a, b], including both end points.

    Parameters:
        a(int): The lowest point of the range.
        b(int): The highest point of the range.
        level(int): The random level of the password.
        times(int): The times of repeated random loops of the password.
        SuperLevel(int): Random level of password re-picking.
    """
    results = []
    for i in range(times):
        results.append(
            HighQualityRandomInt(
                a=a,
                b=b,
                level=level
            )
        )
    return results[
        HighQualityRandomInt(
            a=0,
            b=len(results),
            level=SuperLevel
        )
    ]


def RandomWord(words, length, level=6, times=100, SuperLevel=8):
    """
    Return a random word from chars.

    Parameters:
        words(str or list): A collection of characters to choose from.
        length(int): The length of the password.
        level(int): The random level of the password.
        times(int): The times of repeated random loops of the password.
        SuperLevel(int): Random level of password re-picking.
    """
    return words[
        SuperRandomInt(
            a=0,
            b=length,
            level=level,
            times=times,
            SuperLevel=SuperLevel
        )
    ]


class Chars:
    def __init__(self, chars):
        """
        Create a chars object.

        Parameters:
            chars(str or list): A collection of characters to be randomly selected for the password.
        """
        if chars is None:
            chars = __chars__
        self.chars = chars
        self.length = len(self.chars)


class RandomPassword(Password):
    def __init__(self, words=None, size=12, level=6, times=100, SuperLevel=8):
        """
        Random Password controller.

        Parameters:
            words(str or list): A collection of characters to choose from.
            size(int): The length of the password.
            level(int): The random level of the password.
            times(int): The times of repeated random loops of the password.
            SuperLevel(int): Random level of password re-picking.
        """
        super().__init__()
        self.chars = Chars(chars=words)
        self.random(size=size, level=level, times=times, SuperLevel=SuperLevel)

    def random(self, size=1, level=6, times=100, SuperLevel=8):
        for i in range(size):
            self.password += RandomWord(
                words=self.chars.chars,
                length=self.chars.length,
                level=level,
                times=times,
                SuperLevel=SuperLevel
            )

    def resort(self, level=6, times=1):
        """
        Resort the password.

        Parameters:
            level(int): The random resort level of the password.
            times(int): The times of repeated random resort loops of the password.
        """
        password = list(self.password)
        for i in range(times):
            HighQualityRandom(level=level).shuffle(password)
        self.password = ''.join(password)

    def reset(self, password='', place='', size=12, level=6, times=100, SuperLevel=8):
        """
        Reset a new password.

        Parameters:
            password(str): A customized password to insert into the reset password.
            place(str): The place of the customized password, must be in ['first', 'end'].
            size(int): The length of the password.
            level(int): The random level of the password.
            times(int): The times of repeated random loops of the password.
            SuperLevel(int): Random level of password re-picking.
        """
        self.random(size=size, level=level, times=times, SuperLevel=SuperLevel)
        if place == 'first':
            self.password = password + self.password
        elif place == 'end':
            self.password = self.password + password


class Demo:
    """Something demo."""

    @staticmethod
    def EnglishRandomChoiceQuestions(quantity, level=6, times=100, SuperLevel=8):
        """Generate random options for multiple choice English questions"""
        result = ''
        password = RandomPassword(
            words='ABCD',
            size=quantity,
            level=level,
            times=times,
            SuperLevel=SuperLevel
        ).get()
        for i in range(len(password)):
            result += f'{i + 1}.{password[i]}\n'
        return result


if __name__ == '__main__':
    import timeit


    def test():
        r = RandomPassword(words=__chars__)
        r.printf('print')
        r.random(size=1000)
        r.printf('print')
        r.resort()
        r.printf('print')
        r.random(size=1)
        r.printf('print')
        print(Demo.EnglishRandomChoiceQuestions(15, 12, 100, 14))


    time = timeit.timeit(test, number=1)
    print(f"\n\nTime elapsed: {time:.4f} seconds")
