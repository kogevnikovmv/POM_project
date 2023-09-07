from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):

    def register_new_user(self, email, password):
        email_form=self.browser.find_element(*LoginPageLocators.EMAIL_TEXT_FORM)
        password_form=self.browser.find_element(*LoginPageLocators.PASSWORD_TEXT_FORM)
        password_confirm_form=self.browser.find_element(*LoginPageLocators.PASSWORD_CONFIRM_TEXT_FORM)
        regbutton=self.browser.find_element(*LoginPageLocators.REG_BUTTON)
        email_form.send_keys(email)
        password_form.send_keys(password)
        password_confirm_form.send_keys(password)
        regbutton.click()

    def should_be_login_page(self):
        a=self.should_be_login_url()
        b=self.should_be_login_form()
        c=self.should_be_register_form()
        abc=(a, b, c)
        assert all(abc)==True, "It's not login page"


    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "wrong login url"
        return "login" in self.browser.current_url


    def should_be_login_form(self):
        b=self.is_element_present(*LoginPageLocators.LOGIN_FORM)
        assert b==True, "Login form not found"
        return b

    def should_be_register_form(self):
        c=self.is_element_present(*LoginPageLocators.REGISTER_FORM)
        assert c==True, "Register form not found"
        return c