from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from Pages.base_page import BasePage


class CartPage(BasePage):

    def __init__(self, browser):
        super().__init__(browser)  # Llama al constructor de la clase base

    def validar_url(self, expected_url):
        try:            
            # Esperar a que la página se cargue completamente
            if WebDriverWait(self.browser, 10).until(EC.url_to_be(expected_url)):
                return True
        except TimeoutException:
            print("La página no se cargó dentro del tiempo esperado.")
        except Exception as e:
            print(f"Ocurrió un error al cargar la página: {e}")
        

        # # Verifica que estés en la página correcta
        # current_url = self.browser.current_url
        # if current_url == 'https://tienda.personal.com.ar/cart':
        #     return True
        # else:
        #     return False