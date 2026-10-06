import pytest
from selenium.webdriver.common.by import By
from utils.herpers import login_exitoso, verif_inventario, productos_visibles
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# ==========================================================
# Actividad 1: Login y Validación de la página de inventario
# ==========================================================

def test_login_page(driver):
    login_exitoso(driver) #Se llama a la función login_exitoso para realizar el login exitoso
  
    #validación de la página de inventario
    assert "/inventory.html" in driver.current_url, "ERROR: la página de inventario no se cargó correctamente."


def test_verificar_inventario(driver):
  
    login_exitoso(driver) #Se llama a la función login_exitoso para realizar el login exitoso
   
    verif_inventario(driver) #Se llama a la función verif_inventario para obtener el título de la página y el título de la sección de inventario
   
    #Se valida que el título de la página de inventario sea "Swag Labs"
    assert "Swag Labs" in driver.title, "ERROR: el título de la página de inventario no coincide con el esperado."   
    #Se valida que el título de la sección de inventario sea "Products"
    assert 'Products' in driver.page_source, "ERROR: el título de la sección de inventario no coincide con el esperado."


# =================================================================================
# Actividad 2:Caso de prueba "Navegación y verificación del catálogo de productos"
# =================================================================================


def test_productos_visibles(driver):

    lista_productos = productos_visibles(driver) #Se llama a la función productos_visibles para obtener la lista de productos visibles en la página de inventario
   
    #Se valida que haya al menos un producto visible en la página de inventario
    assert len(lista_productos) > 0, "ERROR: no se encontraron productos visibles en la página de inventario."

    # assert lista_productos != "", "ERROR: no se encontraron productos visibles en la página de inventario." 


def test_obtener_primer_producto(driver):
    #Se obtiene la lista de productos visibles en la página de inventario 
    first_product = driver.find_element(By.CLASS_NAME, 'inventory_item')  # Se obtiene el primer producto visible en la página de inventario   

    first_product_name = first_product.find_element(By.CLASS_NAME, 'inventory_item_name').text
    first_product_price = first_product.find_element(By.CLASS_NAME, 'inventory_item_price').text

    #Se valida que el nombre y el precio del primer producto sean correctos
    assert first_product_name == 'Sauce Labs Backpack', "ERROR: el nombre del primer producto no coincide con el esperado."
    assert first_product_price == '$29.99', "ERROR: el precio del primer producto no coincide con el esperado."

    print(f"Primer producto: {first_product_name} | Precio: {first_product_price}")


def test_validacion_interfaz(driver):
    #Se obtienen los elementos de la interfaz de usuario en la página de inventario
    menu_button  = driver.find_element(By.ID, 'react-burger-menu-btn')
    cart_button = driver.find_element(By.CLASS_NAME, 'shopping_cart_link') 
    filtro = driver.find_element(By.CLASS_NAME, 'product_sort_container')     

    assert menu_button.is_displayed(), "ERROR: el botón de menú no está presente en la página de inventario." #Se valida que el botón de menú esté presente en la página de inventario

    assert cart_button.is_displayed(), "ERROR: el botón del carrito no está presente en la página de inventario." #Se valida que el botón del carrito esté presente en la página de inventario

    assert filtro.is_displayed(), "ERROR: el dropdown de filtrado no está presente en la página de inventario." #Se valida que el dropdown de filtrado esté presente en la página de inventario

  
# ================================================
# Actividad 3:Caso de prueba "Carrito de compras"
# ================================================

def test_add_product_to_cart(driver):
    #Se obtiene la lista de productos visibles en la página de inventario
    productos = driver.find_elements(By.CLASS_NAME, 'inventory_item')[0]
    
    #Se hace clic en el botón "Add to cart" del primer producto visible en la página de inventario
    add_to_cart_button = productos.find_element(By.CLASS_NAME, 'btn_inventory')
    add_to_cart_button.click()

    #Se espera a que el contador del carrito de compras se actualice a 1
    WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.CLASS_NAME, 'shopping_cart_badge'), '1'))

    # se re-localiza el botón del producto después de hacer clic en "Add to cart"
    btn_actualizado = productos.find_element(By.CLASS_NAME, 'btn_inventory')

    #se valida que el texto del botón haya cambiado a "Remove"
    assert btn_actualizado.text.capitalize() == 'Remove', "ERROR: el botón 'Add to cart' no cambió a 'Remove'."

def test_contador_carrito(driver):
    #Se obtiene el contador del carrito de compras
    contador_carrito = driver.find_element(By.CLASS_NAME, 'shopping_cart_badge').text

    #Se valida que el contador del carrito de compras sea igual a 1
    assert contador_carrito == '1', "ERROR: el contador del carrito de compras no es igual a 1 después de agregar un producto al carrito."


def test_navegar_carrito(driver):
    #Se hace clic en el botón del carrito de compras
    driver.find_element(By.CLASS_NAME, 'shopping_cart_link').click()

    #Se valida que la URL de la página del carrito de compras sea la correcta
    assert "/cart.html" in driver.current_url, "ERROR: la página del carrito de compras no se cargó correctamente."


def test_verificar_producto_carrito(driver):
    #Se obtiene el nombre del producto en el carrito de compras
    product_name_carrito = driver.find_element(By.CLASS_NAME, 'inventory_item_name').text


    #Se valida que el nombre del producto en el carrito de compras sea correcto
    assert product_name_carrito == 'Sauce Labs Backpack', "ERROR: el nombre del producto en el carrito de compras no coincide con el esperado."