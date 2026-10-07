from playwright.sync_api import Locator

from autoexercise.pages.base_page import BasePage


class ProductDetailPage(BasePage):
    @property
    def info(self) -> Locator:
        return self.page.locator(".product-information")

    @property
    def name(self) -> Locator:
        return self.info.locator("h2")

    @property
    def price(self) -> Locator:
        return self.info.locator("span > span").first

    def label(self, text: str) -> Locator:
        """Detail rows such as 'Category:', 'Availability:', 'Condition:', 'Brand:'."""
        return self.info.get_by_text(text)

    def set_quantity(self, quantity: int) -> None:
        self.page.locator("#quantity").fill(str(quantity))

    def add_to_cart(self) -> None:
        self.info.get_by_role("button", name="Add to cart").click()

    # ----- reviews -----
    @property
    def review_heading(self) -> Locator:
        return self.page.get_by_text("Write Your Review")

    @property
    def review_success(self) -> Locator:
        return self.page.get_by_text("Thank you for your review.")

    def submit_review(self, name: str, email: str, text: str) -> None:
        self.page.locator("#name").fill(name)
        self.page.locator("#email").fill(email)
        self.page.locator("#review").fill(text)
        self.page.locator("#button-review").click()
