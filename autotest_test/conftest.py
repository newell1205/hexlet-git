from playwright.sync_api import sync_playwright
import pytest


@pytest.fixture
def page():
    """Фикстура, создающая страницу браузера через Playwright"""
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        yield page
        context.close()
        browser.close()
