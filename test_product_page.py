from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
import pytest
import time # для генерации имени email"а в setup'е класса TestUserAddToBasketFromProductPage()

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

# Если нужно запустить тесты с параметризацией, то нужно удалить link="..." из тестов,
# добавить в каждой функции аргумент link, который она будет принимать вместе с browser

@pytest.mark.user_add_to_basket
class TestUserAddToBasketFromProductPage():

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        email=str(time.time())+"@fakemail.com"
        password="asdfghjim"
        login_link="http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
        page=LoginPage(browser, login_link)
        page.open()
        page.register_new_user(email, password)
        page.should_be_authorized_user()
        print("User creat.")



    def test_user_cant_see_success_message(self, browser):  #
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"

        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_notification()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"

        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_notification()
        page.should_be_add_basket_button()
        page.add_to_basket()
        page.should_be_notification_about_successful_add_to_basket()
        page.should_be_notification_about_total_sum_basket()

@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"

    productpage=ProductPage(browser, link)
    productpage.open()
    productpage.go_to_basket_page()
    basketpage = BasketPage(browser, browser.current_url)
    basketpage.should_be_basket_page()
    basketpage.should_not_be_items_in_basket()
    basketpage.should_be_message_about_empty_basket()

def test_guest_should_see_login_link_on_product_page(browser):

    link="http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    page=ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):

    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    loginpage=LoginPage(browser, browser.current_url)
    loginpage.should_be_login_page()

@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser):
    link="http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"

    page=ProductPage(browser, link)
    page.open()
    page.should_not_be_success_notification()
    page.should_be_add_basket_button()
    page.add_to_basket()
    #page.solve_quiz_and_get_code() эта функция нужна для задания с параметризацией
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
def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    page=ProductPage(browser, link)
    page.open()
    page.should_not_be_success_notification()

@pytest.mark.skip  # тест заведомо неверный, при прохождении упадет
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    page=ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.should_be_disappeared()