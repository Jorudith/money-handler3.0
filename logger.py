import logging

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

# initialized handlers
debug_file_handler = logging.FileHandler("log/debug.log")
transaction_file_handler = logging.FileHandler("log/transactions.log")

# add log filters based on log levels 
df = DebugFilter()
debug_file_handler.addFilter(df)
tf = TransactionFilter()
transaction_file_handler.addFilter(tf)

# added levels for handlers
debug_file_handler.setLevel(logging.DEBUG)
transaction_file_handler.setLevel(logging.INFO)

# initialized formatters for each handler
debug_formatter = logging.Formatter("%(name)s - %(levelname)s - %(asctime)s - %(message)s", r"%b/%d/%Y %H:%M:%S")
transaction_formatter = logging.Formatter("%(asctime)s - %(message)s", r"%b/%d/%Y %H:%M:%S")

# inputted each formatter to respective handlers
debug_file_handler.setFormatter(debug_formatter)
transaction_file_handler.setFormatter(transaction_formatter)

# inputted each handler to logger
logger.addHandler(debug_file_handler)
logger.addHandler(transaction_file_handler)

if __name__ == "__main__":
    pass

my_filter = logging.Filter(__name__)

