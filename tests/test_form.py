from selenium.webdriver import ActionChains, Keys
from pages.BasePage import Basepage
from utils.locators import Locators
from utils.t_random_data import Random_data

base_url = "https://demoqa.com/text-box"


def test_form(browser):
    page = Basepage(browser, base_url)
    page.open_page()
    page.keyboard_input(*Locators.FULL_NAME, Random_data.full_name)
    page.keyboard_input(*Locators.EMAIL, Random_data.email)
    page.keyboard_input(*Locators.CURRENT_ADDRESS, Random_data.r_address)
    page.keyboard_input(*Locators.PERMANENT_ADDRESS, Random_data.r_address)
    actions = ActionChains(browser)
    actions.send_keys(Keys.TAB)
    actions.send_keys(Keys.RETURN)
    actions.perform()

    # SENT RESULTS:

    rname = page.get_element_text(*Locators.R_NAME)
    name = rname.replace("Name:", "")
    rmail = page.get_element_text(*Locators.R_EMAIL)
    mail = rmail.replace("Email:", "")
    rc_address = page.get_element_text(*Locators.R_C_ADDRESS)
    address = rc_address.replace("Current Address :", "")
    rp_address = page.get_element_text(*Locators.R_P_ADDRESS)
    p_address = rp_address.replace("Permananet Address :", "")

    assert Random_data.full_name == name
    assert Random_data.email == mail
    assert Random_data.r_address == address
    assert Random_data.r_address == p_address
