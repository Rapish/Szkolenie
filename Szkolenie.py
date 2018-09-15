import time

from selenium import webdriver
from selenium.webdriver.support.select import Select
from new_classes_and_methods.find_elements.get_elements_and_click import FindandClick
from new_classes_and_methods.open_page.openpage import WebPage


class MineTest():

    def test(self):
        driver = webdriver.Firefox()
        wp = WebPage(driver)
        wp.openWebpage("https://letskodeit.teachable.com/p/practice")


        fm = FindandClick(driver)
        fm.fieldsmethod("Pierwszy tekst, writing something", "Drugi tekst, second time writing something")

        # driver.find_element_by_id("bmwradio").click()
        # driver.find_element_by_id("bmwcheck").click()
        # driver.find_element_by_id("name").send_keys("Wpisuje tutaj testowy tekst")
        # driver.find_element_by_xpath("//input[@id='displayed-text']").send_keys("Wpisuje kolejny tekst")


        selectExample = driver.find_element_by_id("carselect")
        sel = Select(selectExample)
        sel.select_by_value("benz")

        #Hide, Show i Napis
        driver.find_element_by_id("hide-textbox").click()
        time.sleep(3)
        driver.find_element_by_id("show-textbox").click()
        time.sleep(3)
        driver.find_element_by_id("displayed-text").send_keys("Wpisuje sobie cos")


        #otwieramy okno
        parentHandle = driver.current_window_handle
        driver.find_element_by_id("openwindow").click()
        time.sleep(4)
        handles = driver.window_handles

        for handle in handles:
            print(handle)
            if handle not in parentHandle:
                driver.switch_to.window(handle)
                x = driver.find_element_by_xpath("//input[@id='search-courses']")
                x.send_keys("test")
                time.sleep(3)
                driver.close()

        driver.switch_to_window(parentHandle)
        driver.find_element_by_id("name").send_keys("TEST SIE UDAL !!")
        time.sleep(3)

        driver.close()

        if driver.close:
           print("Brawo, twój test się udał !!")

open = MineTest()
open.test()