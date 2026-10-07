"""Exercise 4 (API): parametrized product search.

Use @pytest.mark.parametrize with the terms "top", "tshirt", "jean", and one nonsense term.
For each term, assert the response code is 200 and print how many products came back.
Then decide what a correct assertion is for the nonsense term and write it.
Name each case with pytest.param(..., id="...").
"""

import pytest

pytestmark = [pytest.mark.api, pytest.mark.exercise]


def test_search_terms():  # add the fixtures you need as arguments
    pytest.skip("TODO: complete exercise 4")
