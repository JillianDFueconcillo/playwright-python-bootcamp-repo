"""Test Case 9: Search Product. See https://automationexercise.com/test_cases"""

import pytest
from playwright.sync_api import expect

from tests.ui.test_cases.steps import verify_home_page_visible

pytestmark = [pytest.mark.ui, pytest.mark.testcases]


def test_tc09_search_products(app):
    """Test Case 9: Search Product

    Steps from automationexercise.com:
    1. Launch browser
    2. Navigate to url 'http://automationexercise.com'
    3. Verify that home page is visible successfully
    4. Click on 'Products' button
    5. Verify user is navigated to ALL PRODUCTS page successfully
    6. Enter product name in search input and click search button
    7. Verify 'SEARCHED PRODUCTS' is visible
    8. Verify all the products related to search are visible

    NOTE: This test runs with a visible browser window (headed mode) for visual testing.
    The browser_launch_args fixture in conftest.py configures headless=False for this test.
    """
    # STEP 1-2: Launch browser and navigate to the home page
    app.home.open()

    # STEP 3: Verify that home page is visible successfully
    verify_home_page_visible(app)

    # STEP 4: Click on 'Products' button in the navigation
    app.nav.products_link.click()
    app.page.wait_for_load_state("networkidle")

    # STEP 5: Verify user is navigated to ALL PRODUCTS page successfully
    assert "Products" in app.page.title()

    # STEP 6: Enter product name in search input and click search button
    app.products.search("top")

    # STEP 7: Verify 'SEARCHED PRODUCTS' is visible
    # expect() waits for the results page to load, unlike is_visible() which checks once
    expect(app.products.searched_heading).to_be_visible()

    # STEP 8: Verify all the products related to search are visible
    assert app.products.cards.count() > 0, "At least one product should be visible"
