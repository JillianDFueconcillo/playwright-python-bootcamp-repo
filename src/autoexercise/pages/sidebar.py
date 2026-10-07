from playwright.sync_api import Locator, Page


class Sidebar:
    """Left sidebar with categories and brands. Shown on home and products pages."""

    def __init__(self, page: Page):
        self.page = page

    @property
    def categories_heading(self) -> Locator:
        return self.page.locator(".left-sidebar").get_by_role("heading", name="Category")

    @property
    def brands_heading(self) -> Locator:
        return self.page.locator(".left-sidebar").get_by_role("heading", name="Brands")

    @property
    def brand_links(self) -> Locator:
        return self.page.locator(".brands-name a")

    def open_category(self, name: str) -> None:
        """name: 'Women', 'Men' or 'Kids'."""
        self.page.locator(f'#accordian a[href="#{name}"]').click()

    def open_subcategory(self, category: str, name: str) -> None:
        self.page.locator(f"#{category}").get_by_role("link", name=name).click()
