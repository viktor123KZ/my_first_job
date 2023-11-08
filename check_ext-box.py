import time

from selene import browser
from selene import  have

a = 'Bukarev Viktor Vladimirovich'
e = 'bukarev1985@gmail.com'
address = ' 1, testovaya str, Almaty, Kazakhstan'
address2 = '1, testovaya str, Almaty, Kazakhstan'

def test_check_ext_box():
    browser.open('https://demoqa.com/text-box')
    browser.element('[id="userName"]').type(a)
    browser.element('[id="userEmail"]').type(e)
    browser.element('//*[@id="currentAddress-wrapper"]/div[2]').type(address)
    browser.element('//*[@id="permanentAddress-wrapper"]/div[2]').type(address2)
    browser.element('[id="submit"]').click()
    time.sleep(45)