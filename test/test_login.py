from page.login_page import LoginPage
from utils.logger import logger
import pytest

@pytest.mark.smoke
def test_login_ok(driver):
    login_page = LoginPage(driver)
    
    login_page.login("standard_user","secret_sauce")

    assert "/inventory.html" in driver.current_url, "no se redirigio al inventario"

@pytest.mark.regression
def test_login_invalid_password(driver):
    login_page = LoginPage(driver)
    login_page.login("standard_user","1234")

    error = login_page.get_error_message()

    
    assert "Epic sadface: Username and password do not match any user in this service" in error
    