import inspect
import logging
from datetime import datetime, timedelta

import pytest
from selenium.webdriver.support.select import Select


@pytest.mark.usefixtures("invokeBrowser")
class BaseClass:

    def selectByVisibleText(self, locator, text):
        select = Select(locator)
        select.select_by_visible_text(text)
        print(text+" has been selected in dropdown")

    def selectByValue(self, locator, value):
        select = Select(locator)
        select.select_by_value(value)
        print(value+" has been selected in dropdown")

    def selectByIndex(self, locator, index):
        select = Select(locator)
        select.select_by_index(index)
        print(index+" has been selected in dropdown")

    def getLogger(self):
        testCaseName = inspect.stack()[1][3]
        logger = logging.getLogger(testCaseName)
        fileHandler = logging.FileHandler("logFile.log")
        formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)
        logger.setLevel(logging.DEBUG)
        return logger

    def elementShouldBeVisible(self, locator):
        assert locator.is_displayed(), f"Element {locator} is not visible on the screen."
        print(f"Element {locator} is visible.")

    def elementShouldNotBeVisible(self, locator):
        assert not locator.is_displayed(), (f"Element {locator} is visible.")
        print(f"Element {locator} is not visible.")

    def scroll_element_into_view(self, locator):
        self.driver.execute_script("arguments[0].scrollIntoView(true);", locator)

    def get_todays_date(self, format):
        return datetime.today().strftime(format)

    def getFutureDate(self, days_ahead, format):
        futureDate = datetime.today() + timedelta(days=days_ahead)
        return futureDate.strftime(format)