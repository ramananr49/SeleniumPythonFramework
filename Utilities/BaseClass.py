import inspect
import logging

import pytest
from selenium.webdriver.support.select import Select


@pytest.mark.usefixtures("invokeBrowser")
class BaseClass:

    def selectByVisibleText(self, locator, text):
        select = Select(locator)
        select.select_by_visible_text(text)
        print(text+" has been selected in dropdown")

    def getLogger(self):
        testCaseName = inspect.stack()[1][3]
        logger = logging.getLogger(testCaseName)
        fileHandler = logging.FileHandler("logFile.log")
        formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)
        logger.setLevel(logging.DEBUG)
        return logger

