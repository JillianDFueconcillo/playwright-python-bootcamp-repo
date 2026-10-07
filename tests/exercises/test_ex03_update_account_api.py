"""Exercise 3 (API): update an account and verify the change.

1. Use the new_user fixture.
2. Call account_api.update(...) with the same user data but a different `city`.
3. Assert the update response code and message.
4. Call account_api.get_by_email(...) and assert the stored city changed.
   Hint: print the response first to see the field names.
"""

import pytest

pytestmark = [pytest.mark.api, pytest.mark.exercise]


def test_update_account_changes_city():  # add the fixtures you need as arguments
    pytest.skip("TODO: complete exercise 3")
