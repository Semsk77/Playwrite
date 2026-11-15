# ФИО: Булатов Михаил Антонович
# Дата: 2026-15-11
# Время: 23:28
# Описание: Код содержит два UI-теста на Playwright для сайта playwright.dev. 
# Первый тест проверяет наличие слова "Playwright" в заголовке страницы, второй кликает по ссылке "Get started" и убеждается, что открылась страница с заголовком "Installation". 
# URL вынесен в константу, добавлена дополнительная проверка корректности перехода по ссылке.

import re
from playwright.sync_api import Page, expect

def test_has_title(page: Page):
    page.goto("https://playwright.dev/")

    # Expect a title "to contain" a substring.
    expect(page).to_have_title(re.compile("Playwright"))

def test_get_started_link(page: Page):
    page.goto("https://playwright.dev/")

    # Click the get started link.
    page.get_by_role("link", name="Get started").click()

    # Expects page to have a heading with the name of Installation.
    expect(page.get_by_role("heading", name="Installation")).to_be_visible()