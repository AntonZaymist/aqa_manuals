from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


# ДЗ
def main():
    link = "http://the-internet.herokuapp.com/"
    browser = webdriver.Chrome()
    browser.get(link)
    button = browser.find_element(By.CSS_SELECTOR, "a[href='/checkboxes']")
    button.click()
    element_click = browser.find_element(By.CSS_SELECTOR, "form#checkboxes > input:nth-child(2)")
    element_click.click()
    print("hello")


if __name__ == "__main__":
    main()


# Откройте страницу https://s.onliner.by/tasks. Откройте консоль разработчика и вкладку Elements в ней.
#
# Напишите минимально достаточный CSS-селектор:
#
# Который найдет картинку 2-ого объявления
# Который надет время размещения 4-ого объявления
# Который надет цену за работу