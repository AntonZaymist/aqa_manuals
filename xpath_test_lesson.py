from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


def test_xpath(calc_driver):
    elements = calc_driver.find_elements(By.XPATH, "//input")
    atr_element = calc_driver.find_element(By.XPATH, "//*[@name='email']")
    tag_class_element = calc_driver.find_element(By.XPATH, "//div[@class='order-line clearfix'][1]")
    tag_class_element_1 = calc_driver.find_element(By.XPATH, "//div[contains(@class, 'order-line clearfix')][1]")
    tag_class_element_2 = calc_driver.find_element(By.XPATH, "//*[contains(@name, 'name') and @type='text']")
    text_element = calc_driver.find_element(By.XPATH, "//*[text()='Контактный телефон:']")
    text_element_1 = calc_driver.find_element(By.XPATH, "//*[contains(text(), 'Контактный')]")
    parent_element_from_child = calc_driver.find_element(By.XPATH, "//*[@class='t3-off-canvas-body']/..")
    parent_element_from_child_1 = calc_driver.find_element(
        By.XPATH, "//*[@class='module-ct']/ancestor::div[@id='t3-off-canvas']"
    )
    find_child_element_from_parent = calc_driver.find_element(
        By.XPATH, "//*[@id='t3-off-canvas']//div[@class='module-ct']"
    )
    find_child_element_from_parent_1 = calc_driver.find_element(
        By.XPATH, "//*[@id='t3-off-canvas']/descendant::div[@class='module-ct']"
    )
    find_child_element_from_parent_2 = calc_driver.find_element(
        By.XPATH, "//*[@id='t3-off-canvas']/div[@class='t3-off-canvas-header']"
    )
    find_child_element_from_parent_3 = calc_driver.find_element(
        By.XPATH, "//*[@id='t3-off-canvas']/div[2]"
    )
    find_last_child = calc_driver.find_element(
        By.XPATH, "//*[@id='page']/*[last()]"
    )
    print('hello')
