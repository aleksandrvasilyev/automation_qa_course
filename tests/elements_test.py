from random import random, randint

from pages.base_page import BasePage
import time
import pytest
from pages.elements_page import TextBoxPage, CheckBoxPage, RadioButtonPage, WebTablePage


class TestElements:
    class TestTextBox:

        def test_text_box(self, driver):
            text_box_page = TextBoxPage(driver, 'https://demoqa.com/text-box')
            text_box_page.open()
            full_name, email, current_address, permanent_address = text_box_page.fill_all_fields()
            output_full_name, output_email, output_current_address, output_permanent_address = text_box_page.check_filled_form()
            assert full_name == output_full_name
            assert email == output_email
            assert current_address == output_current_address
            assert permanent_address == output_permanent_address

    class TestCheckBox:

        def test_check_box(self, driver):
            check_box_page = CheckBoxPage(driver, 'https://demoqa.com/checkbox')
            check_box_page.open()
            check_box_page.expand_all()
            check_box_page.click_random_checkbox()
            input_checkbox = check_box_page.get_checked_checkboxes()
            output_result = check_box_page.get_output_result()
            assert input_checkbox == output_result

    class TestRadioButton:

        def test_radio_button(self, driver):
            radio_button_page = RadioButtonPage(driver, 'https://demoqa.com/radio-button')
            radio_button_page.open()
            radio_button_page.click_radio_page('yes')
            result_yes = radio_button_page.get_output()
            radio_button_page.click_radio_page('impressive')
            result_impressive = radio_button_page.get_output()
            radio_button_page.click_radio_page('no')
            result_no = radio_button_page.get_output()
            assert result_yes == 'Yes'
            assert result_impressive == 'Impressive'
            assert result_no == 'No'

    class TestWebTables:

        def test_add_user_to_table(self, driver):
            add_user_to_table = WebTablePage(driver, 'https://demoqa.com/webtables')
            add_user_to_table.open()
            add_user_to_table.click_to_add_button()
            new_person = add_user_to_table.add_new_person()
            table = add_user_to_table.check_new_added_person()
            assert new_person in table

        def test_search_user_in_table(self, driver):
            search_user_in_table = WebTablePage(driver, 'https://demoqa.com/webtables')
            search_user_in_table.open()
            search_user_in_table.click_to_add_button()
            key_word = search_user_in_table.add_new_person()[randint(0, 5)]
            search_user_in_table.search(key_word)
            table_result = search_user_in_table.check_search_person()
            assert key_word in table_result

