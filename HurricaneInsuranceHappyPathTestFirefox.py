import unittest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json


class HurricaneInsuranceTestCase(unittest.TestCase):

    def setUp(self):
        """Explicitly create a Chrome browser instance."""
        fService = webdriver.FirefoxService(executable_path='./geckodriver')
        self.browser = webdriver.Firefox(service = fService)
        self.addCleanup(self.browser.quit)

        self.f = open('strings.json')
        self.strings = json.load(self.f)

        self.landing_page_url = self.strings["landing_page_url"]
        self.building_materials_page_url = self.strings["building_material_page_url"]
        self.water_proximity_page_url = self.strings["water_proximity_page_url"]
        self.quote_page_url = self.strings["quote_page_url"]
        
        self.quote_page_checkbox_locator = self.strings["quote_page_checkbox_locator"]
        self.building_material_straw_radio_button_locator = self.strings["building_material_straw_radio_button_locator"]
        self.next_button_locator = self.strings["next_button_locator"]
        self.water_proximity_yes_radio_button_locator = self.strings["water_proximity_yes_radio_button_locator"]


    def tearDown(self):
        self.f.close()

    def test_landing_page_zip_code_entry(self):
        """Assert that landing page and zip code entry works"""
        self.browser.get(self.landing_page_url)
        self.assertEqual('Hurricane Insurance', self.browser.title, "Browser title does not match")
        self.assertEqual(self.landing_page_url, self.browser.current_url, "Current url does not match landing page url")

        # waitPageLoad = WebDriverWait(self.browser, 30).until(EC.presence_of_element_located((By.NAME, "postalCode")))
        zip_code_field = self.browser.find_element(By.NAME, "postalCode")
        self.assertIsNot(zip_code_field, None, "Zip code field is None")
        zip_code_field.send_keys('98105' + Keys.RETURN)
        waitPageLoad = WebDriverWait(self.browser, 30).until(EC.url_to_be(self.building_materials_page_url))
        self.assertEqual(self.building_materials_page_url, self.browser.current_url, "Curent url does not match building materials page url")


    def test_building_material_question_page_data_entry(self):
        """Assert that building material selection works"""
        self.browser.get(self.building_materials_page_url)
        self.assertEqual(self.building_materials_page_url, self.browser.current_url, "Curent url does not match building materials page url")
        waitPageLoad = WebDriverWait(self.browser, 30).until(EC.presence_of_element_located((By.XPATH, self.building_material_straw_radio_button_locator)))

        building_materials_straw_radio_button = self.browser.find_element(By.XPATH, self.building_material_straw_radio_button_locator)
        assert building_materials_straw_radio_button is not None
        building_materials_straw_radio_button.click()
        next_button = self.browser.find_element(By.XPATH, self.next_button_locator)
        assert next_button is not None
        next_button.click()
        waitPageLoad = WebDriverWait(self.browser, 30).until(EC.url_to_be(self.water_proximity_page_url))
        self.assertEqual(self.water_proximity_page_url, self.browser.current_url, "Curent url does not match water proximity page url")


    def test_water_proximity_question_page_data_entry(self):
        """Assert that water proximity selection works"""
        self.browser.get(self.water_proximity_page_url)
        self.assertEqual(self.water_proximity_page_url, self.browser.current_url, "Curent url does not match water proximity page url")
        element = self.browser.find_element(By.XPATH, self.water_proximity_yes_radio_button_locator)
        assert element is not None
        element.click()
        next_button = self.browser.find_element(By.XPATH, self.next_button_locator)
        assert next_button is not None
        next_button.click()
        waitPageLoad = WebDriverWait(self.browser, 30).until(EC.url_to_be(self.quote_page_url))
        self.assertEqual(self.quote_page_url, self.browser.current_url, "Curent url does not match quote page url")
    
    def test_quote_page_checkbox_exists(self):
        """Assert that the quote page checkbox exists and is clickable"""
        self.browser.get(self.quote_page_url)
        waitPageLoad = WebDriverWait(self.browser, 30).until(EC.url_to_be(self.quote_page_url))
        self.assertEqual(self.quote_page_url, self.browser.current_url)
        waitPageLoad = WebDriverWait(self.browser, 30).until(EC.presence_of_element_located((By.XPATH, self.quote_page_checkbox_locator)))
        element = self.browser.find_element(By.XPATH, self.quote_page_checkbox_locator)
        assert element is not None
        element.click()

    def test_complete_flow(self):
        """Assert that the entire flow happy path functions correctly"""
        self.browser.get(self.landing_page_url)
        self.assertEqual('Hurricane Insurance', self.browser.title)
        zip_code_field = self.browser.find_element(By.NAME, "postalCode")
        assert zip_code_field is not None
        zip_code_field.send_keys('98105' + Keys.RETURN)

        waitPageLoad = WebDriverWait(self.browser, 30).until(EC.url_to_be(self.building_materials_page_url))
        self.assertEqual(self.building_materials_page_url, self.browser.current_url)
        building_materials_straw_radio_button = self.browser.find_element(By.XPATH, self.building_material_straw_radio_button_locator)
        assert building_materials_straw_radio_button is not None
        building_materials_straw_radio_button.click()
        building_materials_next_button = self.browser.find_element(By.XPATH, self.next_button_locator)
        assert building_materials_next_button is not None
        building_materials_next_button.click()

        waitPageLoad = WebDriverWait(self.browser, 30).until(EC.url_to_be(self.water_proximity_page_url))
        self.assertEqual(self.water_proximity_page_url, self.browser.current_url)
        water_proximity_yes_button = self.browser.find_element(By.XPATH, self.water_proximity_yes_radio_button_locator)
        assert water_proximity_yes_button is not None
        water_proximity_yes_button.click()
        water_proximity_next_button = self.browser.find_element(By.XPATH, self.next_button_locator)
        assert water_proximity_next_button is not None
        water_proximity_next_button.click()

        waitPageLoad = WebDriverWait(self.browser, 30).until(EC.url_to_be(self.quote_page_url))
        self.assertEqual(self.quote_page_url, self.browser.current_url)
        waitPageLoad = WebDriverWait(self.browser, 30).until(EC.presence_of_element_located((By.XPATH, self.quote_page_checkbox_locator)))
        element = self.browser.find_element(By.XPATH, self.quote_page_checkbox_locator)
        assert element is not None


if __name__ == '__main__':
    unittest.main(verbosity=2)