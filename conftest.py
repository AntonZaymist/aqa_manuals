import pytest
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


@pytest.fixture(scope="session")
def chrome_driver():
    return Chrome()


@pytest.fixture(scope="module")
def mpage_onliner_driver(chrome_driver):
    chrome_driver.get("https://s.onliner.by/tasks")
    chrome_driver.implicitly_wait(15)
    yield chrome_driver
    chrome_driver.close()


@pytest.fixture(scope="module")
def page_thedemosite_driver(chrome_driver):
    chrome_driver.get("https://demoqa.com/text-box")
    chrome_driver.implicitly_wait(10)
    yield chrome_driver
    chrome_driver.close()


@pytest.fixture(scope="module")
def calc_driver(chrome_driver):
    chrome_driver.get("https://calc.by/building-calculators/laminate.html")
    chrome_driver.implicitly_wait(10)
    yield chrome_driver
    chrome_driver.close()


@pytest.fixture(scope="module")
def hw21_ex1_driver(chrome_driver):
    chrome_driver.get("http://the-internet.herokuapp.com/login")
    chrome_driver.implicitly_wait(15)
    yield chrome_driver
    chrome_driver.close()


@pytest.fixture(scope="module")
def hw21_ex2_driver(chrome_driver):
    chrome_driver.get("https://the-internet.herokuapp.com")
    chrome_driver.implicitly_wait(15)
    yield chrome_driver
    chrome_driver.close()


@pytest.fixture(scope="module")
def hw22_driver(chrome_driver):
    chrome_driver.get("https://www.saucedemo.com/")
    chrome_driver.implicitly_wait(15)
    yield chrome_driver
    chrome_driver.close()

# @pytest.fixture()
# def searched_field(main_page_driver):
#     search_field = main_page_driver.find_element(By.ID, "searchInput")
#     search_field.send_keys("python")
#     search_field.send_keys(Keys.ENTER)
#     return main_page_driver.find_element(By.ID, "firstHeading")
