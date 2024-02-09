
#selenium.
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import time

# Lista de caracteres que se pueden usar en el buscador
caracteres = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

try:
    for _ in range(33):  # Realizar la búsqueda 33 veces (cuantas veces quiero que se realize la busqueda)
        # inicia el navegador Edge 
        driver = webdriver.Edge()

        try:
            # Generar una cadena aleatoria de 5 caracteres
            busqueda = ''.join(random.choice(caracteres) for _ in range(5))

            # ir a Bing
            driver.get('https://www.bing.com/')

            # Esperar el cuadro de busqueda
            search_box = WebDriverWait(driver, 17).until(EC.presence_of_element_located((By.NAME, 'q')))
            search_box.send_keys(busqueda)

            # Presionar Enter para realizar la busqueda
            search_box.send_keys(Keys.RETURN)

            # Esperar a que la pagina se cargue totalment
            WebDriverWait(driver, 17).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

            # Esperar 3 segundos despues de la busqueda
            time.sleep(3)

            # Borrar la cadena de busqueda
            search_box.clear()

            # Esperar a que la página se cargue completamente después de borrar
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

        except Exception as e:
            print(f"Ocurrió un error durante la iteración: {e}")

        finally:
            # Cerrar el navegador despues de cada busqueda
            driver.quit()

except Exception as e:
    print(f"ocurrió un error: {e}")
