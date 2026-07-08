from page.login_page import LoginPage
from utils.data_reader import read_user_csv
import pytest
from utils.logger import logger

@pytest.mark.regression
@pytest.mark.parametrize("user",read_user_csv())
def test_login(driver,user):
    logger.info("inicializando el driver para test login")
    login_page = LoginPage(driver)

    logger.info("ingresando los datos")

    login_page.login(user["username"],user["password"])

    logger.info("iniciando sesion")


    if user["valid"] == "true":
        assert "/inventory.html" in driver.current_url, "no se redirigio al inventario"

        logger.info("sesion iniciada correctamente")
    else:
        error =login_page.get_error_message()
        assert "Epic sadface" in error

        logger.info("error de inicio de sesion")
    
