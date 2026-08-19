from pages.login_page import LoginPage
from pages.welcome_page import WelcomePage


def test_successful_login_navigates_to_welcome(driver):
    login_page = LoginPage(driver)
    login_page.login("admin", "password123")

    welcome_page = WelcomePage(driver)
    assert welcome_page.is_loaded()


def test_failed_login_shows_error(driver):
    login_page = LoginPage(driver)
    login_page.login("admin", "wrong-password")

    assert login_page.error_is_visible()


def test_welcome_screen_lists_items(driver):
    login_page = LoginPage(driver)
    login_page.login("admin", "password123")

    welcome_page = WelcomePage(driver)
    assert welcome_page.is_loaded()
    texts = welcome_page.item_texts()
    assert "Design Verification" in texts


def test_logout_returns_to_login(driver):
    login_page = LoginPage(driver)
    login_page.login("admin", "password123")

    welcome_page = WelcomePage(driver)
    welcome_page.is_loaded()
    welcome_page.logout()

    login_page.wait_until_loaded()
    assert login_page.error_is_visible() is False
