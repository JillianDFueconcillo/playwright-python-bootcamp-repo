"""Test Case 8: Verify All Products and product detail page. See https://automationexercise.com/test_cases"""

import pytest

from tests.ui.test_cases.steps import verify_home_page_visible

pytestmark = [pytest.mark.ui, pytest.mark.testcases]


def test_tc08_verify_all_products(app):
    """Test Case 8: Verify All Products and product detail page

    Steps from automationexercise.com:
    1. Launch browser
    2. Navigate to url 'http://automationexercise.com'
    3. Verify that home page is visible successfully
    4. Click on 'Products' button
    5. Verify user is navigated to ALL PRODUCTS page successfully
    6. The products list is visible
    7. Click on 'View Product' of first product
    8. User is landed to product detail page
    9. Verify product details: name, category, price, availability, condition, brand

    NOTE: This test runs with a visible browser window (headed mode) for visual testing.
    The browser_launch_args fixture in conftest.py configures headless=False for this test.
    """
    # STEP 1-2: Launch browser and navigate to the home page (http://automationexercise.com)
    # Opens the base URL configured in pytest.ini or settings
    app.home.open()

    # STEP 3: Verify that home page is visible successfully
    # Checks page title contains 'Automation Exercise' and verifies the slider is visible
    verify_home_page_visible(app)

    # STEP 4: Click on 'Products' button in the navigation
    # This navigates user to the all products page
    app.nav.products_link.click()

    # STEP 5: Verify user is navigated to ALL PRODUCTS page successfully
    # Check that the page title contains 'Products'
    assert "Products" in app.page.title(), "Page title should contain 'Products'"

    # STEP 6: The products list is visible
    # Verify that the products section title is visible
    assert app.products.section_title.is_visible()

    # Verify that the first product card is visible
    assert app.products.cards.first.is_visible()

    # STEP 7: Click on 'View Product' of first product
    # Get the first product card and click View Product button
    first_product = app.products.cards.first
    first_product.get_by_role("link", name="View Product").click()

    # STEP 8-9: User is landed to product detail page and details are visible
    # Verify we're on the product detail page
    assert app.product_detail.name.is_visible()
    assert app.product_detail.price.is_visible()

    # Verify detail labels are visible: Category, Availability, Condition, Brand
    assert app.product_detail.label("Category:").is_visible()
    assert app.product_detail.label("Availability:").is_visible()
    assert app.product_detail.label("Condition:").is_visible()
    assert app.product_detail.label("Brand:").is_visible()
