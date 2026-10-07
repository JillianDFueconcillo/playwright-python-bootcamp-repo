from playwright.sync_api import Download, Locator

from autoexercise.pages.base_page import BasePage


class CheckoutPage(BasePage):
    path = "/checkout"

    @property
    def delivery_address(self) -> Locator:
        return self.page.locator("#address_delivery")

    @property
    def billing_address(self) -> Locator:
        return self.page.locator("#address_invoice")

    @property
    def order_review(self) -> Locator:
        return self.page.locator("#cart_info")

    def place_order(self, comment: str) -> None:
        self.page.locator("textarea[name=message]").fill(comment)
        self.page.get_by_role("link", name="Place Order").click()


class PaymentPage(BasePage):
    path = "/payment"

    def pay(self, card: dict) -> None:
        self.page.get_by_test_id("name-on-card").fill(card["name"])
        self.page.get_by_test_id("card-number").fill(card["number"])
        self.page.get_by_test_id("cvc").fill(card["cvc"])
        self.page.get_by_test_id("expiry-month").fill(card["expiry_month"])
        self.page.get_by_test_id("expiry-year").fill(card["expiry_year"])
        self.page.get_by_test_id("pay-button").click()


class OrderConfirmationPage(BasePage):
    @property
    def heading(self) -> Locator:
        return self.page.get_by_test_id("order-placed")

    @property
    def continue_button(self) -> Locator:
        return self.page.get_by_test_id("continue-button")

    def download_invoice(self) -> Download:
        with self.page.expect_download() as download_info:
            self.page.get_by_role("link", name="Download Invoice").click()
        return download_info.value
