from selenium import webdriver


class WebPage():

    def __init__(self, driver):
        self.driver = driver

    def openWebpage(self, URL):
        baseURL = (URL)
        self.driver.maximize_window()
        self.driver.get(URL)