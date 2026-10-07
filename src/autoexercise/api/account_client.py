from playwright.sync_api import APIResponse

from autoexercise.api.base_client import BaseClient


class AccountClient(BaseClient):
    """User accounts. This API has no tokens. Credentials go in every request."""

    def create(self, user: dict) -> APIResponse:
        return self.post("createAccount", user)

    def update(self, user: dict) -> APIResponse:
        return self.put("updateAccount", user)

    def delete_account(self, email: str, password: str) -> APIResponse:
        return self.delete("deleteAccount", {"email": email, "password": password})

    def verify_login(self, email: str | None = None, password: str | None = None) -> APIResponse:
        form = {k: v for k, v in {"email": email, "password": password}.items() if v is not None}
        return self.post("verifyLogin", form or None)

    def get_by_email(self, email: str) -> APIResponse:
        return self.get("getUserDetailByEmail", email=email)
