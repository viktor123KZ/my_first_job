from selene import browser, have
def test_1():
    browser.open('https://demoqa.com/text-box')
    browser.element('[id=userName]').type('Madina')  #атрибуты с названием id можно сокращать и использовать '#' - получится #userName
    browser.element('[id=userEmail]').type('noname@mailforspam.com')
    browser.element('[id=currentAddress]').type('Moscow')
    browser.element('[id=permanentAddress]').type('Moscow')

    browser.execute_script("window.scrollTo(0, 1080)") # Эта часть когда прокручивает страницу в низ, тем самым проггружает элементы ( в нашем случае - кнопка)

    browser.element('//*[@id="submit"]').click()
    browser.element('[id=name]').should(have.exact_text('Name:Madina'))
    browser.element('[id=email]').should(have.exact_text('Email:noname@mailforspam.com'))
    browser.element('//*[@id="output"]/div //*[@id="currentAddress"]').should(have.exact_text('Current Address :Moscow'))
    browser.element('//*[@id="output"] //*[@id="permanentAddress"]').should(have.exact_text('Permananet Address :Moscow'))