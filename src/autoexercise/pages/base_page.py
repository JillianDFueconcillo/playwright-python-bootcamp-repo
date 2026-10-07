"""Base class for page objects plus the parts shared by every page."""

from playwright.sync_api import Locator, Page, expect

from autoexercise.pages.sidebar import Sidebar


class NavBar:
    def __init__(self, page: Page):
        self.page = page

    def _link(self, href: str) -> Locator:
        return self.page.locator(f'header a[href="{href}"]')

    @property
    def home_link(self) -> Locator:
        return self._link("/")

    @property
    def products_link(self) -> Locator:
        return self._link("/products")

    @property
    def cart_link(self) -> Locator:
        return self._link("/view_cart")

    @property
    def login_link(self) -> Locator:
        return self._link("/login")

    @property
    def logout_link(self) -> Locator:
        return self._link("/logout")

    @property
    def delete_account_link(self) -> Locator:
        return self._link("/delete_account")

    @property
    def test_cases_link(self) -> Locator:
        return self._link("/test_cases")

    @property
    def contact_link(self) -> Locator:
        return self._link("/contact_us")

    @property
    def logged_in_as(self) -> Locator:
        return self.page.locator("header").get_by_text("Logged in as")


class Footer:
    def __init__(self, page: Page):
        self.page = page

    @property
    def heading(self) -> Locator:
        return self.page.locator("#footer").get_by_role("heading", name="Subscription")

    @property
    def success_message(self) -> Locator:
        return self.page.locator("#success-subscribe")

    def scroll_into_view(self) -> None:
        self.page.locator("#footer").scroll_into_view_if_needed()

    def subscribe(self, email: str) -> None:
        # The site's own id is spelled "susbscribe_email".
        self.page.locator("#susbscribe_email").fill(email)
        self.page.locator("#subscribe").click()


class BasePage:
    path = "/"

    def __init__(self, page: Page):
        self.page = page
        self.nav = NavBar(page)
        self.footer = Footer(page)
        self.sidebar = Sidebar(page)

    def open(self):
        self.page.goto(self.path)
        return self

    # ----- shared by every page that lists products -----
    @property
    def section_title(self) -> Locator:
        return self.page.locator(".features_items .title")

    @property
    def cart_modal(self) -> Locator:
        return self.page.locator("#cartModal")

    def add_card_to_cart(self, card: Locator) -> None:
        """Hover a product card so the overlay shows, click Add to cart, wait for the dialog."""
        card.hover()
        card.locator(".product-overlay .add-to-cart").click()
        expect(self.cart_modal).to_be_visible()

    def continue_shopping(self) -> None:
        self.cart_modal.locator(".close-modal").click()
        expect(self.cart_modal).to_be_hidden()

    def view_cart_from_modal(self) -> None:
        self.cart_modal.get_by_role("link", name="View Cart").click()

    def open_product_details(self, card: Locator) -> None:
        card.get_by_role("link", name="View Product").click()
