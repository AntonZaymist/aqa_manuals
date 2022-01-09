from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://ru.wikipedia.org")
field_search_text = 'searchInput'
field_search = driver.find_element(By.ID, field_search_text)
field_search.send_keys("python")
field_search.send_keys(Keys.ENTER)
heading_field = driver.find_element(By.ID, "firstHeading")
# driver.close()



