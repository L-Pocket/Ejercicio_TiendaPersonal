from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from Pages.base_page import BasePage


class ResultPage(BasePage): # Hereda de BasePage

    #Locators:
    TITLE = (By.XPATH, '//h1[text()="Resultados Edge 40"]')
    ACCESORIOS = (By.XPATH, '(//div[text()="Incluye accesorios"])[1]')
    CUOTAS = (By.XPATH, '(//strong[text()="Hasta 12 cuotas sin interés"])[1]')
    FIRST_ITEM = (By.XPATH, '//div[@class="emsye87w"]/a[1]')
    SORT_DROPDOWN = (By.XPATH, '//div[@class="_1qzmwzw3i"]')  # Selector para el dropdown    
    # SORT_LOWEST_PRICE = (By.XPATH, '//a[@class="emsye86u"][2]')  # Selector para "Menor precio"
    SORT_LOWEST_PRICE = (By.XPATH, '//a/span[.="Menor precio"]')  # Selector para "Menor precio"


    def __init__(self, browser):
        super().__init__(browser)  # Llama al constructor de la clase base


    def textobuscado_entitulo(self):
        result_title = self.browser.find_element(*self.TITLE) 
        return result_title.text.lower()  # devuelve el text del elemento encontrado
    

    def ordenar_por_precio_mas_bajo(self):
        # Hacer clic en el dropdown para desplegar las opciones
        dropdown = self.browser.find_element(*self.SORT_DROPDOWN)         
        dropdown.click()
        # Seleccionar la opción "Menor precio"
        self.browser.find_element(*self.SORT_LOWEST_PRICE)   


    def obtener_primer_item(self):  # verifica que haya al menos un resultado  
        try:
            # Esperar a que los resultados se muestren en pantalla
            if self.esperar_elemento(self.FIRST_ITEM):
                return True            
        except TimeoutException:
            print("No se encontró el item dentro del tiempo esperado.")
        except NoSuchElementException:
            print("El item no se encontró en la página.")
        except Exception as e:
            print(f"Ocurrió un error durante la búsqueda: {e}")
        

    def incluye_accesorios(self):
        try:
            # Esperar a que aparezca el primer "Incluye accesorios"
            accesorio_element = self.esperar_elemento(self.ACCESORIOS)
            return accesorio_element.text.lower() 
        except TimeoutException:
            print("El texto 'Incluye accesorios' no se encontró dentro del tiempo esperado.")            
        except NoSuchElementException:
            print("No se encontró el elemento 'Incluye accesorios' en la página.")            
        except Exception as e:
            print(f"Ocurrió un error durante la validación: {e}")
            
    
    def tiene_cuotas(self):
        try:
            # Esperar a que aparezca el primer "CUOTAS"
            cuota_element = self.esperar_elemento(self.CUOTAS)
            return cuota_element.text.lower() 
        except TimeoutException:
            print("El texto 'cuotas sin interés' no se encontró dentro del tiempo esperado.")            
        except NoSuchElementException:
            print("No se encontró el elemento 'cuotas sin interés' en la página.")            
        except Exception as e:
            print(f"Ocurrió un error durante la validación: {e}")
    

    def click_item(self):
        # Reutilizando el método click_elemento desde la clase base
        self.click_elemento(self.FIRST_ITEM)
