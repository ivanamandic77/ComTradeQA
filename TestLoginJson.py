from selenium import webdriver
import Constants
import Locators
import MockedData
import time

def TestLogin(email,password):
    driver=webdriver.Chrome()
    driver.get(Constants.BASE_URL)
    driver.maximize_window()

    prijava=driver.find_element_by_css_selector(Locators.prijaviSe_css)
    prijava.click()
    mejl=driver.find_element_by_css_selector(Locators.imejllogin_css)
    sifra=driver.find_element_by_css_selector(Locators.sifralogin_css)
    login=driver.find_element_by_css_selector(Locators.ulogujSe_css)

    mejl.send_keys(email)
    sifra.send_keys(password)
    login.click()
    time.sleep(3)


    if driver.current_url==Constants.BASE_URL:
        print(f"Uspesno ste se ulogovali sa {email} and {password}")
    else:
        print(f"Neuspesna prijava sa {email} and {password}")
    time.sleep(3)


test_data=MockedData.getTestData("Mocked_Login.json")
for podatak in test_data:
    TestLogin(podatak["email"],podatak["password"])



