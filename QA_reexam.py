# unicode 8
"TestingUnitest"
import unittest
import time
from selenium import webdriver

class QAExam(unittest.TestCase):
    "Testing"
    def setUp(self):
        self.driver = webdriver.Chrome(
            "C:\\Users\\User\\SCHOOLFILES\\2ndyear\\SOFTWAREQUALITYENG\\chromedriver.exe")
        self.driver.implicitly_wait(30) # use for loading the page with the given time of 30 sec.
        self.base_url = "https://danibudi.github.io/Cross-Site%20Scripting%20(safe%20XSS).html"
    def test_ss(self):
        """
        Error free coding
        """
        driver = self.driver
        driver.get(self.base_url)
        time.sleep(10)
        alert = driver.switch_to_alert()
        alert.accept()
        elm = driver.find_element_by_link_text('Click here to see solution of problem in Django')
        driver.implicitly_wait(10)
        elm.click()
        driver.save_screenshot("First_Screenshot.png")
        time.sleep(10)
        try:
            assert 'Django' in driver.page_source
            print('Asertion testpassed')
        except ImportError as e_a:
            print('Asertion testfailed', format(e_a))
        driver.back()
        time.sleep(10)
        alert = driver.switch_to_alert()
        alert.accept()
        time.sleep(10)
        elm = driver.find_element_by_link_text('Click here to see solution of problem - html file')
        driver.implicitly_wait(10) #use for loading the page with the given time of 30 sec.
        elm.click()
        time.sleep(10)
        try:
            assert 'There is an allert on this page' in driver.page_source
            print('Asertion testpassed')
        except ImportError as e_c:
            print('Asertion testfailed', format(e_c))
    def tearDown(self):
        self.driver.quit()
if __name__ == "__main__":
    unittest.main()
