from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Pages.base_page import BasePage


class ItemPage(BasePage):  # Hereda de BasePage

    #Locators:
    ITEM_COMPRARBUTTON = (By.XPATH, '//button[@class="l0q4lv1v" and text()="Comprar"]')

    def __init__(self, browser):
        super().__init__(browser)  # Llama al constructor de la clase base

    def click_comprar(self):
        # Reutilizando el método click_elemento desde la clase base
        self.click_elemento(self.ITEM_COMPRARBUTTON)        