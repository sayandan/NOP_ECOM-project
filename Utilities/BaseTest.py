import inspect
import logging
import pytest


@pytest.mark.usefixtures('init_driver')
class BaseTest:

    def get_logger(self):
        # logger = logging.getLogger(__name__)  # __name__ will print the test file name to the log (ie. Baseclass)
        logger_name = inspect.stack()[1][3]     # logger_name will get the name of the test method that calls this
        logger = logging.getLogger(logger_name)
        file_handler = logging.FileHandler('../Reports/Automation.log')  # fileHandler variable contains log file name
        formatter = logging.Formatter('%(asctime)s : %(levelname)s : %(name)s : %(message)s')
        file_handler.setFormatter(formatter)  # fileHandler variable now updated with format information too
        logger.handlers = []  # this is to eliminate multiple logs when using parameterized methods
        logger.addHandler(file_handler)
        logger.setLevel(logging.INFO)
        return logger
