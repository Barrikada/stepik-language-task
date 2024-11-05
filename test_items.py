import pytest
from selenium.webdriver.common.by import By


def test_add_to_cart_button_present(browser):
    # Открываем страницу товара
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)

    # Проверяем наличие кнопки добавления в корзину
    add_to_cart_button = browser.find_elements(By.CSS_SELECTOR, ".btn-add-to-basket")
    assert add_to_cart_button, "Кнопка добавления в корзину не найдена на странице"