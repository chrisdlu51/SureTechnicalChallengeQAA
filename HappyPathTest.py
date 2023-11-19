# hello.py

import unittest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options


#chrome_options = Options()
#chrome_options.add_experimental_option("detach", True)
cService = webdriver.ChromeService(executable_path='./chromedriver')
driver = webdriver.Chrome(service = cService)
#driver = webdriver.Chrome(options=chrome_options)

driver.get("https://www.python.org")
search_bar = driver.find_element("name", "q")
search_bar.clear()
search_bar.send_keys("getting started with python")
search_bar.send_keys(Keys.RETURN)
print(driver.current_url)