import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#Refer to http://selenium-python.readthedocs.org/en/latest/api.html for API
#Refer to http://docs.python.org/2/library/unittest.html for unittest 

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.set_window_size(1024, 768)

        #Twitter dummy account
        self.username = "cio_test"
        self.password = "CIOtest123"

        #Page title
        self.loginPageTitle = "login page"
        self.mainPageTiltle = "home page"

        #Links for CIO page
        self.url_HomePage = "http://idata-a.d1.comp.nus.edu.sg/home"

    #This will be testing the Home page
    def test_HomePage(self):
        driver = self.driver
        driver.get(self.url_HomePage)
        self.assertIn(self.loginPageTitle, driver.title)


    #This will be testing logging in with Twitter
    def test_TwitterLogin(self):
        driver = self.driver
        driver.get(self.url_HomePage)
        self.assertIn(self.loginPageTitle, driver.title)
        elem = driver.find_element_by_xpath("//a[@class=\"btn btn-primary btn-large\"]")
        elem.click()
        self.assertIn("Twitter / Authorize an application", driver.title)
        elem_username = driver.find_element_by_id("username_or_email")
        elem_username.send_keys(self.username)
        elem_password = driver.find_element_by_id("password")
        elem_password.send_keys(self.password)
        driver.find_element_by_id("allow").click()
        time.sleep(2)
        self.assertIn(self.mainPageTiltle, driver.title)

    def test_Logout(self):
        self.test_TwitterLogin()
        driver = self.driver
        driver.get(self.url_HomePage)
        find_element_by_id("dLabel").click()
        time.sleep(0.5)
        elem = driver.find_element_by_xpath("//a[@id=\"logout\"]").click()
        time.sleep(2)
        self.assertIn(self.loginPageTitle, driver.title)

    #This will testing the main page after logging in
    def test_MainPage(self):
        self.test_TwitterLogin()
        driver = self.driver
        driver.get(self.url_HomePage)
        time.sleep(3)
        try:
            driver.find_element_by_xpath("//a[contains(@href,'#tab1')]")
        except NoSuchElementException:
            assert 0, "Did not return correct search result"

    #This will be testing CIO search
    def test_Search(self):
        self.test_TwitterLogin()
        driver = self.driver
        driver.get(self.url_HomePage)
        elem = driver.find_element_by_xpath("//input[@class=\"search-query span2\"]")
        elem.send_keys("Singapore")
        elem.send_keys(Keys.RETURN)
        time.sleep(1)
        try:
            driver.find_element_by_xpath("//a[contains(@href,'/home/en/?title=Singapore')]")
        except NoSuchElementException:
            assert 0, "Did not return correct search result"

    def test_doubleSearch(self):
        self.test_Search()
        driver = self.driver
        driver.get(self.url_HomePage)
        elem = driver.find_element_by_xpath("//input[@class=\"search-query span2\"]")
        elem.send_keys("NUS")
        elem.send_keys(Keys.RETURN)
        time.sleep(2)
        try:
            driver.find_element_by_xpath("//a[contains(@href,'/home/en/?title=NUS')]")
        except NoSuchElementException:
            assert 0, "Did not return correct search result"

    def test_MoreTweets(self):
        self.test_TwitterLogin()
        driver = self.driver
        driver.get(self.url_HomePage)
        elem = driver.find_element_by_link_text("Wikipedia")
        elem.click()
        time.sleep(10)
        elem = driver.find_element_by_id("loadMore")
        self.assertIn("No New Tweets", driver.find_element_by_id("loadMore").text)


    #This will end the test suite
    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()