from playwright.sync_api import sync_playwright
import time

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto('https://automationexercise.com')
    page.wait_for_load_state('networkidle')
    
    # Get first product and click view product
    first_product = page.locator('.features_items .product-image-wrapper').first
    first_product.get_by_role('link', name='View Product').click()
    page.wait_for_load_state('networkidle')
    
    # Wait for quantity field to appear
    page.locator('#quantity').wait_for(state='visible', timeout=10000)
    
    # Set quantity
    page.locator('#quantity').fill('4')
    time.sleep(1)
    
    # Add to cart
    page.locator('.product-information').get_by_role('button', name='Add to cart').click()
    
    # Wait a bit
    time.sleep(2)
    
    # Navigate to cart
    page.locator('header a[href="/view_cart"]').click()
    page.wait_for_load_state('networkidle')
    
    # Check if items exist
    quantities = page.locator('#cart_info_table .cart_quantity button')
    print(f'Quantities count: {quantities.count()}')
    
    if quantities.count() > 0:
        print(f'First quantity text: {quantities.first.inner_text()}')
    else:
        print('No items in cart')
        # Try to see if there's an empty message
        content = page.content()
        if 'empty' in content.lower():
            print('Cart appears to be empty')
        
        # Print the page HTML to debug
        print('\n--- Page HTML (first 2000 chars) ---')
        print(page.content()[:2000])
    
    browser.close()
