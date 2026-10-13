"""Test Case 12: Add Products in Cart. See https://automationexercise.com/test_cases"""

import pytest

from tests.ui.test_cases.steps import verify_home_page_visible

pytestmark = [pytest.mark.ui, pytest.mark.testcases]


def test_tc12_add_products_cart(app):
    """Test Case 12: Add Products in Cart

    Steps from automationexercise.com:
    1. Launch browser
    2. Navigate to url 'http://automationexercise.com'
    3. Verify that home page is visible successfully
    4. Click 'Products' button
    5. Hover over first product and click 'Add to cart'
    6. Click 'Continue Shopping' button
    7. Hover over second product and click 'Add to cart'
    8. Click 'View Cart' button
    9. Verify both products are added to Cart
    10. Verify their prices, quantity and total price

    NOTE: This test runs with a visible browser window (headed mode) for visual testing.
    The browser_launch_args fixture in conftest.py configures headless=False for this test.
    """
    # STEP 1-2: Launch browser and navigate to the home page
    app.home.open()

    # STEP 3: Verify that home page is visible successfully
    verify_home_page_visible(app)

    # STEP 4: Click 'Products' button
    app.nav.products_link.click()

    # STEP 5-6: Hover over first product and click 'Add to cart', then Continue Shopping
    first_product = app.products.cards.nth(0)
    app.home.add_card_to_cart(first_product)
    app.home.continue_shopping()

    # STEP 7: Hover over second product and click 'Add to cart'
    second_product = app.products.cards.nth(1)
    app.home.add_card_to_cart(second_product)

    # STEP 8: Click 'View Cart' button
    app.home.view_cart_from_modal()

    # STEP 9-10: Verify both products are added to Cart with prices, quantity, and totals
    assert app.cart.rows.count() >= 2, "At least 2 products should be in cart"

    # Verify prices, quantities and totals are visible
    assert app.cart.unit_prices.count() >= 2, "Both product prices should be visible"
    assert app.cart.quantities.count() >= 2, "Both product quantities should be visible"
    assert app.cart.totals.count() >= 2, "Both product totals should be visible"
