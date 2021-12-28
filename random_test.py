from selenium import webdriver
from selenium.webdriver.common.by import By


def main():
    try:
        link = "https://www.onliner.by/"
        browser = webdriver.Chrome()
        browser.get(link)
        # button = browser.find_elements(By.CLASS_NAME, "fast-search__input")
        # button.send_keys("пылесос")
        elements = browser.find_elements(By.CSS_SELECTOR, "div.catalog-offers__section")

        print("ddd")
    finally:
        browser.quit()


if __name__ == "__main__":
    main()

