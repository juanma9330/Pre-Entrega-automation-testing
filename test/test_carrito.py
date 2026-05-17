from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

def test_cart(login_in_driver):
    driver = login_in_driver

    
     #agregar producto al carrito
    driver.find_elements(By.CLASS_NAME, "btn_inventory")[0].click()
    
    #verificar contador carrito
    contador_carrito = driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
    assert contador_carrito.text == "1"

    #obtener nombre del primer producto
    Nombre_producto = driver.find_elements(By.CLASS_NAME, "inventory_item_name")[0].text

    #ir al carrito
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    #nombre del producto en el carrito
    item_carrito = driver.find_element(By.CLASS_NAME, "inventory_item_name").text

    #verificar el producto agregado al carrito
    assert item_carrito == Nombre_producto, "el producto no coincide"






