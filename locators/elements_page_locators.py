from selenium.webdriver.common.by import By


class TextBoxPageLocators:
    # form fields
    FULL_NAME = (By.CSS_SELECTOR, "input[id='userName']")
    EMAIL = (By.CSS_SELECTOR, "input[id='userEmail']")
    CURRENT_ADDRESS = (By.CSS_SELECTOR, "textarea[id='currentAddress']")
    PERMANENT_ADDRESS = (By.CSS_SELECTOR, "textarea[id='permanentAddress']")
    SUBMIT = (By.CSS_SELECTOR, "button[id='submit']")

    # created from
    CREATED_FULL_NAME = (By.CSS_SELECTOR, "#output #name")
    CREATED_EMAIL = (By.CSS_SELECTOR, "#output #email")
    CREATED_CURRENT_ADDRESS = (By.CSS_SELECTOR, "#output #currentAddress")
    CREATED_PERMANENT_ADDRESS = (By.CSS_SELECTOR, "#output #permanentAddress")


class CheckBoxPageLocators:
    EXPAND_BUTTON = (By.CSS_SELECTOR, "button[class='rct-option rct-option-expand-all']")
    ITEM_LIST = (By.CSS_SELECTOR, "span[class='rct-title']")
    CHECKED_ITEMS = (By.CSS_SELECTOR, "svg[class='rct-icon rct-icon-check']")
    TITLE_ITEM = (By.XPATH, ".//ancestor::span[@class='rct-text']")
    OUTPUT_RESULT = (By.CSS_SELECTOR, "span[class='text-success']")


class RadioButtonPageLocators:
    YES_RADIO_BUTTON = (By.CSS_SELECTOR, "label[for='yesRadio']")
    IMPRESSIVE_RADIO_BUTTON = (By.CSS_SELECTOR, "label[for='impressiveRadio']")
    NO_RADIO_BUTTON = (By.CSS_SELECTOR, "label[for='noRadio']")
    TEXT_SUCCESS = (By.CSS_SELECTOR, "span[class='text-success']")


class WebTablePageLocators:
    ADD_BUTTON = (By.CSS_SELECTOR, "button[id='addNewRecordButton']")
    FORM_FIRST_NAME = (By.CSS_SELECTOR, "input[id='firstName']")
    FORM_LAST_NAME = (By.CSS_SELECTOR, "input[id='lastName']")
    FORM_EMAIL = (By.CSS_SELECTOR, "input[id='userEmail']")
    FORM_AGE = (By.CSS_SELECTOR, "input[id='age']")
    FORM_SALARY = (By.CSS_SELECTOR, "input[id='salary']")
    FORM_DEPARTMENT = (By.CSS_SELECTOR, "input[id='department']")
    FORM_SUBMIT_BUTTON = (By.CSS_SELECTOR, "button[id='submit']")

    TABLE_NEW_ROW_ELEMENTS = (By.CSS_SELECTOR, ".rt-tr-group:nth-child(4) > div > div")
    TABLE_ALL_ELEMENTS = (By.CSS_SELECTOR, "div[class='rt-tr-group']")
    SEARCH_INPUT = (By.CSS_SELECTOR, 'input[id="searchBox"]')

    DELETE_BUTTON = (By.CSS_SELECTOR, 'span[title="Delete"]')
    ROW_PARENT = (By.XPATH, ".//ancestor::div[@class='rt-tr-group']")
