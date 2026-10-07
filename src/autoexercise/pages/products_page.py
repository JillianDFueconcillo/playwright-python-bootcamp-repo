from playwright.sync_api import Locator

from autoexercise.pages.base_page import BasePage


class ProductsPage(BasePage):
    path = "/products"

    @property
    def cards(self) -> Locator:
        return self.page.locator(".features_items .product-image-wrapper")

    @property
    def names(self) -> Locator:
        return self.page.locator(".features_items .productinfo p")

    @property
    def prices(self) -> Locator:
        return self.page.locator(".features_items .productinfo h2")

    @property
    def searched_heading(self) -> Locator:
        return self.page.get_by_role("heading", name="Searched Products")

    def search(self, term: str) -> None:
        self.page.locator("#search_product").fill(term)
        self.page.locator("#submit_search").click()

    def add_to_cart(self, index: int = 0) -> None:
        """Add one product and close the dialog so the next action can follow."""
        self.add_card_to_cart(self.cards.nth(index))
        self.continue_shopping()
