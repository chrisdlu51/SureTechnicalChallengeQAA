import unittest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json


class HurricaneInsuranceTestCase(unittest.TestCase):
    longMessage = True;


"""
NOTE: THIS TEST FILE IS NOT FUNCTIONAL
This file was my attempt to unify the 4 different scripts into a single test runner 
to avoid duplicated code but I couldn't get it running in time.

I've left it here in case you would like to look at it.

"""

def make_test_function(browser):
        
    def test_landing_page_zip_code_entry(self):
        f = open('strings.json')
        strings = json.load(f)
        landing_page_url = strings["landing_page_url"]
        building_materials_page_url = strings["building_material_page_url"]
        water_proximity_page_url = strings["water_proximity_page_url"]
        quote_page_url = strings["quote_page_url"]
        quote_page_checkbox_locator = strings["quote_page_checkbox_locator"]
        building_material_straw_radio_button_locator = strings["building_material_straw_radio_button_locator"]
        next_button_locator = strings["next_button_locator"]
        water_proximity_yes_radio_button_locator = strings["water_proximity_yes_radio_button_locator"]
        
        """Assert that landing page and zip code entry works"""
        browser.get(landing_page_url)
        self.assertEqual('Hurricane Insurance', browser.title, "Browser title does not match")
        self.assertEqual(landing_page_url, browser.current_url, "Current url does not match landing page url")

        zip_code_field = browser.find_element(By.NAME, "postalCode")
        self.assertIsNot(zip_code_field, None, "Zip code field is None")
        zip_code_field.send_keys('98105' + Keys.RETURN)
        waitPageLoad = WebDriverWait(browser, 30).until(EC.url_to_be(building_materials_page_url))
        self.assertEqual(building_materials_page_url, browser.current_url, "Curent url does not match building materials page url")

        f.close()


    return test_landing_page_zip_code_entry


def make_test_function2(browser):
        
    def test_building_material_question_page_data_entry(self):
        f = open('strings.json')
        strings = json.load(f)
        landing_page_url = strings["landing_page_url"]
        building_materials_page_url = strings["building_material_page_url"]
        water_proximity_page_url = strings["water_proximity_page_url"]
        quote_page_url = strings["quote_page_url"]
        quote_page_checkbox_locator = strings["quote_page_checkbox_locator"]
        building_material_straw_radio_button_locator = strings["building_material_straw_radio_button_locator"]
        next_button_locator = strings["next_button_locator"]
        water_proximity_yes_radio_button_locator = strings["water_proximity_yes_radio_button_locator"]
        
        """Assert that building material selection works"""
        browser.get(building_materials_page_url)
        self.assertEqual(building_materials_page_url, browser.current_url, "Curent url does not match building materials page url")
        waitPageLoad = WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.XPATH, building_material_straw_radio_button_locator)))
        building_materials_straw_radio_button = browser.find_element(By.XPATH, building_material_straw_radio_button_locator)
        assert building_materials_straw_radio_button is not None
        building_materials_straw_radio_button.click()
        next_button = browser.find_element(By.XPATH, next_button_locator)
        assert next_button is not None
        next_button.click()
        waitPageLoad = WebDriverWait(browser, 30).until(EC.url_to_be(water_proximity_page_url))
        self.assertEqual(water_proximity_page_url, browser.current_url, "Curent url does not match water proximity page url")
        f.close()


    return test_building_material_question_page_data_entry


if __name__ == '__main__':

    cService = webdriver.ChromeService(executable_path='./chromedriver')
    chrome = webdriver.Chrome(service = cService)

    eService = webdriver.EdgeService(executable_path='./msedgedriver')
    edge = webdriver.Edge(service = eService)

    fService = webdriver.FirefoxService(executable_path='./geckodriver')
    firefox = webdriver.Firefox(service = fService)

    sService = webdriver.SafariService(executable_path='/usr/bin/safaridriver')
    safari = webdriver.Safari(service = sService)


    webdrivers = {chrome: "chrome", edge: "edge", firefox: "firefox", safari: "safari"}

    for driver, name in webdrivers.items():
        test_func = make_test_function(driver)
        setattr(HurricaneInsuranceTestCase, 'test_{0}'.format(name), test_func)

        test_func2 = make_test_function2(driver)
        setattr(HurricaneInsuranceTestCase, 'test_{0}'.format(name), test_func2)

    unittest.main()





