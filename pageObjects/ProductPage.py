from selenium.webdriver.common.by import By

from pageObjects.CheckoutPage import CheckoutPage


class ProductPage:
    def __init__(self, driver):
        self.driver = driver

    size = (By.XPATH, "//*[@id='option-size']/a[1]")

    addToCartButton = (By.XPATH, "//*[@id='pd_add_to_cart']")

    goToCartButton = (By.XPATH, "//span[text()='Sepetim']")


    def selectSize(self):
        self.driver.find_element(*ProductPage.size).click()


    def addToCart(self):
        self.driver.find_element(*ProductPage.addToCartButton).click()

    def goToCart(self):
        self.driver.find_element(*ProductPage.goToCartButton).click()
        checkoutPage = CheckoutPage(self.driver)
        assert self.driver.current_url == "https://www.lcwaikiki.com/tr-TR/TR/sepetim"
        return checkoutPage



#     keys = (By.ID, "country")
#     india = (By.LINK_TEXT, "India")
#     check = (By.XPATH, "//*[@class='checkbox checkbox-primary']")
#     submitText = (By.XPATH, "//*[@type='submit']")
#
#     def sendKeys(self):
#         return self.driver.find_element(*ConfirmPage.keys)
#     #self.driver.find_element(By.ID, "country").send_keys("ind")
#
#     def choose(self):
#         return self.driver.find_element(*ConfirmPage.india)
#     #self.driver.find_element(By.LINK_TEXT, "India").click()
#
#     def checkBox(self):
#         return self.driver.find_element(*ConfirmPage.check)
#     #self.driver.find_element(By.XPATH, "//*[@class='checkbox checkbox-primary']").click()
#
#     def submit(self):
#         return self.driver.find_element(*ConfirmPage.submitText)
#
#     #self.driver.find_element(By.XPATH, "//*[@type='submit']").click()