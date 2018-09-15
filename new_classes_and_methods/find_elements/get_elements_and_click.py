from selenium import webdriver
from selenium.webdriver.common.by import By


class FindandClick():
    def __init__(self, driver):
        self.driver = driver

    # Locators
    _bmwradio = ("bmwradio")
    _bmwcheck = ("bmwcheck")
    _name = ("name")
    _sometextfield = ("//input[@id='displayed-text']")

    def getradio(self):
        return self.driver.find_element_by_id(self._bmwradio)

    def bmwcheck(self):
        return self.driver.find_element_by_id(self._bmwcheck)

    def name(self):
        return self.driver.find_element_by_id(self._name)

    def texfield(self):
        return self.driver.find_element_by_xpath(self._sometextfield)

    def clickradio(self):
        self.getradio().click()

    def clickbmw(self):
        self.bmwcheck().click()

    def nametext(self, text1):
        self.name().send_keys(text1)

    def sometextfield(self, text2):
        self.texfield().send_keys(text2)

    def fieldsmethod(self, text1, text2):
        self.clickradio()
        self.clickbmw()
        self.nametext(text1)
        self.sometextfield(text2)
