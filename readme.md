# Proyecto de Automatizacion QA - Juan Manuel Cabral

## Descripcion

Proyecto de automatización de pruebas funcionales y de API desarrollado con Python.

El objetivo es validar funcionalidades principales de la web https://www.saucedemo.com/ y realizar pruebas utilizando una estructura  organizada con Page Object Model, datos externos y reportes de  ejecución.

## Tecnologias usadas 
- Python
- Pytest
- Selenium WebDriver
- Behave (BDD)
- Requests
- Pytest HTML
- Pytest Check
- Git / Github


## Instalacion

git clone (https://github.com/juanma9330/Pre-Entrega-automation-testing.git)

## Instalacion de dependencias

pip install -r requirements.txt

## Funcionalidades automatizadas

- Login

Se validan diferentes escenarios:

    Login exitoso.
    Usuario incorrecto.
    Contraseña incorrecta.
    Campos vacíos.
    Datos parametrizados desde archivo CSV.
    Escenarios BDD utilizando Behave.
    
- Inventario

Se verifica:

    Correcta carga de la página de inventario.
    Título de la página.
    Visualización de productos.
    Elementos principales de la interfaz.

- Carrito de compras

Se valida:

    Agregado de productos al carrito.
    Actualización del contador.
    Coincidencia de productos agregados.
    Validación de productos utilizando datos externos desde JSON.

- Pruebas API

Se realizan pruebas sobre ReqRes:

    Login exitoso.
    Login sin contraseña.
    Login sin email.
    Creación de usuarios.
    Obtención de usuarios.
    Eliminación de usuarios.

## Marcadores disponibles

El proyecto utiliza markers de Pytest:

smoke       -> pruebas críticas del sistema
regression  -> pruebas de regresión
api         -> pruebas de api
ui          -> pruebas de interfaz

## Ejecución de pruebas

- Ejecutar todos los tests con comando:

py -m pytest

- Ejecutar pruebas API:

py -m pytest -m api

- Ejecutar pruebas UI:

py -m pytest -m ui

- Ejecutar pruebas Smoke:

py -m pytest -m smoke

- Ejecutar pruebas regression:

py -m pytest -m regression

- Ejecutar pruebas BDD:

py -m behave

## Reporte HTML

El proyecto genera automáticamente un reporte HTML con los resultados de las pruebas ejecutadas.


El reporte incluye:

    Estado de cada prueba (Passed / Failed).
    Tiempo de ejecución.
    Detalle de errores.
    Screenshots automáticos en caso de fallos durante pruebas.

Las capturas se almacenan en:

reports/screenshots

Se implementó un sistema de logs para registrar:

Inicio de pruebas.
Acciones realizadas.
Validaciones ejecutadas.
Resultado de los escenarios.
