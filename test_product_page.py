from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
import pytest

#@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
 #                                 "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
  #                                "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
   #                               "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
    #                              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
     #                             "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
      #                            "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
       #                           pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
        #                          "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
         #                         "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])

def test_guest_should_see_login_link_on_product_page(browser):

    link="http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
    page=ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page(browser):

    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    loginpage=LoginPage(browser, browser.current_url)
    loginpage.should_be_login_page()

def test_guest_can_add_product_to_basket(browser):
    #old link
    #link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209/?promo=newYear"

    link="http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"

    page=ProductPage(browser, link)
    page.open()
    page.should_not_be_success_notification()
    page.should_be_add_basket_button()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_notification_about_successful_add_to_basket()
    page.should_be_notification_about_total_sum_basket()

@pytest.mark.skip #  тест заведомо неверный, при прохождении упадет
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):

    link="http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"

    page=ProductPage(browser, link)
    page.open()
    page.should_be_add_basket_button()
    page.add_to_basket()
    page.should_not_be_success_notification()

@pytest.mark.skip  # тест для наглядности, проходит
def test_guest_cant_see_success_message(browser):  #
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
    page=ProductPage(browser, link)
    page.open()
    page.should_not_be_success_notification()

@pytest.mark.skip  # тест заведомо неверный, при прохождении упадет
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
    page=ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.should_be_disappeared()