import logging

logger = logging.getLogger(__name__)

logger.setLevel(logging.DEBUG)

debug_file_handler = logging.FileHandler("log/debug.log")
transaction_file_handler = logging.FileHandler("log/transactions.log")

debug_file_handler.setLevel(logging.DEBUG)
transaction_file_handler.setLevel(logging.INFO)

debug_formatter = logging.Formatter("%(levelname)s - %(asctime)s - %(message)s", r"%b/%d/%Y")
transaction_formatter = logging.Formatter("%(asctime)s - %(message)s", r"%b/%d/%Y")

debug_file_handler.setFormatter(debug_formatter)
transaction_file_handler.setFormatter(transaction_formatter)

logger.addHandler(debug_file_handler)
logger.addHandler(transaction_file_handler)

logger.info("first log. initialized log files")