from selenium import webdriver
import Locators
import Constants
import time


def IzlogujSe(imejl,sifra):
    driver=webdriver.Chrome()
    driver.get(Constants.BASE_URL)
    driver.maximize_window()
    time.sleep(5)
    prijaviSe=driver.find_element_by_css_selector(Locators.prijaviSe_css)
    prijaviSe.click()
    time.sleep(5)
    
    unesiImejl=driver.find_element_by_css_selector(Locators.imejllogin_css)
    unesiSifru=driver.find_element_by_css_selector(Locators.sifralogin_css)
    ulogujSe=driver.find_element_by_css_selector(Locators.ulogujSe_css)
    odjaviSe=driver.find_element_by_css_selector(Locators.odjaviSe_css)

    unesiImejl.send_keys(imejl)
    unesiSifru.send_keys(sifra)
    ulogujSe.click()
    time.sleep(2)
    odjaviSe.click()


IzlogujSe("bobicicd@hotmail.com","Nekasifra1")
print("Uspesno ste se izlogovali")
time.sleep(2)





