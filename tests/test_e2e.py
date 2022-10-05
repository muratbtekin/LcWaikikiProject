import time
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestOne(BaseClass):

    def test_e2e(self):
        self.driver.implicitly_wait(6)
        homePage = HomePage(self.driver)
        homePage.selectGender()
        maleTshirtsPage = homePage.selectTshirts()
        productPage = maleTshirtsPage.selectTshirt()
        time.sleep(5)
        productPage.selectSize()
        productPage.addToCart()
        checkoutPage = productPage.goToCart()
        checkoutPage.selectMainLogo()
        time.sleep(3)

