"""Logger helper"""
import uuid
import logging


def logger():
    """Create python logger"""
    # Create transaction id
    transaction_id = str(uuid.uuid4())
    # Create log configurations
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | mathematical_function | {transaction_id} | %(message)s".format(transaction_id=transaction_id),
        handlers=[
            logging.StreamHandler()
        ])
    # Create logger
    logger = logging.getLogger()
    return logger
