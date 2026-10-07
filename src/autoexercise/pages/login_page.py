from playwright.sync_api import Locator

from autoexercise.pages.base_page import BasePage


class LoginPage(BasePage):
    path = "/login"

    @property
    def login_heading(self) -> Locator:
        return self.page.locator(".login-form h2")

    @property
    def signup_heading(self) -> Locator:
        return self.page.locator(".signup-form h2")

    @property
    def error_message(self) -> Locator:
        return self.page.get_by_text("Your email or password is incorrect!")

    @property
    def signup_error(self) -> Locator:
        return self.page.get_by_text("Email Address already exist!")

    def login(self, email: str, password: str) -> None:
        self.page.get_by_test_id("login-email").fill(email)
        self.page.get_by_test_id("login-password").fill(password)
        self.page.get_by_test_id("login-button").click()

    def start_signup(self, name: str, email: str) -> None:
        self.page.get_by_test_id("signup-name").fill(name)
        self.page.get_by_test_id("signup-email").fill(email)
        self.page.get_by_test_id("signup-button").click()
