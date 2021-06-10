from selenium import webdriver
import Constants
import Locators
import MockedData
import unittest
import requests
import time

class TestLogout(unittest.TestCase):
    def test_logout(self):
        for podatak in MockedData.getTestData("MockedLogin.json"):
            driver=webdriver.Chrome()
            driver.get(Constants.BASE_URL)
            driver.maximize_window()
            time.sleep(2)

            prijaviSe=driver.find_element_by_css_selector(Locators.prijaviSe_css)
            prijaviSe.click()
            time.sleep(2)
            imejlLogin=driver.find_element_by_css_selector(Locators.imejllogin_css)
            imejlLogin.send_keys(podatak["email"])
            time.sleep(2)
            sifraLogin=driver.find_element_by_css_selector(Locators.sifralogin_css)
            sifraLogin.send_keys(podatak["password"])
            time.sleep(2)
            ulogujSe=driver.find_element_by_css_selector(Locators.ulogujSe_css)
            ulogujSe.click()        
            time.sleep(2)
            
            odjaviSe=driver.find_element_by_css_selector(Locators.odjaviSe_css)
            odjaviSe.click()
            time.sleep(2)

            self.assertEqual(driver.current_url,Constants.BASE_URL)

if __name__=="__main__":
    unittest.main()
