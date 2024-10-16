from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException


class BasePage:
    def __init__(self, browser):
        self.browser = browser

    # Método genérico para hacer clic en un elemento
    def click_elemento(self, locator, timeout=10):
        try:
            elemento = WebDriverWait(self.browser, timeout).until(
                EC.presence_of_element_located(locator)
            )
            elemento.click()
        except TimeoutException:
            print(f"El elemento {locator} no se encontró dentro del tiempo esperado.")
        except NoSuchElementException:
            print(f"El elemento {locator} no se encontró en la página.")
        except Exception as e:
            print(f"Ocurrió un error durante el clic en el elemento: {e}")
    
    def esperar_elemento(self, locator, timeout=10):
        """
        Espera hasta que el elemento esté presente en la pantalla.        
        retorna: El elemento web si se encuentra, o False en caso de que no se encuentre dentro del tiempo
        """
        try:
            # Esperar hasta que el elemento esté presente en el DOM y sea visible
            elemento = WebDriverWait(self.browser, timeout).until(
                EC.presence_of_element_located(locator)
            )
            return elemento
        except TimeoutException:
            print(f"El elemento con locator {locator} no se encontró dentro del tiempo esperado de {timeout} segundos.")
        except NoSuchElementException:
            print(f"El elemento {locator} no se encontró en la página.")
        except Exception as e:
            print(f"Ocurrió un error durante el clic en el elemento: {e}")           