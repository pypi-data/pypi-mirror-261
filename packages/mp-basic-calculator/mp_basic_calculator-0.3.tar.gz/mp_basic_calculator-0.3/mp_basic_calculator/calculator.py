from typing import Union


class Calculator:
    """It's basic calculator made with python"""

    def __init__(self):
        """Initialize the calculator and internal memory"""
        self.memory = 0

    def add(self, x: Union[int, float]) -> Union[int, float]:
        """Accepts value as float or integer and adds to existing value in the memory

        Parameters:
        x: Should be integer or float
        """
        self.memory = self.memory + x
        print(self.memory)
        return self.memory

    def subtract(self, x: Union[int, float]) -> Union[int, float]:
        """Accepts value as float or integer and subtracts to existing value in the memory

        Parameters:
        x: Should be integer or float
        """
        self.memory = self.memory - x
        print(self.memory)
        return self.memory

    def multiply(self, x: Union[int, float]) -> Union[int, float]:
        """Accepts value as float or integer and multiplies to existing value in the memory

        Parameters:
        x: Should be integer or float
        """
        if self.memory == 0:
            self.memory = x
        else:
            self.memory *= x
        print(self.memory)
        return self.memory

    def divide(self, x: Union[int, float]) -> Union[int, float]:
        """Accepts value as float or integer and divides to existing value in the memory

        Parameters:
        x: Should be integer or float
        """
        if self.memory == 0:
            self.memory = x
        else:
            self.memory /= x
        print(self.memory)
        return self.memory

    def take_nth_root(self, x: Union[int, float], y: float) -> Union[int, float]:
        """Accepts value as float or integer and takes nth root, which given as second parameter as integer

        Parameters:
        x: Should be integer or float
        y: Should be integer
        """
        self.memory = x ** (1 / y)
        print(self.memory)
        return self.memory

    def clean_memory(self):
        """Cleans the memory"""
        self.memory = 0
        print(self.memory)
        return self.memory
