from playwright.sync_api import Locator

from autoexercise.pages.base_page import BasePage


class AccountPage(BasePage):
    """Confirmation pages for account created and account deleted."""

    @property
    def created_heading(self) -> Locator:
        return self.page.get_by_test_id("account-created")

    @property
    def deleted_heading(self) -> Locator:
        return self.page.get_by_test_id("account-deleted")

    @property
    def continue_button(self) -> Locator:
        return self.page.get_by_test_id("continue-button")
