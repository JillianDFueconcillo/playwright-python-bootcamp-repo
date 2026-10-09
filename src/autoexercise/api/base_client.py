"""Thin wrapper over Playwright's APIRequestContext.

Important quirk of this API: the real result code is in the JSON body
("responseCode"). The HTTP status is not reliable. Use `code(response)` in tests.

Paths have no leading slash ("productsList") so they join onto the /api/ base URL.
"""

from playwright.sync_api import APIRequestContext, APIResponse


def code(response: APIResponse) -> int:
    """Return the responseCode from the JSON body.
    
    Raises:
        RuntimeError: If the response is HTML (likely a WAF block) instead of JSON
        KeyError: If the JSON doesn't contain responseCode
    """
    try:
        return response.json()["responseCode"]
    except Exception as e:
        # Check if we got a WAF block (HTML instead of JSON)
        text = response.text()
        if text.strip().startswith("<!DOCTYPE") or "Please wait while your request is being verified" in text:
            raise RuntimeError(
                f"API request blocked by WAF/server verification. Status: {response.status}. "
                "The server is throttling requests. This often happens on GitHub Actions due to shared IPs. "
                "Consider: 1) Adding request delays, 2) Using retry logic, 3) Checking server status"
            ) from e
        raise


class BaseClient:
    def __init__(self, context: APIRequestContext):
        self.context = context

    def get(self, path: str, **params) -> APIResponse:
        return self.context.get(path, params=params or None)

    def post(self, path: str, form: dict | None = None) -> APIResponse:
        return self.context.post(path, form=form)

    def put(self, path: str, form: dict | None = None) -> APIResponse:
        return self.context.put(path, form=form)

    def delete(self, path: str, form: dict | None = None) -> APIResponse:
        return self.context.delete(path, form=form)
