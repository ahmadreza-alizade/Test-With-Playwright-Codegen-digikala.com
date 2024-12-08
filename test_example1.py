import re, time
from playwright.sync_api import Playwright, sync_playwright, expect
# import os

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=True, slow_mo=1000)
    context = browser.new_context(
        record_video_dir="videos/",
        record_video_size={"width": 640, "height": 480},

    )
    page = context.new_page()
    page.goto("https://www.digikala.com/users/login/?backUrl=/")
    page.get_by_label("").click()
    page.get_by_label("").fill("0912********")
    page.get_by_role("button", name="ورود").click()
    time.sleep(8)
    page.locator(".w-full > div > div:nth-child(3) > svg > use").click()

    page.get_by_role("link", name="پرفروش‌ترین‌ها").click()

    with page.expect_popup() as page_info:
        page.locator("a").filter(has_text="۲ارسال رایگانگوشی موبایل نوکیا مدل 105 2023").click()
    page1 = page_info.value
    page1.get_by_test_id("buy-box").get_by_test_id("add-to-cart").click()


    page1.evaluate("window.scrollTo(0, 0)")
    page1.get_by_role("link", name="پرفروش‌ترین‌ها").click()
    with page1.expect_popup() as page2_info:
        page1.locator("a").filter(has_text="۱ارسال رایگانگوشی موبایل آلکاتل مدل 1069").click()
    page2 = page2_info.value
    page2.get_by_test_id("buy-box").get_by_test_id("add-to-cart").click()
    page2.get_by_role("link", name="۲", exact=True).click()
    # time.sleep(10)
    page2.evaluate("window.scrollTo(0, 150)")
    page2.get_by_test_id("quantity-decrease").nth(2).click()
    page2.get_by_test_id("quantity-decrease").nth(3).click()
    time.sleep(8)

    page.wait_for_timeout(10000)

    time.sleep(60)
    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)


