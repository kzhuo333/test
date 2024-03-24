"""Docstring."""


class MyClass:
    """_summary_
    """

    def __init__(self, name: str):
        self.a = 1
        self.b = 2
        self.name = name

    def throw_exception(self):
        """_summary_

        Raises:
            ValueError: _description_
        """
        raise ValueError(f"{self.name} loves value errors!")
