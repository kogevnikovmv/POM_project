from selenium.webdriver.common.by import By
from .pages.main_page import MainPage
from .pages.basket_page import BasketPage
from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
import pytest

@pytest.mark.login_guest
class TestGuestLoginFromMainPage():

    # Пример подготовки данных для каждого теста
    #@pytest.fixture(scope="function", autouse=True)
    #def setup(self):
        #self.product = ProductFactory(title="Best book created by robot")
        # создаем по апи
        #self.link = self.product.link
        #yield
        # после этого ключевого слова начинается teardown
        # выполнится после каждого теста в классе
        # удаляем те данные, которые мы создали
        #self.product.delete()

    def test_guest_should_see_login_link(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page=MainPage(browser, link)
        page.open()
        page.should_be_login_link()

    def test_guest_can_go_to_login_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page=MainPage(browser, link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()

def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"

    mainpage=MainPage(browser, link)
    mainpage.open()
    mainpage.go_to_basket_page()
    basketpage=BasketPage(browser, browser.current_url)
    basketpage.should_be_basket_page()
    basketpage.should_not_be_items_in_basket()
    basketpage.should_be_message_about_empty_basket()

def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"

    productpage=ProductPage(browser, link)
    productpage.open()
    productpage.go_to_basket_page()
    basketpage = BasketPage(browser, browser.current_url)
    basketpage.should_be_basket_page()
    basketpage.should_not_be_items_in_basket()
    basketpage.should_be_message_about_empty_basket()
