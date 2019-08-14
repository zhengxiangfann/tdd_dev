#coding:utf-8

from selenium import webdriver
import unittest
# browser = webdriver.Firefox()
# browser.get("http://localhost:8000")
# assert 'Django' in browser.title

class NewVistorTest(unittest.TestCase): #@1
    def setUp(self): #@2
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)
    def tearDown(self): # @3
        self.browser.quit()
    def test_can_start_a_list_and_retrieve_it_later(self):
        self.browser.get('http://localhost:8000')
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test!')


if __name__ == '__main__':
    unittest.main(warnings='ignore')

