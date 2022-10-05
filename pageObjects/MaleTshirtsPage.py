
from selenium.webdriver.common.by import By

from pageObjects.ProductPage import ProductPage


class MaleTshirtsPage:
    def __init__(self, driver):
        self.driver = driver

    tshirt = (By.XPATH, "//a[@href='/tr-TR/TR/urun/LC-WAIKIKI/erkek/Tisort/5906261/2419331']")

    def selectTshirt(self):
        self.driver.find_element(*MaleTshirtsPage.tshirt).click()
        assert self.driver.current_url == "https://www.lcwaikiki.com/tr-TR/TR/urun/LC-WAIKIKI/erkek/Tisort/5906261/2419331"
        productPage = ProductPage(self.driver)
        return productPage
