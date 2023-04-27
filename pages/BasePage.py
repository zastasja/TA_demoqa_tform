from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Basepage:
    def __init__(self, browser, link):
        self.browser = browser
        self.link = link

    def open_page(self):
        self.browser.get(self.link)

    def keyboard_input(self, method, locator, keys_text):
        WebDriverWait(self.browser, 30).until(
            EC.element_to_be_clickable((method, locator))
        ).send_keys(keys_text)

    def get_element_text(self, method, locator):
        el = self.browser.find_element(method, locator)
        word = el.text
        return word
