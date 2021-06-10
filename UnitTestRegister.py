from selenium import webdriver
import Constants
import Locators
import MockedData
import unittest
import requests
import time

class TestRegister(unittest.TestCase):
    def test_register(self):
        for podatak in MockedData.getTestData("MockedRegister.json"):
            driver=webdriver.Chrome()
            driver.get(Constants.BASE_URL)
            driver.maximize_window()

            prijaviSe=driver.find_element_by_css_selector(Locators.prijaviSe_css)
            prijaviSe.click()
            time.sleep(2)
            registrujSe=driver.find_element_by_css_selector(Locators.registrujteSe_css)
            registrujSe.click()
            time.sleep(2)
            korisnickoIme=driver.find_element_by_css_selector(Locators.korisnickoIme_css)
            korisnickoIme.send_keys(podatak["username"])
            imejlReg=driver.find_element_by_css_selector(Locators.imejlreg_css)
            imejlReg.send_keys(podatak["email"])
            sifraReg=driver.find_element_by_css_selector(Locators.sifrareg_css)
            sifraReg.send_keys(podatak["password"])
            potvrdaSifre=driver.find_element_by_css_selector(Locators.potvrdaSifre_css)
            potvrdaSifre.send_keys(podatak["password"])
            time.sleep(2)
            registracijaDugme=driver.find_element_by_css_selector(Locators.registrujSe_dugme_css)
            registracijaDugme.click()
            time.sleep(2)
            
            ok=driver.find_element_by_css_selector(Locators.ok_css)
#           ok=True (Prvobitna verzija (radi), al sam onda shvatila da je ovo visak)
           
            self.assertTrue(ok)
           

if __name__=="__main__":
    unittest.main()

# Dugo sam razmisljala kako da se proveri uspesnost registracije. preko login forme kao u prvom projektu je nemoguce
# jer ce se ulogovati svakako i ako podaci vec postoje(znaci neuspesna registracija) i onda sam se setila tog cuvenog OK sto ste stavili. 
# pa sam trazila kako da napravim test koji ce proveravati da li postoji taj OK (sto je dokaz uspesne registracije!) i uspela sa true fazonom..... 