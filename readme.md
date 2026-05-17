# Proyecto de Automatizacion QA - Juan Manuel Cabral

## Descripcion

Proyecto de automatización de pruebas funcionales sobre la página https://www.saucedemo.com/, desarrollado utilizando Python, Selenium WebDriver y Pytest.

El objetivo del proyecto es validar funcionalidades principales del sitio como:
-Login de usuario
- Visualización del inventario
- Agregado de productos al carrito

## Tecnologias usadas 
- Python
- Pytest
- Selenium Webdriver
- Pytest HTML
- Github

## Instalacion

git clone https:

## Instalacion de dependencias

pip install -r requirements.txt

## Funcionamiento de puebas

-Test login: Valida que el usuario pueda iniciar sesión correctamente y sea redirigido al inventario.

-Test inventory: Verifica si estamos en la pagina correcta, a través del título de la página.
Verifica que haya productos visibles en la página y también verificación de elementos de la interfaz.

-Test carrito: Verifica el agregado de productos al carrito, su contador y la coincidencia del producto agregado.

## Ejecución de pruebas

Ejecutar todos los tests con comando:

py -m pytest

## Reporte HTML

El proyecto genera automáticamente un reporte HTML con los resultados de las pruebas.


