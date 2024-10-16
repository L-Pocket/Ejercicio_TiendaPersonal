from Pages.search import SearchPage
from Pages.result import ResultPage
from Pages.item import ItemPage
from Pages.cart import CartPage

def test_searchEdge40(browser):
    # Inicialización de clases
    search_page = SearchPage(browser)
    result_page= ResultPage(browser)
    item_page = ItemPage(browser)
    cart_page = CartPage(browser)
    # Variables -- podrían ir en un archivo Variables
    texto_buscado = "Edge 40"
    texto_accesorios = "incluye accesorios"
    texto_cuotas = "Hasta 12 cuotas sin interés"
    expected_url='https://tienda.personal.com.ar/cart'
    

    # Given the user navigates to https://tienda.personal.com.ar
    search_page.cargarPagina()

    # When the user searches for “Edge 40”
    search_page.buscar(texto_buscado)

    #Then the search result title contains "Edge 40"
    assert texto_buscado.lower() in result_page.textobuscado_entitulo(), f"El titulo no contiene {texto_buscado}"    

    # Then order the results by lowest price
    result_page.ordenar_por_precio_mas_bajo()
    result_page.obtener_primer_item() 

    # And verify that 1st result contains “incluye accesorios”    
    assert texto_accesorios.lower() in result_page.incluye_accesorios(), f"El primer resultado no contiene {texto_accesorios}"    

    # And verify that 1st result contains “Hasta 12 cuotas sin interés”
    assert texto_cuotas.lower() in result_page.tiene_cuotas(), f"El primer resultado no contiene {texto_cuotas}"    

    # Then Open the 1st result
    result_page.click_item()

    # And click on “Comprar” button
    item_page.click_comprar()

    # Then the system should redirect to cart page.
    assert cart_page.validar_url(expected_url)

    # raise Exception("Incomplete test")