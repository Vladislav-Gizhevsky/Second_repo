"""Module descriptions needs to be here"""

def sumNums(num1: float|int, num2: float|int) -> float:
    """Please, enter only nums!"""
    try:
        return num1 + num2
    except TypeError:
        return "Open your eyes and read the function doc!!!"


def substractNums(num1: float|int, num2: float|int) -> float:
    """Please, enter only nums!"""
    try:
        return num1 - num2
    except TypeError:
        return "Open your eyes and read the function doc!!!"


def multiplyNums(num1: float|int, num2: float|int) -> float:
    """Please, enter only nums!"""
    try:
        return num1 * num2
    except TypeError:
        return "Open your eyes and read the function doc!!!"


def divideNums(num1: float|int, num2: float|int) -> float:
    """Please, enter only nums!"""
    try:
        return num1 / num2
    except ZeroDivisionError:
        return "Bruh... Dividing by zero?! Go learn some math nerd!"
    except TypeError:
        return "Open your eyes and read the function doc!!!"