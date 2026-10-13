"""Test Case 13: Verify Product quantity in Cart. See https://automationexercise.com/test_cases"""

import pytest

from tests.ui.test_cases.steps import verify_home_page_visible

pytestmark = [pytest.mark.ui, pytest.mark.testcases]


def test_tc13_verify_quanity_cart(app):
    """Test Case 13: Verify Product quantity in Cart

    Steps from automationexercise.com:
    1. Launch browser
    2. Navigate to url 'http://automationexercise.com'
    3. Verify that home page is visible successfully
    4. Click 'View Product' for any product on home page
    5. Verify product detail is opened
    6. Increase quantity to 4
    7. Click 'Add to cart' button
    8. Click 'View Cart' button
    9. Verify that product is displayed in cart page with exact quantity

    NOTE: This test runs with a visible browser window (headed mode) for visual testing.
    The browser_launch_args fixture in conftest.py configures headless=False for this test.
    """
    # STEP 1-2: Launch browser and navigate to the home page (http://automationexercise.com)
    # Opens the base URL configured in pytest.ini or settings
    app.home.open()

    # STEP 3: Verify that home page is visible successfully
    # Checks page title contains 'Automation Exercise' and verifies the slider is visible
    verify_home_page_visible(app)

    # Navigate to products page to get clickable products
    app.nav.products_link.click()
    app.page.wait_for_load_state("networkidle", timeout=10000)

    # STEP 4: Click 'View Product' for any product
    # Get the first product card and click View Product button
    first_product = app.products.cards.first
    first_product.get_by_role("link", name="View Product").click()
    app.page.wait_for_load_state("networkidle", timeout=10000)

    # STEP 5: Verify product detail is opened
    # Check that product information section is visible
    assert app.product_detail.info.is_visible()
    
    # Store product name for verification later
    product_name = app.product_detail.name.inner_text()

    # STEP 6: Increase quantity to 4
    # Set the quantity field to 4
    app.product_detail.set_quantity(4)

    # STEP 7: Click 'Add to cart' button
    # Add the product with the specified quantity to the cart
    import time
    app.product_detail.add_to_cart()
    time.sleep(1)

    # STEP 8: Click 'View Cart' button
    # The modal appears with "Continue Shopping" and "View Cart" buttons
    # We need to wait for it and click View Cart from the modal
    from playwright.sync_api import expect
    expect(app.home.cart_modal).to_be_visible(timeout=10000)
    app.home.view_cart_from_modal()
    
    # Wait for cart page to load
    app.page.wait_for_load_state("networkidle", timeout=10000)

    # STEP 9: Verify that product is displayed in cart page with exact quantity
    # Check that the cart has the product
    item_names = app.cart.item_names
    assert item_names.count() > 0, "Cart should have at least one product"
    
    # Verify the product name is in the cart
    first_item_name = item_names.first.inner_text()
    assert product_name in first_item_name, (
        f"Expected '{product_name}' in cart, but got '{first_item_name}'"
    )
    
    # Verify the quantity is 4
    quantities = app.cart.quantities
    assert quantities.count() > 0, "Cart should have quantity information"
    quantity_text = quantities.first.inner_text()
    assert "4" in quantity_text, f"Expected quantity 4, but got '{quantity_text}'"
