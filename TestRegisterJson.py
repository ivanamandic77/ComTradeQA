from selenium import webdriver
import Constants
import Locators
import requests
import time
import MockedData

def RegistrujteSe(usr,email,psw):
    driver=webdriver.Chrome()
    driver.get(Constants.BASE_URL)
    driver.maximize_window()
    time.sleep(2)
    prijaviSe=driver.find_element_by_css_selector("header:nth-child(1) div.meniji ul.lista li:nth-child(2) > a:nth-child(1)")
    prijaviSe.click()
    time.sleep(2)
    registrujteSe=driver.find_element_by_css_selector(Locators.registrujteSe_css)
    registrujteSe.click()
    time.sleep(3)

    korisnickoIme=driver.find_element_by_css_selector(Locators.korisnickoIme_css)
    imejl=driver.find_element_by_css_selector(Locators.imejlreg_css)
    sifra=driver.find_element_by_css_selector(Locators.sifrareg_css)
    ponoviSifru=driver.find_element_by_css_selector(Locators.potvrdaSifre_css)
    registrujSe=driver.find_element_by_css_selector(Locators.registrujSe_dugme_css)

    korisnickoIme.send_keys(usr)
    imejl.send_keys(email)
    sifra.send_keys(psw)
    ponoviSifru.send_keys(psw)
    registrujSe.click()
    time.sleep(3)
    

    if driver.find_elements_by_css_selector(Locators.ok_css):
        print("Uspesno ste se registrovali")
    else:
        print("Neuspesna registracija")

test_data=MockedData.getTestData("Mocked_Register.json")
for podatak in test_data:
    RegistrujteSe(podatak["username"],podatak["email"],podatak["password"])

#promeni podatke u json fajlu jer su ovi postojeci vec registrovani