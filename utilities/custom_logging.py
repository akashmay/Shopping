import logging
import os


class LogGen:
    @staticmethod
    def get_logger():
        log_dir = os.path.join(os.path.abspath(os.curdir), "logs")
        log_file = os.path.join(log_dir, "logs.log")

        # Ensure the logs directory exists
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)

        logger = logging.getLogger()  # Get the root logger

        # 🔥 Clear existing handlers before configuring logging
        if logger.hasHandlers():
            logger.handlers.clear()

        logging.basicConfig(
            filename=log_file,
            format=" %(levelname)s : %(message)s : %(asctime)s",
            datefmt="%m/%d/%Y %I:%M:%S %p",
            level=logging.DEBUG
        )

        return logger


