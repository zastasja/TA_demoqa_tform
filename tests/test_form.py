import time

from pages.BasePage import Basepage
from utils.locators import Locators
from utils.t_random_data import Random_data

base_url = 'https://demoqa.com/text-box'
def test_form(browser):
    page = Basepage(browser, base_url)
    page.open_page()
    page.keyboard_input(*Locators.FULL_NAME, Random_data.full_name)
    page.keyboard_input(*Locators.EMAIL, Random_data.email)
    page.keyboard_input(*Locators.CURRENT_ADDRESS, Random_data.r_address)
    page.keyboard_input(*Locators.PERMANENT_ADDRESS, Random_data.r_address)
    page.click_element(*Locators.SUBMIT_BTN)
    res = page.pick_element(*Locators.R_NAME)
    print(res.text)
    time.sleep(10)