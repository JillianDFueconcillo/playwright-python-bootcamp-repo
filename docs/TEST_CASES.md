# Test Case Traceability

The site publishes 26 test cases at https://automationexercise.com/test_cases. This repo implements every one as a UI test. Test cases with a matching API endpoint also have an API test.

Every test name starts with `tcNN`, where NN is the number on the site. Every step in the code carries the site's step number as a comment.

Run by number:

```bash
pytest -k tc14                      # UI and API tests for test case 14
pytest -k "tc01 or tc02"            # several
pytest -m testcases                 # all numbered tests
pytest -m "testcases and api"       # API ones only
```

## Table

| TC | Title | UI test | API test |
| --- | --- | --- | --- |
| 1 | Register User | `test_tc01_register_user.py` | `test_tc01_register_user_api` |
| 2 | Login with correct email and password | `test_tc02_login_valid.py` | `test_tc02_login_with_correct_credentials_api` |
| 3 | Login with incorrect email and password | `test_tc03_login_invalid.py` | `test_tc03_login_with_incorrect_credentials_api` |
| 4 | Logout User | `test_tc04_logout.py` | not applicable: no logout endpoint |
| 5 | Register with existing email | `test_tc05_register_existing_email.py` | `test_tc05_register_with_existing_email_api` |
| 6 | Contact Us Form | `test_tc06_contact_us.py` | not applicable |
| 7 | Verify Test Cases Page | `test_tc07_test_cases_page.py` | not applicable |
| 8 | All Products and product detail page | `test_tc08_products_and_detail.py` | `test_tc08_products_data_api` (name, price, brand, category only) |
| 9 | Search Product | `test_tc09_search_product.py` | `test_tc09_search_product_api` |
| 10 | Subscription on home page | `test_tc10_subscription_home.py` | not applicable |
| 11 | Subscription on cart page | `test_tc11_subscription_cart.py` | not applicable |
| 12 | Add Products in Cart | `test_tc12_add_products_to_cart.py` | not applicable: no cart endpoint |
| 13 | Verify Product quantity in Cart | `test_tc13_product_quantity.py` | not applicable |
| 14 | Place Order: Register while Checkout | `test_tc14_order_register_while_checkout.py` | not applicable: no order endpoint |
| 15 | Place Order: Register before Checkout | `test_tc15_order_register_before_checkout.py` | not applicable |
| 16 | Place Order: Login before Checkout | `test_tc16_order_login_before_checkout.py` | not applicable. The UI test creates its user through the API. |
| 17 | Remove Products From Cart | `test_tc17_remove_from_cart.py` | not applicable |
| 18 | View Category Products | `test_tc18_category_products.py` | `test_tc18_category_data_api` (category data only) |
| 19 | View and Cart Brand Products | `test_tc19_brand_products.py` | `test_tc19_brand_data_api` (brand data only) |
| 20 | Search Products and Verify Cart After Login | `test_tc20_search_then_cart_after_login.py` | `test_tc20_search_results_api` (search half only) |
| 21 | Add review on product | `test_tc21_add_review.py` | not applicable |
| 22 | Add to cart from Recommended items | `test_tc22_recommended_items.py` | not applicable |
| 23 | Verify address details in checkout page | `test_tc23_checkout_address_details.py` | not applicable |
| 24 | Download Invoice after purchase order | `test_tc24_download_invoice.py` | not applicable |
| 25 | Scroll Up using Arrow button | `test_tc25_scroll_up_with_arrow.py` | not applicable |
| 26 | Scroll Up without Arrow button | `test_tc26_scroll_up_without_arrow.py` | not applicable |

UI files live in `tests/ui/test_cases/`. API tests live in `tests/api/test_cases/test_api_testcases.py`.

## Where the code departs from the site's wording

- TC 18 names Dress in step 5 but expects `WOMEN - TOPS PRODUCTS` in step 6. The test opens Tops.
- TC 14, 15, 16, 23, 24 verify the `Order Placed!` page. The site flashes `Your order has been placed successfully!` for a moment and then moves on, so a check on the flash is unreliable.
- TC 9 and TC 20 search for `jeans`. Every result name contains the word, which makes the check exact.
- TC 20 adds every search result to the cart, then checks the same items after login.
- TC 5 and TC 20 use the API fixture `new_user` for the existing account.
- TC 1, 14, 15, 23, 24 register through the browser. They use `signup_user`, which deletes the account through the API afterward if the test fails before reaching the delete step.

## Building blocks

| Piece | File |
| --- | --- |
| Shared steps (home visible, sign up, delete account, pay) | `tests/ui/test_cases/steps.py` |
| All page objects in one handle | `src/autoexercise/pages/app.py`, fixture `app` |
| Card, email, and user data | `src/autoexercise/data.py` |
