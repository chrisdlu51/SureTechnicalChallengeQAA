import unittest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class HurricianeInsuranceTestCase(unittest.TestCase):

    def setUp(self):
        """Explicitly create a Chrome browser instance."""
        cService = webdriver.ChromeService(executable_path='./chromedriver')
        self.browser = webdriver.Chrome(service = cService)
        self.addCleanup(self.browser.quit)

    def test_page_title(self):
        """Assert that title of page says 'Hurricane Insurance'."""
        self.browser.get('https://sure-qa-challenge.vercel.app/')
        self.assertIn('Hurricane Insurance', self.browser.title)

    def test_landing_page_zip_code_entry(self):
        """Assert that"""
        self.browser.get('https://sure-qa-challenge.vercel.app/')
        self.assertIn('Hurricane Insurance', self.browser.title)
        element = self.browser.find_element(By.NAME, "postalCode")
        assert element is not None
        element.send_keys('98105' + Keys.RETURN)
        # assert self.browser.title.startswith('Red Hat')

if __name__ == '__main__':
    unittest.main(verbosity=2)