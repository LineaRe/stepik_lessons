import pytest
from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.main_page import MainPage

link = "http://selenium1py.pythonanywhere.com/"


class TestMainPage:
    def test_guest_can_go_to_login_page(self, browser):
        page = MainPage(browser,
                        link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page.open()  # открываем страницу
        page.go_to_login_page()  # выполняем метод страницы - переходим на страницу логина

    def test_guest_should_see_login_link(self, browser):
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()

    def test_guest_can_find_all_items(self, browser):
        page = MainPage(browser, link)
        page.open()
        page.find_items()

    def test_change_language_to_russian(self, browser):
        page = MainPage(browser, link)
        page.open()
        page.change_language()

    def test_guest_can_create_account(self, browser):
        page = MainPage(browser, link)
        page.open()
        page.go_to_login_page()



