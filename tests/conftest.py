import pytest
from selenium import webdriver
import time

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from selenium.webdriver.support import expected_conditions



@pytest.fixture(scope="class")
def setup(request):
    service_obj = Service("/Users/muratbilaltekin/Downloads/chromedriver");
    driver = webdriver.Chrome(service=service_obj)

    driver.get("https://www.lcwaikiki.com/tr-TR/TR/")
    assert driver.current_url == "https://www.lcwaikiki.com/tr-TR/TR/"
    driver.maximize_window()
    request.cls.driver = driver

    yield

    driver.close()

