from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
from page.inventory_page import InventoryPage
from page.login_page import LoginPage
from utils.logger import logger


@pytest.mark.ui
def test_inventory_title(driver_logged):
    logger.info("Iniciando prueba validar titulo del inventario")
    inventory_page=InventoryPage(driver_logged)

    logger.info("Obteniendo titulo de la pagina")
    titulo =  inventory_page.obtener_titulo()

    logger.info(f"Titulo obtenido: {titulo}")
    assert titulo == "Swag Labs", "El titulo de la pagina no es correcto"
    logger.info("Titulo validado correctamente")

@pytest.mark.smoke
def test_productos_visibles(driver_logged):
    logger.info("Iniciando prueba validar productos visibles")
    inventory_page=InventoryPage(driver_logged)

    logger.info("Obteniendo lista de productos")
    productos =  inventory_page.obtener_productos()

    logger.info(f"Cantidad de productos encontrados: {len(productos)}")
    assert len(productos) > 0, "No hay productos visibles"

    logger.info("Productos visibles correctamente")


@pytest.mark.ui
def test_ui_elements(driver_logged):
    logger.info("Iniciando prueba validar elementos UI")
    inventory_page=InventoryPage(driver_logged)

    logger.info("Validando menu lateral")
    assert inventory_page.menu_visible(), "El menu no está presente en la pagina"
    logger.info("Menu visible correctamente")

    logger.info("Validando filtro de productos")
    assert  inventory_page.filtro_visible(), "El filtro no está presente en la pagina"
    logger.info("Filtro visible correctamente")




