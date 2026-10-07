from playwright.sync_api import Locator

from autoexercise.pages.base_page import BasePage


class HomePage(BasePage):
    path = "/"

    @property
    def slider(self) -> Locator:
        return self.page.locator("#slider")

    @property
    def featured_items(self) -> Locator:
        return self.page.locator(".features_items .product-image-wrapper")

    @property
    def recommended_heading(self) -> Locator:
        return self.page.get_by_role("heading", name="recommended items")

    @property
    def active_recommended_item(self) -> Locator:
        return self.page.locator(".recommended_items .item.active").first

    def add_recommended_to_cart(self) -> str:
        """Add the visible recommended product to the cart. Returns its name."""
        item = self.active_recommended_item
        name = item.locator(".productinfo p").first.inner_text()
        item.locator(".add-to-cart").first.click()
        return name
