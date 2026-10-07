from playwright.sync_api import APIResponse

from autoexercise.api.base_client import BaseClient


class CatalogClient(BaseClient):
    """Products and brands."""

    def list_products(self) -> APIResponse:
        return self.get("productsList")

    def list_brands(self) -> APIResponse:
        return self.get("brandsList")

    def search_products(self, term: str | None = None) -> APIResponse:
        form = {"search_product": term} if term is not None else None
        return self.post("searchProduct", form)
