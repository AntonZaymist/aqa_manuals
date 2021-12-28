from selenium import webdriver
from selenium.webdriver.common.by import By


def main():
    try:
        link = "http://the-internet.herokuapp.com/"
        browser = webdriver.Chrome()
        browser.get(link)
        element = browser.find_element(By.XPATH, "//*[@id='content']/ul/li[27]/a")
        element.click()
        element2 = browser.find_element(By.XPATH, "//*[@id='content']/div/div/div/input")
        element2.send_keys('2222')
        element2.get_attribute('2222')
        # print("ddd")

    finally:
        browser.quit()


if __name__ == "__main__":
    main()


    def main():
        link = "https://s.onliner.by/tasks"
        browser = webdriver.Chrome()
        browser.get(link)
        # pic_button = browser.find_element(By.CSS_SELECTOR, ".service-offers__image.service-offers__image_person.service-offers__image_person_4")
        # button.click()
        element_click = browser.find_element(By.CSS_SELECTOR,
                                             ".service-offers__name.ng-binding and text()='Подготовить стены под обои в трех комнатах, сделать откосы - 2 шт'")
        # element_click.click()
        print("hello")


    if __name__ == "__main__":
        main()
