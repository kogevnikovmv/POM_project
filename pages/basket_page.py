from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):

    # Функция проверяет, что это страница корзины
    # Обединяет результаты should_be_basket_url() и should_be_basket_header_text(),
    # если хотя бы одна из функций вернет False, то проверка провалена.
    def should_be_basket_page(self):
        ab=(self.should_be_basket_url(), self.should_be_basket_header_text())
        assert all(ab)==True, 'It is not basket page!!'


    def should_be_basket_url(self): # проверяет что в текущем url есть basket для подтверждения что это страница корзины
        assert "basket" in self.browser.current_url, "wrong basket url"
        return True

    def should_be_basket_header_text(self): # проверяет что заголовок(?) страницы basket
        assert "Basket" in self.browser.find_element(*BasketPageLocators.BASKET_HEADER_TEXT).text, "another header text"
        return True

    def should_be_message_about_empty_basket(self):
        assert "Your basket is empty" in self.browser.find_element(*BasketPageLocators.MES_EMPTY_BASKET).text, \
            "Message about empty basket not found"

    def should_not_be_items_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ADDED_ITEMS), "Basket is not empty!"
