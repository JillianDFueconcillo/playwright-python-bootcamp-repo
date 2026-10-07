from playwright.sync_api import Locator

from autoexercise.pages.base_page import BasePage


class CartPage(BasePage):
    path = "/view_cart"

    @property
    def rows(self) -> Locator:
        return self.page.locator("#cart_info_table tbody tr")

    @property
    def item_names(self) -> Locator:
        return self.page.locator("#cart_info_table .cart_description h4 a")

    @property
    def unit_prices(self) -> Locator:
        return self.page.locator("#cart_info_table .cart_price p")

    @property
    def quantities(self) -> Locator:
        return self.page.locator("#cart_info_table .cart_quantity button")

    @property
    def totals(self) -> Locator:
        return self.page.locator("#cart_info_table .cart_total p")

    @property
    def register_login_link(self) -> Locator:
        """Link in the dialog that appears when a guest clicks Proceed To Checkout."""
        return self.page.locator("#checkoutModal").get_by_role("link", name="Register / Login")

    def remove_first_item(self) -> None:
        self.page.locator(".cart_quantity_delete").first.click()

    def proceed_to_checkout(self) -> None:
        self.page.get_by_text("Proceed To Checkout").click()
        # After clicking, either a modal appears (if not logged in) or checkout page loads.
        # Wait for navigation to complete first
        self.page.wait_for_load_state("networkidle", timeout=10000)
        # Now check if modal or checkout page appeared
        try:
            # Wait for the modal with register/login to appear (for guest users)
            self.page.locator("#checkoutModal").wait_for(state="visible", timeout=2000)
        except:
            # If modal doesn't appear, we must be logged in - wait for checkout page
            # Increase timeout to account for slower server responses
            self.page.locator("#address_delivery").wait_for(state="visible", timeout=15000)
