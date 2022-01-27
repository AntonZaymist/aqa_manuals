from selenium.webdriver.common.by import By

class LoginPageLocators:
    EMAIL_LOCATOR = (By.XPATH, "//*[@id='id_login-username']")
    PASSWORD_LOCATRO = (By.XPATH, "//*[@id='id_login-password']")
    BUTTON_LOGGIN_LOCATOR =(By.XPATH, "//*[@id='login_form']/button")