from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class WelcomePage:
    WELCOME_TEXT = (AppiumBy.ID, "com.example.sampleapp:id/welcomeText")
    ITEM_LIST = (AppiumBy.ID, "com.example.sampleapp:id/itemList")
    LOGOUT_BUTTON = (AppiumBy.ID, "com.example.sampleapp:id/logoutButton")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def is_loaded(self) -> bool:
        return self.wait.until(EC.visibility_of_element_located(self.WELCOME_TEXT)) is not None

    def item_texts(self) -> list[str]:
        items = self.driver.find_elements(AppiumBy.CLASS_NAME, "android.widget.TextView")
        return [i.text for i in items if i.text]

    def logout(self):
        self.driver.find_element(*self.LOGOUT_BUTTON).click()
