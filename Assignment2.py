# unicode 8
"jkkjkjkjk"
import unittest
import json,csv
import time
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities

class Testassignment(unittest.TestCase):

    def setUp(self):

        Capabilities = DesiredCapabilities.CHROME
        Capabilities['loggingPrefs'] = {'performance': 'ALL'}
        
        self.driver = webdriver.Chrome(
                "C:\\Users\\User\\SCHOOLFILES\\2ndyear\\SOFTWAREQUALITYENG\\chromedriver.exe")
        #C:\Users\User\SCHOOLFILES\2ndyear\SOFTWAREQUALITYENG
        self.driver.implicitly_wait(30) # use for loading the page with the given time of 30 sec.
        self.base_url = "http://en.wikipedia.org/wiki/Software_metric"

    def test_ff (self):
        """
        testing starts here
        """

        driver = self.driver
        self.driver.get(self.base_url)
        time.sleep(10)
        #elm = driver.find_element_by_link_text('login')

        #driver.save_screenshot("First_Screenshot.png")
        #time.sleep(10)
        #elm.click()



        logs = driver.execute_script('return window.performance.getEntries();')
        #self.driver.close()
        

        with open('performance.txt','w') as out:
            json.dump(logs,out, indent = 5, sort_keys=True)
        

        with open('performance.json','w') as out:
            json.dump (logs,out, indent = 5, sort_keys=True)

        with open('performance.csv','w') as out:
            out.write ('URL,Duration\n')
            for row in logs:
                    out.write('%s,%s\n' % (row['name'],str(row['duration'])))

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()

