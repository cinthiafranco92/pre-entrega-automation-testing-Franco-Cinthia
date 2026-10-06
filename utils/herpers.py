
from selenium.webdriver.common.by import By


def login_exitoso(driver):
    driver.get("https://www.saucedemo.com/")
    
    # Ingreso de credenciales y clic en Login   
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()


def verif_inventario(driver):
    #Se obtiene el título de la página y el título de la sección de inventario
    title_page = driver.title
    title_section = driver.find_element(By.CLASS_NAME, 'title').text

    return title_page, title_section

def productos_visibles(driver):
    #Se obtiene la lista de productos visibles en la página de inventario
    productos = driver.find_elements(By.CLASS_NAME, 'inventory_item')
    
    return productos