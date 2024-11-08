from playwright.sync_api import sync_playwright
import time

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        
        # Navigate to the profile page
        page.goto("https://x.com/bouchernicolas")
        
        # Hover over the follower count element
        follower_selector = 'a[href="/BoucherNicolas/verified_followers"]'
        page.wait_for_selector(follower_selector)
        page.hover(follower_selector)
        
        # Pause briefly to allow the tooltip to appear
        time.sleep(2)

        # Now locate the tooltip that appears after hovering
        detailed_count_selector = '[data-testid="HoverLabel"]'
        detailed_count = page.locator(detailed_count_selector).text_content()

        print("Detailed follower count:", detailed_count.strip())
        
        browser.close()

# Run the function
run()
