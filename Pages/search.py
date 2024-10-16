from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from Pages.base_page import BasePage


class SearchPage(BasePage): # Hereda de BasePage

    #URL
    URL = 'https://tienda.personal.com.ar'
    #Locators:
    SEARCH_INPUT = (By.XPATH, '//input[@placeholder="Buscar en Tienda"]')


    def __init__(self, browser):
        super().__init__(browser)  # Llama al constructor de la clase base


    def cargarPagina(self):
        try:
            self.browser.get(self.URL)  # Get = carga una URL dada en el browser
            # Esperar a que la página se cargue completamente si se cargó el siguiente elemento
            self.esperar_elemento(self.SEARCH_INPUT)
        except TimeoutException:
            print("La página no se cargó dentro del tiempo esperado.")
        except Exception as e:
            print(f"Ocurrió un error al cargar la página: {e}")


    def buscar(self,texto):
        try:
            search_input = self.esperar_elemento(self.SEARCH_INPUT)
            search_input.clear()  # asegura que el nuevo texto no se mezcle con un posible texto existente
            search_input.send_keys(texto + Keys.RETURN)
        except TimeoutException:
            print("El campo de búsqueda no se encontró dentro del tiempo esperado.")
        except NoSuchElementException:
            print("El campo de búsqueda no se encontró en la página.")
        except Exception as e:
            print(f"Ocurrió un error durante la búsqueda: {e}")