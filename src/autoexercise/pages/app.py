"""One object that holds every page object.

Long flows (register, add to cart, check out, pay) touch many pages.
Passing one `app` argument keeps those tests readable and does not open any page by itself.

    def test_example(app):
        app.home.open()
        app.home.nav.login_link.click()
        app.login.login(email, password)
"""

from playwright.sync_api import Page

from autoexercise.pages.account_page import AccountPage
from autoexercise.pages.cart_page import CartPage
from autoexercise.pages.checkout_page import CheckoutPage, OrderConfirmationPage, PaymentPage
from autoexercise.pages.contact_page import ContactPage
from autoexercise.pages.home_page import HomePage
from autoexercise.pages.login_page import LoginPage
from autoexercise.pages.product_detail_page import ProductDetailPage
from autoexercise.pages.products_page import ProductsPage
from autoexercise.pages.signup_page import SignupPage
from autoexercise.pages.test_cases_page import TestCasesPage


class App:
    def __init__(self, page: Page):
        self.page = page
        self.home = HomePage(page)
        self.login = LoginPage(page)
        self.signup = SignupPage(page)
        self.account = AccountPage(page)
        self.contact = ContactPage(page)
        self.test_cases = TestCasesPage(page)
        self.products = ProductsPage(page)
        self.product_detail = ProductDetailPage(page)
        self.cart = CartPage(page)
        self.checkout = CheckoutPage(page)
        self.payment = PaymentPage(page)
        self.order = OrderConfirmationPage(page)

    # Parts shared by every page. The home page object carries them.
    @property
    def nav(self):
        return self.home.nav

    @property
    def footer(self):
        return self.home.footer

    @property
    def sidebar(self):
        return self.home.sidebar
