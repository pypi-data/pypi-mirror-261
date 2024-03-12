import sys

from .errors.PasswordErrors import PasswordPrintfModeError, BadPasswordError


class Password:
    def __init__(self, password=''):
        """
        Password controller.

        Parameters:
            password(str): An original password.

        Examples:
            '''
            Input:
                p = Password()
                p.set('1234567890')
                print(p.get())
            Output:
                1234567890
            '''
        """
        self.password = password

    def clear(self):
        """
        Clear the password.
        """
        self.set('')

    def set(self, password):
        """
        Set a new password.

        Parameters:
            password(str): A new password to set.
        """
        self.password = password

    def reset(self, password=''):
        """
        Reset a new password.

        Parameters:
            password(str): A new password to reset.
        """
        self.set(password)

    def get(self):
        """
        Get the password.

        return: password.
        """
        return self.password

    def printf(self, mode='sys'):
        """
        Parameters:
            mode(str): The form of the output password. Usually is 'sys', 'print'.
        """
        if mode == 'sys':
            sys.stdout.write(self.password)
            sys.stdout.flush()

        elif mode == 'print':
            print(self.password)

        else:
            raise PasswordPrintfModeError()

    def verify(self, password):
        """
        Parameters:
            password(str): The password to be verified.
        return: True or False
        """
        if password == self.password:
            return True
        else:
            return False

    def RaiseBadPassword(self, bad):
        """
        Raise a BadPasswordError.

        Parameters:
            bad(str): The bad password to be raise.
        """
        raise BadPasswordError(password=bad)

    def RaiseVerify(self, password):
        """
        Verify and raise the bad password.

        Parameters:
            password(str): The password to be verified.
        """
        if not self.verify(password=password):
            self.RaiseBadPassword(bad=password)


if __name__ == '__main__':
    p = Password()
    p.set('1234567890')
    p.printf()
    p.RaiseVerify('1234')
