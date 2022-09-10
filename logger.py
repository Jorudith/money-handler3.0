import logging
from datetime import date
import os

current_year = date.today().year

class DebugFilter(logging.Filter):
    def filter(self, record):
        if record.levelno != logging.INFO:
            return 1
        return 0

class TransactionFilter(logging.Filter):
    def filter(self, record):
        if record.levelno == logging.INFO:
            return 1
        return 0

# initialized logger and default level
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# initialized handlers (create folder first for current year)
if current_year not in os.listdir("log"):
    try: 
        os.mkdir(f"log/{current_year} logs")
    except FileExistsError:
        pass

debug_file_handler = logging.FileHandler(f"log/{current_year} logs/debug.log")
transaction_file_handler = logging.FileHandler(f"log/{current_year} logs/transactions.log")

# add log filters based on log levels 
df = DebugFilter()
debug_file_handler.addFilter(df)
tf = TransactionFilter()
transaction_file_handler.addFilter(tf)

# added levels for handlers
debug_file_handler.setLevel(logging.DEBUG)
transaction_file_handler.setLevel(logging.INFO)

# initialized formatters for each handler
debug_formatter = logging.Formatter("%(name)s - %(levelname)s - %(asctime)s - %(message)s", r"%b/%d/%Y %h:%M:%S")
transaction_formatter = logging.Formatter("%(asctime)s - %(message)s", r"%b/%d/%Y %h:%M:%S")

# inputted each formatter to respective handlers
debug_file_handler.setFormatter(debug_formatter)
transaction_file_handler.setFormatter(transaction_formatter)

# inputted each handler to logger
logger.addHandler(debug_file_handler)
logger.addHandler(transaction_file_handler)

if __name__ == "__main__":
    pass

