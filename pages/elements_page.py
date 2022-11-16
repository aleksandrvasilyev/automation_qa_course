import random

from generator.generator import generated_person
from locators.elements_page_locators import TextBoxPageLocators, CheckBoxPageLocators, RadioButtonPageLocators, \
    WebTablePageLocators
from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class TextBoxPage(BasePage):
    locators = TextBoxPageLocators()

    def fill_all_fields(self):
        person_info = next(generated_person())
        full_name = person_info.full_name
        email = person_info.email
        current_address = person_info.current_address
        permanent_address = person_info.permanent_address
        self.element_is_visible(self.locators.FULL_NAME).send_keys(full_name)
        self.element_is_visible(self.locators.EMAIL).send_keys(email)
        self.element_is_visible(self.locators.CURRENT_ADDRESS).send_keys(current_address)
        self.element_is_visible(self.locators.PERMANENT_ADDRESS).send_keys(permanent_address)
        self.go_to_element(self.element_is_visible(self.locators.SUBMIT))
        self.element_is_visible(self.locators.SUBMIT).click()
        return full_name, email, current_address, permanent_address

    def check_filled_form(self):
        full_name = self.element_is_present(self.locators.CREATED_FULL_NAME).text.split(':')[1]
        email = self.element_is_present(self.locators.CREATED_EMAIL).text.split(':')[1]
        current_address = self.element_is_present(self.locators.CREATED_CURRENT_ADDRESS).text.split(':')[1]
        permanent_address = self.element_is_present(self.locators.CREATED_PERMANENT_ADDRESS).text.split(':')[1]
        return full_name, email, current_address, permanent_address


class CheckBoxPage(BasePage):
    locators = CheckBoxPageLocators()

    def expand_all(self):
        self.element_is_visible(self.locators.EXPAND_BUTTON).click()

    def click_random_checkbox(self):
        item_list = self.elements_are_visible(self.locators.ITEM_LIST)
        count = len(item_list)
        while count != 0:
            item = item_list[random.randint(1, 15)]
            if count > 0:
                self.go_to_element(item)
                item.click()
                count -= 1
            else:
                break

    def get_checked_checkboxes(self):
        checked_list = self.elements_are_present(self.locators.CHECKED_ITEMS)
        data = []
        for box in checked_list:
            title_item = box.find_element(*self.locators.TITLE_ITEM)
            data.append(title_item.text.lower().replace('.doc', '').replace(' ', ''))
        return data

    def get_output_result(self):
        result_list = self.elements_are_present(self.locators.OUTPUT_RESULT)
        data = []
        for item in result_list:
            data.append(item.text.lower())
        return data


class RadioButtonPage(BasePage):
    locators = RadioButtonPageLocators()

    def click_radio_page(self, choice):
        button = {'yes': self.locators.YES_RADIO_BUTTON,
                  'impressive': self.locators.IMPRESSIVE_RADIO_BUTTON,
                  'no': self.locators.NO_RADIO_BUTTON}
        self.element_is_visible(button[choice]).click()

    def get_output(self):
        return self.element_is_visible(self.locators.TEXT_SUCCESS).text


class WebTablePage(BasePage):
    locators = WebTablePageLocators()

    def click_to_add_button(self):
        self.element_is_visible(self.locators.ADD_BUTTON).click()

    def add_new_person(self):
        count = 1
        while count != 0:
            person_info = next(generated_person())
            print(person_info)
            firstname = person_info.first_name
            lastname = person_info.last_name
            email = person_info.email
            age = person_info.age
            salary = person_info.salary
            department = person_info.department
            self.element_is_visible(self.locators.FORM_FIRST_NAME).send_keys(firstname)
            self.element_is_visible(self.locators.FORM_LAST_NAME).send_keys(lastname)
            self.element_is_visible(self.locators.FORM_EMAIL).send_keys(email)
            self.element_is_visible(self.locators.FORM_AGE).send_keys(age)
            self.element_is_visible(self.locators.FORM_SALARY).send_keys(salary)
            self.element_is_visible(self.locators.FORM_DEPARTMENT).send_keys(department)
            self.element_is_visible(self.locators.FORM_SUBMIT_BUTTON).click()
            return [firstname, lastname, str(age), email, str(salary), department]

    def check_new_added_person(self):
        elements = self.elements_are_present(self.locators.TABLE_ALL_ELEMENTS)
        all_elements = []
        for element in elements:
            all_elements.append(element.text.splitlines())
        return all_elements

    def search(self, key):
        search_field = self.element_is_present(self.locators.SEARCH_INPUT)
        search_field.send_keys(key)
        return key

    def check_search_person(self):
        delete_button = self.element_is_present(self.locators.DELETE_BUTTON)
        row = delete_button.find_element(*self.locators.ROW_PARENT)
        return row.text.splitlines()
