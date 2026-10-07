"""Exercise 1 (UI): parametrize the quantity test.

Start from Test Case 13 (tests/ui/test_cases/test_tc13_product_quantity.py).
It adds a product with quantity 4 and checks the cart.

1. Copy the test into this file under a new name.
2. Use @pytest.mark.parametrize to run it for quantities 1, 4, and 10.
   Give each case a readable id with pytest.param(..., id="...").
3. Assert the quantity in the cart matches each value.
4. Stretch: also assert the cart total equals unit price times quantity.
   Use parse_price from autoexercise.utils to turn "Rs. 500" into 500.
"""

import pytest

pytestmark = [pytest.mark.ui, pytest.mark.exercise]


def test_quantity_in_cart():  # add the fixtures you need as arguments
    pytest.skip("TODO: complete exercise 1")
