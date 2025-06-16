import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

#To Login the webpage
@pytest.fixture
def driver():
    driver=webdriver.Chrome()
    driver.get("https://www.guvi.in/")
    driver.maximize_window()

    return driver

#To End the automation
@pytest.fixture(autouse=True)
def teardown(driver):
    yield
    driver.quit()

