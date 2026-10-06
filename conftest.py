import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="module") #Se define el alcance del fixture como "module" para que se ejecute una vez por módulo de prueba
def driver():
    # Inicialización del navegador Chrome
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    
    yield driver

    driver.quit() # Cierre del navegador al finalizar el test 