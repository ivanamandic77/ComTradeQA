from selenium import webdriver
import Constants
import Locators
import requests


def DaLiJeAktivan(sajt):
    response=requests.get(sajt)
    if(response.status_code==200):
        return True
    else:
        return False

if (DaLiJeAktivan(Constants.BASE_URL)==True):
    print("Sajt je online")
else:
    print("Sajt nije online")