from playwright.sync_api import Locator

from autoexercise.pages.base_page import BasePage


class TestCasesPage(BasePage):
    __test__ = False  # stops pytest from collecting this class as a test class
    path = "/test_cases"

    @property
    def heading(self) -> Locator:
        return self.page.get_by_role("heading", name="Test Cases", exact=True)
