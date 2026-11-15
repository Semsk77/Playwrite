# ФИО: Булатов Михаил Антонович
# Дата: 2026-11-10
# Время: 15:30
# Описание: Этот код запускает браузер Chromium, открывает страницу
# playwright.dev и проверяет, что заголовок страницы содержит слово "Playwright".
# Что изменено: Вынесен базовый URL в константу и добавлена autouse-фикстура для автоматической навигации, что устранило дублирование кода.
# В тест перехода по ссылке добавлена проверка URL после клика и документация к функциям.

import re
import pytest
from playwright.sync_api import Page, expect

BASE_URL = "https://playwright.dev/"


@pytest.fixture(autouse=True)
def navigate_to_home(page: Page):
    """Фикстура: автоматическая навигация на главную страницу перед каждым тестом."""
    page.goto(BASE_URL)
    yield page


def test_has_title(page: Page):
    """Проверяет, что заголовок страницы содержит подстроку 'Playwright'."""
    expect(page).to_have_title(re.compile("Playwright"))


def test_get_started_link(page: Page):
    """Клик по ссылке 'Get started' и проверка перехода на страницу установки."""
    page.get_by_role("link", name="Get started").click()

    # Проверка, что URL изменился после клика
    expect(page).to_have_url(re.compile(r".*/docs/intro"))

    # Проверка видимости заголовка раздела установки
    expect(page.get_by_role("heading", name="Installation")).to_be_visible()