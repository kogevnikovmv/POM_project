import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser): # получение парметров из командной строки
    parser.addoption('--browser_name', action='store', default='chrome',
                     help="Выберете браузер: chrome, yandex or firefox")
    parser.addoption('--language', action='store', default="en",
                     help="Choose language, my friend")

@pytest.fixture(scope="function")
def browser(request):

    # получаем параметр language из коммандной строки
    user_language = request.config.getoption("language")

    #выбираем браузер
    browser_name = request.config.getoption("browser_name")
    browser=None
    if browser_name=="chrome":
        print("start Chrome browser...")
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        browser=webdriver.Chrome(options=options)
    elif browser_name=="yandex":
        print("start Yandex browser...")
        options = webdriver.ChromeOptions()
        options.add_argument(f"--lang={user_language}")
        binary_yandex_driver_file = 'yandexdriver.exe'
        browser = webdriver.Chrome(binary_yandex_driver_file, options=options)
    elif browser_name==("firefox"):
        print("start Firefox browser...")
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", user_language)
        browser = webdriver.Firefox(firefox_profile=fp)
    else:
        raise pytest.UsageError("--browser_name должно быть chrome|yandex|firefox")


    yield browser
    print("close browser")
    browser.quit()