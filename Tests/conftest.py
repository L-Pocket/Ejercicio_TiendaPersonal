import pytest 
import selenium.webdriver
import json
import os


@pytest.fixture
def config(scope='session'): # se ejecuta 1 vez antes de correr toda la suite de tests

    # Obtener la ruta absoluta del archivo config.json
    config_path = os.path.join(os.path.dirname(__file__), '..', 'Config', 'config.json')
    
    # Leer el archivo config.json:
    with open(config_path) as config_file:
        config = json.load(config_file)

    # Validar que estos valores estén correctos antes de arrancar con los tests
    assert config['browser'] in ['Chrome', 'Edge', 'Headless Chrome']
    assert isinstance(config['implicit_wait'], int)
    assert config['implicit_wait'] > 0

    # Retorna el config para ser usado
    return config


# Fixture de Setup and cleanup de instancia
@pytest.fixture
def browser(config): #browser():
    
    #Inicializar instancia de ChromeDriver 
    # b = selenium.webdriver.Chrome()
    if config['browser'] == 'Chrome':
        b = selenium.webdriver.Chrome()
    elif config['browser'] == 'Edge':
        b = selenium.webdriver.Edge()
    elif config['browser'] == 'Headless Chrome':
        # Crear opciones para modo headless
        opts = selenium.webdriver.ChromeOptions()
        opts.add_argument('--headless')
        b = selenium.webdriver.Chrome(options=opts)
    else:
        raise Exception(f'Browser "{config["browser"]}" is not supported')
        
    b.maximize_window()
    # Espera implícita de 10 segundos en cada interacción
    # b.implicitly_wait(10)
    b.implicitly_wait(config['implicit_wait'])

    # Retorna la instancia de webdriver para el setup
    yield b

    # Finaliza la instancia de webdriver para el cleanup
    b.quit()


    