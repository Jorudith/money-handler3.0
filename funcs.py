from logger import logger

def log(function):
    def wrapper():
        try:
            function()
        
        except:
            logger.exception(f"{function} Something we don't know went wrong")

    return wrapper
