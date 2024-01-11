import logging
from colorlog import ColoredFormatter

class LoggerUtility:
    @staticmethod
    # def get_logger(name, level=logging.INFO, log_format='%(asctime)s - %(levelname)s - %(message)s'):
    #     logging.basicConfig(level=level, format=log_format)
    #     return logging.getLogger(name)

    def get_logger(name, level=logging.INFO):
        logger = logging.getLogger(name)
        if not logger.hasHandlers():  # Check if the logger already has handlers
            logger.setLevel(level)

            # Define the log format with colors
            log_format = "%(log_color)s%(asctime)s - %(levelname)s - %(message)s"
            colors = {
                'DEBUG': 'reset',
                'INFO': 'green',
                'WARNING': 'yellow',
                'ERROR': 'red',
                'CRITICAL': 'bold_red',
            }

            # Create a formatter with color support
            formatter = ColoredFormatter(log_format, log_colors=colors)

            # Create a stream handler and set the formatter
            stream_handler = logging.StreamHandler()
            stream_handler.setFormatter(formatter)

            # Add the handler to the logger
            logger.addHandler(stream_handler)

        return logger
