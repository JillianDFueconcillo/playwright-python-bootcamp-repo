"""Exercise 2 (UI): parametrize the bad login test.

Start from Test Case 3 (tests/ui/test_cases/test_tc03_login_invalid.py).

Write one test with @pytest.mark.parametrize for these cases:
- valid email, wrong password (use the new_user fixture for the valid email)
- unknown email, any password
- empty email and empty password

Assert the user is not logged in for every case. Check what the page shows
for the empty form. It is not the same message as the other two.
Add a locator to LoginPage if you need one.
"""

import pytest

pytestmark = [pytest.mark.ui, pytest.mark.exercise]


def test_bad_logins():  # add the fixtures you need as arguments
    pytest.skip("TODO: complete exercise 2")
