"""Exercise 5 (UI + API): the product page shows what the API returns.

1. Get all products from catalog_api.list_products().
2. Open the products page and count the cards.
3. Assert both counts match.
4. Stretch: compare the set of product names from both sources.
Both markers (ui and api) apply, so mix the fixtures from both layers.
"""

import pytest

pytestmark = [pytest.mark.ui, pytest.mark.api, pytest.mark.exercise]


def test_ui_matches_api():  # add the fixtures you need as arguments
    pytest.skip("TODO: complete exercise 5")
