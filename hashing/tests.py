from django.test import TestCase
from selenium import webdriver
import os

class FunctionalTestCase(TestCase):

    def setUp(self):
        self.chromedriver = "chromedriver.exe"  #chromedriver should be installed and env variable shuould be setup in advance
        os.environ["webdriver.chrome.driver"] = self.chromedriver
        self.browser = webdriver.Chrome(self.chromedriver)

    def test_there_is_homepage(self):
        self.browser.get('http://localhost:8000')
        self.assertIn('install', self.browser.page_source)

    def tearDown(self):
        self.browser.quit()
