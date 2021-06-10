from selenium import webdriver
import Constants
import Locators
import MockedData
import unittest
import time

class TestLogin(unittest.TestCase):
    def test_login(self):
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
            
            noviMeme=driver.find_element_by_css_selector(Locators.noviMeme_css)
            noviMeme.click() 
            time.sleep(3)

            self.assertEqual(driver.current_url,Constants.BASE_URL)
    
if __name__=="__main__":
    unittest.main()

