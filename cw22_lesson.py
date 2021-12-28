from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


# def test_s_onliner(mpage_onliner_driver):
#     # link = "https://s.onliner.by/tasks"
#     # browser = webdriver.Chrome()
#     # browser.implicitly_wait(15)
#     # browser.get(link)
#     # pic_button = browser.find_element(By.CSS_SELECTOR, ".service-offers__image.service-offers__image_person.service-offers__image_person_4")
#     # button.click()
#     element_click = mpage_onliner_driver.find_element(
#         By.CSS_SELECTOR,
#         "div.service-offers__list > "
#         ":nth-of-type(4).service-offers__unit.ng-scope .service-offers__data "
#         "[data-ng-if='::searchTasksItem.data.deadline']")
#     assert element_click.text == "До 17 декабря 2021"


def test_demo_site(page_thedemosite_driver):
    name = "Anton"
    email = "test@mail.ru"
    current_address = "Moskov dubrovka"
    permanent_address = "Moskov random street"
    el_fullname = page_thedemosite_driver.find_element(By.ID, "userName")
    el_fullname.send_keys(name)

    el_email = page_thedemosite_driver.find_element(By.CSS_SELECTOR, "#userEmail")
    el_email.send_keys(email)

    el_current_address = page_thedemosite_driver.find_element(By.CSS_SELECTOR, "#currentAddress")
    el_current_address.send_keys(current_address)

    el_permanent_address = page_thedemosite_driver.find_element(By.CSS_SELECTOR, "#permanentAddress")
    el_permanent_address.send_keys(permanent_address)

    sub_button = page_thedemosite_driver.find_element(By.CSS_SELECTOR, "#submit")
    sub_button.click()

    check_name = page_thedemosite_driver.find_element(By.CSS_SELECTOR, "p#name")
    assert name in check_name.text






