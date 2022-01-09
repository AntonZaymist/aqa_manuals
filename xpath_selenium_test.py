from selenium import webdriver
from selenium.webdriver.common.by import By


def test_calc(calc_driver):
    calc_driver.fullscreen_window()
    room_length = calc_driver.find_element(
        By.XPATH, "//*[@id='ln_room_id']"
    )
    room_length.clear()
    room_length.send_keys(800)
    room_width = calc_driver.find_element(
        By.XPATH, "//*[@id='wd_room_id']"
    )
    room_width.clear()
    room_width.send_keys(800)
    button = calc_driver.find_element(By.XPATH, "//*[text()='Рассчитать']")
    button.click()
    calc_driver.execute_script("window.scrollTo(0, 1000)")
    result = calc_driver.find_element(By.XPATH, "//*[text()='Требуемое количество досок ламината: ']/span").text
    assert result == '273'
