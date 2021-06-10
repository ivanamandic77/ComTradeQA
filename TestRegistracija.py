from selenium import webdriver
import Constants
import Locators
import requests
import time

def RegistrujteSe(usr,email,psw,psw1):
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
    ponoviSifru.send_keys(psw1)
    registrujSe.click()
    time.sleep(3)
    

    if driver.find_elements_by_css_selector(Locators.ok_css):
        print("Uspesno ste se registrovali")
    else:
        print("Neuspesna registracija")



korisnickoIme=input("Unesite korisnicko ime: ")
imejl=input("Unesite email adresu:")
sifra=input("Unesite sifru (Sifra mora da ima najmanje 8 karaktera, 1 veliko sovo i 1 broj):")
ponoviSifru=input("Ponovite sifru:")

RegistrujteSe(korisnickoIme,imejl,sifra,ponoviSifru)




