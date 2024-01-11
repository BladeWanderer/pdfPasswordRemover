import logging

class LoggerUtility:
    @staticmethod
    def get_logger(name, level=logging.INFO, log_format='%(asctime)s - %(levelname)s - %(message)s'):
        logging.basicConfig(level=level, format=log_format)
        return logging.getLogger(name)
