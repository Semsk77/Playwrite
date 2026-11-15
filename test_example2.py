# ФИО: Булатов Михаил Антонович
# Дата: 2026-15-11
# Время: 23:28
# Описание: Код содержит два UI-теста на Playwright для сайта playwright.dev. 
# Первый тест проверяет наличие слова "Playwright" в заголовке страницы, второй кликает по ссылке "Get started" и убеждается, что открылась страница с заголовком "Installation". 
# URL вынесен в константу, добавлена дополнительная проверка корректности перехода по ссылке.
# Что изменилось: 
# Вынесен базовый URL в константу BASE_URL
# Добавлена проверка URL после клика 
# Добавлены docstring'и

import re
from playwright.sync_api import Page, expect

BASE_URL = "https://playwright.dev/"


def test_has_title(page: Page):
    """Проверяет, что заголовок страницы содержит подстроку 'Playwright'."""
    page.goto(BASE_URL)
    expect(page).to_have_title(re.compile("Playwright"))


def test_get_started_link(page: Page):
    """Клик по ссылке 'Get started' и проверка перехода на страницу установки."""
    page.goto(BASE_URL)
    page.get_by_role("link", name="Get started").click()
    expect(page).to_have_url(re.compile(r".*/docs/intro"))
    expect(page.get_by_role("heading", name="Installation")).to_be_visible()