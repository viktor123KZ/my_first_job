import time

from selene import browser
from selene import  have

a = 'Bukarev Viktor Vladimirovich'
e = 'bukarev1985@gmail.com'
address = '1, testovaya str, Almaty, Kazakhstan'
address2 = '2, testovaya str, Almaty, Kazakhstan'

def test1():
    browser.open('https://demoqa.com/text-box')
    browser.element('[id="userName"]').type(a)
    browser.element('[id="userEmail"]').type(e)
    browser.element('//*[@id="currentAddress-wrapper"]/div[2] //*[@id="currentAddress"]').type(address)
    browser.element('//*[@id="permanentAddress-wrapper"]/div[2] //*[@id="permanentAddress"]').type(address2)
    browser.element('[id="submit"]').click()

    browser.element('//*[@id="name"]').should(have.exact_text('Name:Bukarev Viktor Vladimirovich'))

    browser.element('//*[@id="email"]').should(have.exact_text('Email:bukarev1985@gmail.com'))
    browser.element('//*[@id="output"]/div //*[@id="currentAddress"]').should(have.exact_text('Current Address :1, testovaya str, Almaty, Kazakhstan'))
    browser.element('//*[@id="output"] //*[@id="permanentAddress"]').should(have.exact_text('Permananet Address :2, testovaya str, Almaty, Kazakhstan'))
    time.sleep(4)