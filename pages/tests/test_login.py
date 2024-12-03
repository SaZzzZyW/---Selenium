import pytest
from selenium import webdriver
from pages.login_page import LoginPage

@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/login")
    yield driver
    driver.quit()

def test_successful_login(driver):
    """Проверка успешного входа с корректными учетными данными."""
    login_page = LoginPage(driver)
    login_page.login("tomsmith", "SuperSecretPassword!")
    assert "You logged into a secure area!" in login_page.get_flash_message()

def test_unsuccessful_login(driver):
    """Проверка входа с некорректными учетными данными."""
    login_page = LoginPage(driver)
    login_page.login("wronguser", "wrongpass")
    assert "Your username is invalid!" in login_page.get_flash_message()
