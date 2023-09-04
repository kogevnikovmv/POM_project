from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):

    def should_be_basket_page(self): # ОШИБКА ТУТ
        ab=(self.should_be_basket_url(), self.should_be_basket_header_text())
        assert all(ab)==True, 'It is not basket page!!'


    def should_be_basket_url(self):
        assert "basket" in self.browser.current_url, "wrong basket url"
        return True

    def should_be_basket_header_text(self):
        assert "Basket" in self.browser.find_element(*BasketPageLocators.BASKET_HEADER_TEXT).text, "another header text"
        return True


