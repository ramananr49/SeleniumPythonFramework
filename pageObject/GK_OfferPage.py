from selenium.webdriver.common.by import By


class GK_OfferPage:

    def __init__(self, driver):
        self.driver = driver

    pageSize = (By.XPATH, "//label[text()='Page size:']/following-sibling::select")
    search_Txtbox = (By.XPATH, "//label[text()='Search:']/following-sibling::input[@id='search-field']")
    vegfruitNameHeader = (By.CSS_SELECTOR, "th[aria-label*='Veg/fruit name']")
    priceHeader = (By.CSS_SELECTOR, "th[aria-label*='Price']")
    discountPriceHeader = (By.CSS_SELECTOR, "th[aria-label*='Discount price']")
    commonVegFruitRow = (By.CSS_SELECTOR, "table tbody tr")
    deliveryDateClearBtn = (By.CSS_SELECTOR, "button[class*='clear-button']")
    deliveryDateCalenderIcon = (By.CSS_SELECTOR, "button[class*='calendar-button']")
    deliverydateInput = (By.CSS_SELECTOR, "div[class*='react-date-picker'] input[name='date']")
    monthInput = (By.CSS_SELECTOR, "input[name='month']")
    dayInput = (By.CSS_SELECTOR, "input[name='day']")
    yearInput = (By.CSS_SELECTOR, "input[name='year']")

    def getPageSize(self):
        return self.driver.find_element(*GK_OfferPage.pageSize)

    def getSearchTxtBox(self):
        return self.driver.find_element(*GK_OfferPage.search_Txtbox)

    def getVegFruitNameColHeader(self):
        return self.driver.find_element(*GK_OfferPage.vegfruitNameHeader)

    def getPriceColHeader(self):
        return self.driver.find_element(*GK_OfferPage.priceHeader)

    def getDiscountPriceColHeader(self):
        return self.driver.find_element(*GK_OfferPage.discountPriceHeader)

    def getCommonVegFruitRow(self):
        return self.driver.find_elements(*GK_OfferPage.commonVegFruitRow)

    def getDeliveryDateClearBtn(self):
        return self.driver.find_element(*GK_OfferPage.deliveryDateClearBtn)

    def getDeliveryDateCalenderIcon(self):
        return self.driver.find_element(*GK_OfferPage.deliveryDateCalenderIcon)

    def getDeliveryDateInput(self):
        return self.driver.find_element(*GK_OfferPage.deliverydateInput)

    def getMonthInput(self):
        return self.driver.find_element(*GK_OfferPage.monthInput)

    def getDayInput(self):
        return self.driver.find_element(*GK_OfferPage.dayInput)

    def getYearInput(self):
        return self.driver.find_element(*GK_OfferPage.yearInput)