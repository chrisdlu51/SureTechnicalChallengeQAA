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

        self.f = open('locators.json')
        self.locators = json.load(self.f)

    def tearDown(self):
        self.f.close()

    def test_using_locators_file(self):
        print(self.locators['some_text'])

        self.assertEqual(self.locators['some_text'], "someMoreText", "IT WORKED!!!")


    def test_landing_page_zip_code_entry(self):
        """Assert that landing page and zip code entry works"""
        self.browser.get('https://sure-qa-challenge.vercel.app/')
        self.assertIn('Hurricane Insurance', self.browser.title)

        # waitPageLoad = WebDriverWait(self.browser, 30).until(EC.presence_of_element_located((By.NAME, "postalCode")))
        element = self.browser.find_element(By.NAME, "postalCode")
        assert element is not None
        element.send_keys('98105' + Keys.RETURN)

    def test_building_material_question_page_data_entry(self):
        """Assert that building material selection works"""
        self.browser.get('https://sure-qa-challenge.vercel.app/building-material')
        self.assertIn('https://sure-qa-challenge.vercel.app/building-material', self.browser.current_url)
        element = self.browser.find_element(By.XPATH, "//input[@type='radio' and @value='straw']")
        assert element is not None
        element.click()
        next_button = self.browser.find_element(By.XPATH, "//*[@id=\"__next\"]/div/div/div/div/div/form/div[2]/button")
        assert next_button is not None
        next_button.click()

    def test_water_proximity_question_page_data_entry(self):
        """Assert that water proximity selection works"""
        self.browser.get('https://sure-qa-challenge.vercel.app/water-proximity')
        self.assertIn('https://sure-qa-challenge.vercel.app/water-proximity', self.browser.current_url)
        element = self.browser.find_element(By.XPATH, "//*[@id=\"__next\"]/div/div/div/div/div/form/div[1]/fieldset/div/label[1]/span[1]/span[1]/input")
        assert element is not None
        element.click()
        next_button = self.browser.find_element(By.XPATH, "//*[@id=\"__next\"]/div/div/div/div/div/form/div[2]/button")
        assert next_button is not None
        next_button.click()

    
    def test_quote_page_checkbox_exists(self):
        """Assert that the quote page checkbox exists and is clickable"""
        self.browser.get('https://sure-qa-challenge.vercel.app/quote')
        waitPageLoad = WebDriverWait(self.browser, 30).until(EC.url_to_be("https://sure-qa-challenge.vercel.app/quote"))
        self.assertIn('https://sure-qa-challenge.vercel.app/quote', self.browser.current_url)
        waitPageLoad = WebDriverWait(self.browser, 30).until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"__next\"]/div/div/div/div/div/form/div/div/div[2]/div/div/div[5]/label/span[1]/span[1]/input")))
        element = self.browser.find_element(By.XPATH, "//*[@id=\"__next\"]/div/div/div/div/div/form/div/div/div[2]/div/div/div[5]/label/span[1]/span[1]/input")
        assert element is not None
        element.click()

    def test_complete_flow(self):
        """Assert that the entire flow happy path functions correctly"""
        self.browser.get('https://sure-qa-challenge.vercel.app/')
        self.assertIn('Hurricane Insurance', self.browser.title)
        element = self.browser.find_element(By.NAME, "postalCode")
        assert element is not None
        element.send_keys('98105' + Keys.RETURN)

        waitPageLoad = WebDriverWait(self.browser, 30).until(EC.url_to_be("https://sure-qa-challenge.vercel.app/building-material"))
        self.assertIn('https://sure-qa-challenge.vercel.app/building-material', self.browser.current_url)
        element = self.browser.find_element(By.XPATH, "//input[@type='radio' and @value='straw']")
        assert element is not None
        element.click()
        next_button = self.browser.find_element(By.XPATH, "//*[@id=\"__next\"]/div/div/div/div/div/form/div[2]/button")
        assert next_button is not None
        next_button.click()

        waitPageLoad = WebDriverWait(self.browser, 30).until(EC.url_to_be("https://sure-qa-challenge.vercel.app/water-proximity"))
        self.assertIn('https://sure-qa-challenge.vercel.app/water-proximity', self.browser.current_url)
        element = self.browser.find_element(By.XPATH, "//*[@id=\"__next\"]/div/div/div/div/div/form/div[1]/fieldset/div/label[1]/span[1]/span[1]/input")
        assert element is not None
        element.click()
        next_button = self.browser.find_element(By.XPATH, "//*[@id=\"__next\"]/div/div/div/div/div/form/div[2]/button")
        assert next_button is not None
        next_button.click()

        waitPageLoad = WebDriverWait(self.browser, 30).until(EC.url_to_be("https://sure-qa-challenge.vercel.app/quote"))
        self.assertIn('https://sure-qa-challenge.vercel.app/quote', self.browser.current_url)
        waitPageLoad = WebDriverWait(self.browser, 30).until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"__next\"]/div/div/div/div/div/form/div/div/div[2]/div/div/div[5]/label/span[1]/span[1]/input")))
        element = self.browser.find_element(By.XPATH, "//*[@id=\"__next\"]/div/div/div/div/div/form/div/div/div[2]/div/div/div[5]/label/span[1]/span[1]/input")
        assert element is not None


if __name__ == '__main__':
    unittest.main(verbosity=2)