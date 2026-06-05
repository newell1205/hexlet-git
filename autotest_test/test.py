import os
import pytest
from playwright.sync_api import Page


# Исправленный тест - page теперь берётся из conftest.py
def test_add_todo(page: Page) -> None:
    page.goto("https://demo.playwright.dev/todomvc/#/")
    page.get_by_placeholder("What needs to be done?").click()
    page.get_by_placeholder("What needs to be done?").fill("Создать первый сценарий playwright")
    page.get_by_placeholder("What needs to be done?").press("Enter")


def test_loc(page: Page):
    page.goto('https://zimaev.github.io/text_input/')
    page.get_by_label("Email address").fill("qa@example.com")
    page.get_by_title("username").fill("Anton")
    page.get_by_placeholder('password').fill("secret")
    page.get_by_role('checkbox').click()
    page.wait_for_timeout(2000)  # Пауза для визуальной проверки


def test_or(page: Page):
    page.goto("https://zimaev.github.io/")
    selector = page.locator("input").or_(page.locator("text"))
    selector.first.fill("Hello Stepik")


def test_locator_and(page: Page):
    page.goto("https://zimaev.github.io/locatorand/")
    selector = page.get_by_role("button", name="Sing up").and_(page.get_by_title("Sing up today"))
    selector.click()


def test_loc_all(page: Page):
    page.goto('https://zimaev.github.io/checks-radios/')
    checkboxes = page.locator("input")
    for checkbox in checkboxes.all():
        checkbox.check()


def test_login(page: Page):
    page.goto('https://exaltedplushadware.antonzimaiev.repl.co/?')
    page.locator("#exampleInputEmail1").fill("admin@example.com")


def test_login_1(page: Page):
    page.goto('https://exaltedplushadware.antonzimaiev.repl.co/?')
    page.locator("#exampleInputEmail1").type("admin@example.com")


def test_checkbox(page: Page):
    page.goto('https://zimaev.github.io/checks-radios/')
    page.locator("text=Default checkbox").click()
    page.wait_for_timeout(500)
    page.locator("text=Checked checkbox").click()
    page.wait_for_timeout(500)
    page.locator("text=Default radio").click()
    page.wait_for_timeout(500)
    page.locator("text=Default checked radio").click()
    page.wait_for_timeout(500)
    page.locator("text=Checked switch checkbox input").click()
    page.wait_for_timeout(500)


def test_select(page: Page):
    page.goto('https://zimaev.github.io/select/')
    page.select_option('#floatingSelect', value="3")
    page.select_option('#floatingSelect', index=1)
    page.select_option('#floatingSelect', label="Нашел и завел bug")


def test_select_multiple(page: Page):
    page.goto('https://zimaev.github.io/select/')
    page.select_option('#skills', value=["playwright", "python"])


def test_drag_and_drop(page: Page):
    page.goto('https://zimaev.github.io/draganddrop/')
    page.drag_and_drop("#drag", "#drop")
    page.wait_for_timeout(1000)


def test_dialogs(page: Page):
    page.goto("https://zimaev.github.io/dialog/")
    # Заранее подписываемся на диалог ДО клика
    page.once("dialog", lambda dialog: dialog.accept())
    page.get_by_text("Диалог Confirmation").click()
    # Ждём, пока диалог обработается
    page.wait_for_timeout(1000)


def test_select_multiple_1(page: Page):
    page.goto('https://zimaev.github.io/upload/')
    page.set_input_files("#formFile", "hello.txt")
    page.locator("#file-submit").click()


def test_download(page: Page):
    page.goto("https://demoqa.com/upload-download")

    with page.expect_download() as download_info:
        page.locator("a:has-text(\"Download\")").click()

    download = download_info.value
    file_name = download.suggested_filename
    destination_folder_path = "./data/"
    download.save_as(os.path.join(destination_folder_path, file_name))


def test_new_tab(page: Page):
    page.goto("https://zimaev.github.io/tabs/")
    with page.context.expect_page() as tab:
        page.get_by_text("Переход к Dashboard").click()

    new_tab = tab.value
    assert new_tab.url == "https://zimaev.github.io/tabs/dashboard/index.html?"
    sign_out = new_tab.locator('.nav-link', has_text='Sign out')
    assert sign_out.is_visible()
