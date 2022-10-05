from selenium.webdriver.common.by import By

from pageObjects.MaleTshirtsPage import MaleTshirtsPage
from selenium.webdriver import ActionChains


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    erkek = (By.LINK_TEXT, "ERKEK")
    tshirts = (By.XPATH, "//a[@href='/tr-TR/TR/kategori/erkek/tisort']")

    def selectGender(self):
        button = self.driver.find_element(*HomePage.erkek)
        achains = ActionChains(self.driver)
        achains.move_to_element(button).perform()

    def selectTshirts(self):
        self.driver.find_element(*HomePage.tshirts).click()
        maleTshirtsPage = MaleTshirtsPage(self.driver)
        assert self.driver.current_url == "https://www.lcwaikiki.com/tr-TR/TR/kategori/erkek/tisort"
        return maleTshirtsPage
