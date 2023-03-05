
from peyton.browser import Browser
from peyton.page import Page
from peyton.elements import Input, Button, Label, Dropdown

class LinioHomePage(Page):
    url = "https://www.linio.com.co/"
    search_box = Input(name='q')
    search_button = Button(css_selector='button[type="submit"]')

class LinioProductPage(Page):
    product_name = Label(css_selector='h1.title')
    add_to_cart_button = Button(css_selector='button[type="submit"].buy-now-button')
    size_dropdown = Dropdown(css_selector='select[name="sku_variation"]')

class LinioCartPage(Page):
    checkout_button = Button(css_selector='a.btn-primary')

def test_buy_product(browser):
    # Inicializar el navegador y cargar la página de inicio de Linio
    page = LinioHomePage(browser).open()

    # Buscar un producto y abrir su página de detalles
    page.search_box.type('iPhone')
    page.search_button.click()
    product_page = LinioProductPage(browser).open_first_result()

    # Añadir el producto al carrito y verificar que el nombre y la variante sean correctos
    product_name = product_page.product_name.text
    product_size = "128GB"
    product_page.add_to_cart_button.click()
    product_page.size_dropdown.select_by_visible_text(product_size)
    assert product_page.product_name.text == product_name, "El nombre del producto no coincide"
    assert product_page.size_dropdown.selected_option.text == product_size, "La variante del producto no coincide"

    # Ir al carrito y verificar que el producto esté en el carrito
    cart_page = LinioCartPage(browser).open()
    assert product_name in cart_page.source, "El producto no se encontró en el carrito"

    # Ir al checkout y verificar que se muestre el formulario de pago
    cart_page.checkout_button.click()
    assert "Forma de Pago" in browser.title, "No se mostró el formulario de pago"



    