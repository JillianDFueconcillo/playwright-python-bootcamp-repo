# Test Cases for Automation Exercise

This project contains 5 test cases (TC01-TC05) that test the automationexercise.com website.

## Test Cases

| Test Case | File | Purpose |
|-----------|------|---------|
| TC01 | `test_tc01_register_user.py` | Register a new user account |
| TC02 | `test_tc02_login_user_correct.py` | Login with correct credentials |
| TC03 | `test_tc03_login_user_incorrect.py` | Verify error message for incorrect login |
| TC04 | `test_tc04_logout_user.py` | Logout functionality |
| TC05 | `test_tc05_register_email.py` | **Verify error for duplicate email registration** |

## Running Tests

### Run All Test Cases
```bash
pytest tests/ui/test_cases/ -v --browser chromium
```

### Run Single Test Case
```bash
pytest tests/ui/test_cases/test_tc05_register_email.py -v --browser chromium
```

## Headed Mode (Visible Browser Window)

Test Case TC05 is configured to run with a **visible Chromium browser window** for visual testing and debugging.

### Via Command Line
```bash
pytest tests/ui/test_cases/test_tc05_register_email.py -v --browser chromium --headed
```

### Via VS Code Beaker Test Explorer
The `.vscode/settings.json` file is configured to automatically add the `--headed` flag. When you click "Run Test" in Beaker:

1. Open VS Code
2. Open the **Beaker Test Explorer** (flask icon in left sidebar)
3. Find **test_tc05_register_email**
4. Click the ▶️ **Run** button
5. A Chromium browser window should appear showing the test running in real-time ✅

### Configuration Details

The headed mode is configured in `tests/ui/conftest.py`:

```python
@pytest.fixture(scope="function")
def browser_launch_args(request):
    """Run tc05 test in headed mode when --headed flag is passed or fixture detects it."""
    if request.node.name == "test_tc05_register_email":
        return {"headless": False}
    return {}
```

This fixture checks if the test being run is `test_tc05_register_email` and returns `{"headless": False}`, which tells pytest-playwright to launch Chromium in headed mode (visible window).

## Browser Support

All tests run with **Chromium** by default. To run with a different browser:

```bash
pytest tests/ui/test_cases/ -v --browser firefox
pytest tests/ui/test_cases/ -v --browser webkit
```

## Test Markers

Tests are marked with `@pytest.mark.ui` and `@pytest.mark.testcases` for filtering:

```bash
# Run only UI tests
pytest -m ui

# Run only test cases
pytest -m testcases
```

## Notes

- **TC01-TC04** run in **headless mode** (no visible window) for speed and CI/CD compatibility
- **TC05** runs in **headed mode** (visible window) for visual testing when `--headed` flag is used
- All tests include ad-blocking and ad-hiding CSS injection to prevent ads from interfering with tests
- Tests use pytest-playwright for cross-browser automation
