from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import math
from .locators import BasePageLocators

class BasePage():

    def __init__(self, browser, url, timeout=10):
        self.browser=browser
        self.url=url
        self.browser.implicitly_wait(timeout)

    def go_to_basket_page(self):
        basket_link=self.browser.find_element(*BasePageLocators.BASKET_LINK)
        basket_link.click()



    def go_to_login_page(self):
        login_link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        login_link.click()

    def should_be_authorized_user(self):
        assert self.is_element_present(*BasePageLocators.USER_ICON), "User icon is not presented," \
                                                                     " probably unauthorised user"

    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link not found"

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how, what):    # проверка наличия элемента
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def is_not_element_present(self, how, what, timeout=4):   # проверка отсутствия элемента
        try:                                                  # ожидание появления элемента 4сек
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:  # если элемент не появляется, перехватывается ошибка и возвращается true
            return True

        return False  # если элемент появился в течении 4сек, возвращается False

    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException).until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True

# это функция требуется если на конце ссылки есть ?promo=offer0, т.к. после добавления товара в корзину
# нужно будет написать ответ в всплывающем окне. Собственно эта функция высчитывает правильный ответ
# и вставляет его в всплывающее окно.
    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")