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
        cService = webdriver.ChromeService(executable_path='./chromedriver')
        self.browser = webdriver.Chrome(service = cService)
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

    """
    def test_using_locators_file(self):
        print(self.strings['some_text'])

        self.assertEqual(self.strings['some_text'], "someMoreText", "IT WORKED!!!")
    """


    def test_landing_page_zip_code_entry(self):
        """Assert that landing page and zip code entry works"""
        self.browser.get(self.landing_page_url)
        self.assertIn('Hurricane Insurance', self.browser.title)

        # waitPageLoad = WebDriverWait(self.browser, 30).until(EC.presence_of_element_located((By.NAME, "postalCode")))
        element = self.browser.find_element(By.NAME, "postalCode")
        assert element is not None
        element.send_keys('98105' + Keys.RETURN)

    def test_building_material_question_page_data_entry(self):
        """Assert that building material selection works"""
        self.browser.get(self.building_materials_page_url)
        self.assertIn(self.building_materials_page_url, self.browser.current_url)
        element = self.browser.find_element(By.XPATH, self.building_material_straw_radio_button_locator)
        assert element is not None
        element.click()
        next_button = self.browser.find_element(By.XPATH, self.next_button_locator)
        assert next_button is not None
        next_button.click()

    def test_water_proximity_question_page_data_entry(self):
        """Assert that water proximity selection works"""
        self.browser.get(self.water_proximity_page_url)
        self.assertIn(self.water_proximity_page_url, self.browser.current_url)
        element = self.browser.find_element(By.XPATH, self.water_proximity_yes_radio_button_locator)
        assert element is not None
        element.click()
        next_button = self.browser.find_element(By.XPATH, self.next_button_locator)
        assert next_button is not None
        next_button.click()

    
    def test_quote_page_checkbox_exists(self):
        """Assert that the quote page checkbox exists and is clickable"""
        self.browser.get(self.quote_page_url)
        waitPageLoad = WebDriverWait(self.browser, 30).until(EC.url_to_be(self.quote_page_url))
        self.assertIn(self.quote_page_url, self.browser.current_url)
        waitPageLoad = WebDriverWait(self.browser, 30).until(EC.presence_of_element_located((By.XPATH, self.quote_page_checkbox_locator)))
        element = self.browser.find_element(By.XPATH, self.quote_page_checkbox_locator)
        assert element is not None
        element.click()

    def test_complete_flow(self):
        """Assert that the entire flow happy path functions correctly"""
        self.browser.get(self.landing_page_url)
        self.assertIn('Hurricane Insurance', self.browser.title)
        element = self.browser.find_element(By.NAME, "postalCode")
        assert element is not None
        element.send_keys('98105' + Keys.RETURN)

        waitPageLoad = WebDriverWait(self.browser, 30).until(EC.url_to_be(self.building_materials_page_url))
        self.assertIn(self.building_materials_page_url, self.browser.current_url)
        element = self.browser.find_element(By.XPATH, self.building_material_straw_radio_button_locator)
        assert element is not None
        element.click()
        next_button = self.browser.find_element(By.XPATH, self.next_button_locator)
        assert next_button is not None
        next_button.click()

        waitPageLoad = WebDriverWait(self.browser, 30).until(EC.url_to_be(self.water_proximity_page_url))
        self.assertIn(self.water_proximity_page_url, self.browser.current_url)
        element = self.browser.find_element(By.XPATH, self.water_proximity_yes_radio_button_locator)
        assert element is not None
        element.click()
        next_button = self.browser.find_element(By.XPATH, self.next_button_locator)
        assert next_button is not None
        next_button.click()

        waitPageLoad = WebDriverWait(self.browser, 30).until(EC.url_to_be(self.quote_page_url))
        self.assertIn(self.quote_page_url, self.browser.current_url)
        waitPageLoad = WebDriverWait(self.browser, 30).until(EC.presence_of_element_located((By.XPATH, self.quote_page_checkbox_locator)))
        element = self.browser.find_element(By.XPATH, self.quote_page_checkbox_locator)
        assert element is not None


if __name__ == '__main__':
    unittest.main(verbosity=2)