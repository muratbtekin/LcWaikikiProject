from selenium.webdriver.common.by import By



class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver

    mainHeaderlogo = (By.CLASS_NAME, "main-header-logo")

    def selectMainLogo(self):
        self.driver.find_element(*CheckoutPage.mainHeaderlogo).click()
        assert self.driver.current_url == "https://www.lcwaikiki.com/tr-TR/TR"