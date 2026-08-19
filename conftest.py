import os
import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options

APPIUM_SERVER_URL = "http://127.0.0.1:4723"
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
APK_PATH = os.path.join(PROJECT_ROOT, "SampleApp", "app", "build", "outputs", "apk", "debug", "app-debug.apk")


@pytest.fixture
def driver():
    options = UiAutomator2Options()
    options.platform_name = "Android"
    options.automation_name = "UiAutomator2"
    options.device_name = "Pixel6_API34"
    options.app = APK_PATH
    options.app_package = "com.example.sampleapp"
    options.app_activity = ".LoginActivity"
    options.no_reset = False

    drv = webdriver.Remote(APPIUM_SERVER_URL, options=options)
    yield drv
    drv.quit()
