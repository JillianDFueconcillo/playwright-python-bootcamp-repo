# Troubleshooting

| Symptom | Cause and fix |
| --- | --- |
| `ModuleNotFoundError: autoexercise` | Run `pytest` from the repo root. `pytest.ini` sets `pythonpath = src`. |
| `Executable doesn't exist` | Run `playwright install chromium`. |
| `command not found: pytest` | Activate the virtual environment. |
| Test passes locally, fails in CI | Download the CI trace from the run's Artifacts section and open it with `playwright show-trace`. |
| `strict mode violation` | Your locator matches several elements. Narrow it with `.first`, `.filter(...)`, or a better locator. |
| `Timeout ... waiting for expect` | The element is missing or the text differs. Open the trace to see the page at that moment. |
| Click fails with "intercepts pointer events" | An ad covers the element. Use the `page` fixture from `tests/ui/conftest.py`, which blocks ads. |
| URL assertion fails because of `#google_vignette` | The site appends that to the URL after an ad. Match the URL with a regex, not an exact string. |
| API assertion fails on HTTP status | This API puts the result in the body. Assert `code(response)`, not `response.status`. |
| `KeyError: 'responseCode'` | The response is not JSON. Print `response.text()`. The site may be rate limiting or showing a block page. |
| Intermittent failure | The practice site is shared and public. Re-run once. If it fails again, it is your test. Never add `time.sleep`. |
| Corporate proxy or VPN blocks the site | Set `HTTPS_PROXY`, or ask your IT team to allow automationexercise.com. |
| Windows script activation error | Run `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned` in PowerShell. |

## Debugging tools

- `pytest --headed --slowmo 500` shows the browser at half speed.
- `PWDEBUG=1 pytest -k <name>` opens the Playwright Inspector.
- `page.pause()` stops the test at that line and opens the Inspector.
- `playwright codegen https://automationexercise.com` records actions as code. Use it to find locators, then move them into page objects.
- `print(response.text())` shows an API body.

## Leftover test users

If a test run is killed, its user may stay on the site. They use emails like `qa.<random>@example.com`. They do no harm. Delete one with `account_api.delete_account(email, password)` if you need to.
