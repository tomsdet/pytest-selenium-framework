from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class PageBase:

    def __init__(self, driver):
        self.driver = driver

    def webelement_listesinden_string_listesi_ver(self, locator):
        elements = self.driver.find_elements(*locator)
        liste = []
        for i in elements:
            liste.append(i.text)

        return liste

    def wait_element_visibility(self, locator):
        element = WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located(locator))
        return element

    def wait_element_presence(self, locator):
        element = WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located(locator))
        return element

    def wait_alert_presence(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.alert_is_present())