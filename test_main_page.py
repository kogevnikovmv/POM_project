from selenium.webdriver.common.by import By
from .pages.main_page import MainPage
from .pages.basket_page import BasketPage
from .pages.product_page import ProductPage

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
