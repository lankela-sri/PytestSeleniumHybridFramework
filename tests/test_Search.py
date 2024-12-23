import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from pages.HomePage import HomePage
from pages.SearchPage import SearchPage
from tests.BaseTest import BaseTest


class TestSearch(BaseTest):
    def test_search_for_valid_product(self):
        home_page = HomePage(self.driver)
        home_page.enter_product_into_search_box_field("HP")
        search_page= home_page.click_on_search_button()
        assert search_page.display_status_of_valid_product()

    def test_search_for_invalid_product(self):
        home_page = HomePage(self.driver)
        home_page.enter_product_into_search_box_field("Honda")
        search_page= home_page.click_on_search_button()
        expected_text = "There is no product that matches the search criteria."

        assert search_page.retrieve_no_product_message().__contains__(expected_text)

    def test_search_without_entering_any_product(self):
        home_page = HomePage(self.driver)
        home_page.enter_product_into_search_box_field("")
        search_page= home_page.click_on_search_button()
        expected_text = "There is no product that matches the search criteria.AB"
        assert search_page.retrieve_no_product_message().__contains__(expected_text)


