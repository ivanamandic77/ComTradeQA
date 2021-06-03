from selenium import webdriver
import Locators
import Constants
import time


def UlogujteSe(imejl,sifra):
    driver.get(Constants.BASE_URL)
    driver.maximize_window()
    time.sleep(5)
    prijaviSe=driver.find_element_by_css_selector("header:nth-child(1) div.meniji ul.lista li:nth-child(2) > a:nth-child(1)")
    prijaviSe.click()
    time.sleep(5)
    
    unesiImejl=driver.find_element_by_css_selector(Locators.imejllogin_css)
    unesiSifru=driver.find_element_by_css_selector(Locators.sifralogin_css)
    ulogujSe=driver.find_element_by_css_selector(Locators.ulogujSe_css)

    unesiImejl.send_keys(imejl)
    unesiSifru.send_keys(sifra)
    ulogujSe.click()
    time.sleep(3)

n=int(input("Koliko mimova zelis da vidis? "))
imejl=input("Unesite vasu email adresu:")
sifra=input("Unesite sifru:")
driver=webdriver.Chrome()
UlogujteSe(imejl,sifra)
time.sleep(3)
klik=driver.find_element_by_css_selector(Locators.noviMeme_css)
i=1
while i<n:
    klik.click()
    time.sleep(2)
    i=i+1

driver.close() 
