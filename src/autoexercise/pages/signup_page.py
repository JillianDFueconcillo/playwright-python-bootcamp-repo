from playwright.sync_api import Locator

from autoexercise.pages.base_page import BasePage


class SignupPage(BasePage):
    """The 'Enter Account Information' form that follows the signup box."""

    @property
    def account_info_heading(self) -> Locator:
        return self.page.get_by_text("Enter Account Information")

    def fill_account(self, user: dict, newsletter: bool = True, offers: bool = True) -> None:
        page = self.page
        page.locator("#id_gender2" if user["title"] == "Mrs" else "#id_gender1").check()
        page.get_by_test_id("password").fill(user["password"])
        page.get_by_test_id("days").select_option(label=user["birth_date"])
        page.get_by_test_id("months").select_option(label=user["birth_month"])
        page.get_by_test_id("years").select_option(label=user["birth_year"])
        if newsletter:
            page.locator("#newsletter").check()
        if offers:
            page.locator("#optin").check()
        page.get_by_test_id("first_name").fill(user["firstname"])
        page.get_by_test_id("last_name").fill(user["lastname"])
        page.get_by_test_id("company").fill(user["company"])
        page.get_by_test_id("address").fill(user["address1"])
        page.get_by_test_id("address2").fill(user["address2"])
        page.get_by_test_id("country").select_option(label=user["country"])
        page.get_by_test_id("state").fill(user["state"])
        page.get_by_test_id("city").fill(user["city"])
        page.get_by_test_id("zipcode").fill(user["zipcode"])
        page.get_by_test_id("mobile_number").fill(user["mobile_number"])

    def submit(self) -> None:
        self.page.get_by_test_id("create-account").click()
