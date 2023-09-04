from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK=(By.CSS_SELECTOR, "#login_link")
    BASKET_LINK=(By.XPATH, '//a[contains(text(), "basket")]')

class BasketPageLocators():
    MES_EMPTY_BASKET=(By.CSS_SELECTOR, '#content_inner p')
    BASKET_HEADER_TEXT=(By.CSS_SELECTOR, '.page-header.action h1')

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    ADD_BASKET_BUTTON=(By.CSS_SELECTOR, ".btn.btn-add-to-basket")
    MES_SUCCESS_ADD_TO_BASKET=(By.XPATH, '//div[@id="messages"]/div[1]//strong')
    MES_SUM_BASKET=(By.XPATH, '//div[@id="messages"]/div[3]//strong')
    BOOK_PRICE=(By.CSS_SELECTOR, '[class="price_color"]')
    BOOK_NAME=(By.CSS_SELECTOR, ".col-sm-6 h1") 