# import dependencies
# import app

# import tkinter for function purposes
import tkinter as tk

# import the main logger
from logger import logger

# app function logger
def func_log(function):
    def wrapper(amount):
        try:
            function(amount)
            logger.debug(f"{function} has been used")
        except:
            logger.warning(f"{function} Something we don't know went wrong")
    return wrapper

@func_log
def deduct_funds(amount):
    pass

@func_log
def add_funds(amount):
    pass

deduct_funds(10)