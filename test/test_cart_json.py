from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
from utils.logger import logger
from page.inventory_page import InventoryPage
from page.cart_page import CartPage
from utils.data_reader import read_products_json

@pytest.mark.smoke
def test_cart_json(driver_logged):
    logger.info("Iniciando prueba carrito con datos JSON")
    inventory_page = InventoryPage(driver_logged)
    cart_page = CartPage(driver_logged)

    logger.info("Leyendo productos desde archivo JSON")
    productos = read_products_json()

    for producto in productos:
        inventory_page.agregar_producto_por_nombre(producto["nombre"])

    logger.info("Ingresando al carrito")
    inventory_page.ir_al_carrito()

    logger.info("Obteniendo productos del carrito")
    productos_carrito = cart_page.obtener_productos_carrito()

    for producto_json in productos:
        encontrado = False
        for producto_carrito in productos_carrito:
            if ( (producto_carrito["nombre"] == producto_json["nombre"]) and (producto_carrito["precio"] == producto_json["precio"])):
                encontrado = True
                break
        
    
        assert encontrado, f"Producto incorrecto o faltante: {producto_json['nombre']}"
        logger.info("Todos los productos fueron validados correctamente")