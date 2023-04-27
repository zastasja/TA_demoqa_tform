from selenium.webdriver.common.by import By


class Locators:
    # LOCATORS OF THE FORM
    FULL_NAME = (By.XPATH, "//input[@id='userName']")
    EMAIL = (By.XPATH, "//input[@id='userEmail']")
    CURRENT_ADDRESS = (By.XPATH, "//textarea[@id='currentAddress']")
    PERMANENT_ADDRESS = (By.XPATH, "//textarea[@id='permanentAddress']")

    # RESULST OF INPUT
    R_NAME = (By.XPATH, "//*[@id='name']")
    R_EMAIL = (By.XPATH, "//p[@id='email']")
    R_C_ADDRESS = (By.XPATH, "//p[@id='currentAddress']")
    R_P_ADDRESS = (By.XPATH, "//p[@id='permanentAddress']")
