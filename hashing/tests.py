from django.test import TestCase
from selenium import webdriver
import os
<<<<<<< HEAD
from .forms import HashForm
import hashlib
from .models import Hash
# class FunctionalTestCase(TestCase):
    #
    # def setUp(self):
    #     self.chromedriver = "chromedriver.exe"  #chromedriver should be installed and env variable shuould be setup in advance
    #     os.environ["webdriver.chrome.driver"] = self.chromedriver
    #     self.browser = webdriver.Chrome(self.chromedriver)
    #
    # def test_there_is_homepage(self):
    #     self.browser.get('http://localhost:8000')
    #     self.assertIn('Enter hash here:', self.browser.page_source)
    #
    # def test_hash_of_hello(self):
    #     self.browser.get('http://localhost:8000')
    #     text = self.browser.find_element_by_id('id_text')
    #     text.send_keys('hello')
    #     self.browser.find_element_by_name('submit').click()
    #     self.assertIn('2CF24DBA5FB0A30E26E83B2AC5B9E29E1B161E5C1FA7425E73043362938B9824', self.browser.page_source)

    # def tearDown(self):
    #     self.browser.quit()


class UnitTestCase(TestCase):

    def test_home_homepage_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'hashing/home.html')

    def test_hash_form(self):
        form = HashForm(data={'text': 'hello'})
        self.assertTrue(form.is_valid())

    def test_hash_func_works(self):
        text_hash = hashlib.sha256('hello'.encode('utf-8')).hexdigest().upper()
        self.assertEqual('2CF24DBA5FB0A30E26E83B2AC5B9E29E1B161E5C1FA7425E73043362938B9824', text_hash)

    def test_hash_object(self):
        hash = Hash()
        hash.text = 'hello'
        hash.hash = '2CF24DBA5FB0A30E26E83B2AC5B9E29E1B161E5C1FA7425E73043362938B9824'
        hash.save()
        pulled_hash = Hash.objects.get(hash='2CF24DBA5FB0A30E26E83B2AC5B9E29E1B161E5C1FA7425E73043362938B9824')
        self.assertEqual(hash.text, pulled_hash)
=======

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
>>>>>>> d477822c606c8260cee2431faa7f2809d23cc037
