from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.common.by import By

class ProductPage(BasePage):

    def should_be_add_basket_button(self):
        self.is_element_present(*ProductPageLocators.ADD_BASKET_BUTTON)

    def should_be_notification_about_successful_add_to_basket(self):
        book=self.browser.find_element(*ProductPageLocators.BOOK_NAME).text
        message_book=self.browser.find_element(*ProductPageLocators.MES_SUCCESS_ADD_TO_BASKET).text
        assert book==message_book, "Another book added"

    def should_be_notification_about_total_sum_basket(self):
        book_price=self.browser.find_element(*ProductPageLocators.BOOK_PRICE).text[1:]
        total_coast=self.browser.find_element(*ProductPageLocators.MES_SUM_BASKET).text[1:]
        assert book_price==total_coast, "In notification message another price"

    def add_to_basket(self):
        basket_button=self.browser.find_element(*ProductPageLocators.ADD_BASKET_BUTTON)
        basket_button.click()




