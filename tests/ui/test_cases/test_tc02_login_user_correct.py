"""Test Case 2: Login User with correct email and password. See https://automationexercise.com/test_cases"""

import pytest

from tests.ui.test_cases.steps import (
    delete_account_through_ui,
    verify_home_page_visible,
    verify_logged_in_as,
)

pytestmark = [pytest.mark.ui, pytest.mark.testcases]


def test_tc02_login_user_correct(app, new_user):
    app.home.open()                                           # 1-2 open the site
    verify_home_page_visible(app)                             # 3
    app.nav.login_link.click()                                # 4
    assert app.login.login_heading.is_visible()               # 5 Verify 'Login to your account' is visible
    app.login.login(new_user["email"], new_user["password"])  # 6-7
    verify_logged_in_as(app, new_user["name"])                # 8
    delete_account_through_ui(app)                            # 9-10
