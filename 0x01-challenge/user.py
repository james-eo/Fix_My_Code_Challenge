#!/usr/bin/python3
"""User class"""


class User():
    """A class representing a user.

    Attributes:
        __email (str): The email address of the user.
    """

    def __init__(self):
        """Initializes a new User object."""
        self.__email = None

    @property
    def email(self):
        """Gets the email address of the user.

        Returns:
            str: The email address.
        """
        return self.__email

    @email.setter
    def email(self, value):
        """Sets the email address of the user.

        Args:
            value (str): The email address to set.

        Raises:
            TypeError: If the value is not a string.
        """
        if not isinstance(value, str):
            raise TypeError("email must be a string")
        self.__email = value


if __name__ == "__main__":
    u = User()
    u.email = "john@snow.com"
    print(u.email)
