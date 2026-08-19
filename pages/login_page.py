from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    USERNAME_FIELD = (AppiumBy.ID, "com.example.sampleapp:id/usernameField")
    PASSWORD_FIELD = (AppiumBy.ID, "com.example.sampleapp:id/passwordField")
    LOGIN_BUTTON = (AppiumBy.ID, "com.example.sampleapp:id/loginButton")
    ERROR_TEXT = (AppiumBy.ID, "com.example.sampleapp:id/errorText")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def login(self, username: str, password: str):
        self.wait.until(EC.visibility_of_element_located(self.USERNAME_FIELD)).send_keys(username)
        self.driver.find_element(*self.PASSWORD_FIELD).send_keys(password)
        self.driver.find_element(*self.LOGIN_BUTTON).click()

    def wait_until_loaded(self):
        self.wait.until(EC.visibility_of_element_located(self.USERNAME_FIELD))

    def error_is_visible(self) -> bool:
        try:
            WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.ERROR_TEXT))
            return True
        except TimeoutException:
            return False
