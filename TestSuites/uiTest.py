from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import sys, unittest, os.path
sys.path.append(os.path.join(os.path.dirname(__file__),'../'))

class googleTest(unittest.TestCase):
    """ Testcases to test google search functionality"""

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.co.in/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_GoogleTitle(self):
        self.driver.get(self.base_url)
        self.assertEqual("Google", self.driver.title)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
