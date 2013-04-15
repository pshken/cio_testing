import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

        #Twitter dummy account
        self.username = "cio_test"
        self.password = "CIOtest123"

        #Links for CIO page
        self.url_HomePage = "http://idata-a.d1.comp.nus.edu.sg:82/home"
        self.url_MainPage = ""

    #This will be testing the Home page
    def test_HomePage(self):
        driver = self.driver
        driver.get(self.url_HomePage)
        self.assertIn("Python", driver.title)
        #elem = driver.find_element_by_name("q")
        #elem.send_keys("selenium")
        #elem.send_keys(Keys.RETURN)
        #self.assertIn("Google", driver.title)

    #This will be testing logging in with Twitter
    def test_Login(self):
        driver = self.driver
        driver.get(self.url_HomePage)

    #This will testing the main page after logging in
    def test_MainPage(self):
        driver = self.driver
        driver.get(self.url)

    #This will be testing CIO search
    def test_Search(self):
        driver = self.driver
        driver.get(self.url_MainPage)
        #elem = driver.find_element_by_name("")
        #elem.send_keys("Singapore")
        #elem.send_keys(Keys.RETURN)
        #time.sleep(1)
        #try:
            #driver.find_element_by_xpath("//a[contains(@href,'http://seleniumhq.org')]")
        #except NoSuchElementException:
            #assert 0, "can't find seleniumhq"


    #This will end the test suite
    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()