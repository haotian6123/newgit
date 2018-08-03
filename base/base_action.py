from selenium.webdriver.support.wait import WebDriverWait


class BaseAction:

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, feature, timeout=5, poll=1):
        feature_by = feature[0]
        feature_value = feature[1]

        web_driver_wait = WebDriverWait(self.driver, timeout, poll)
        return web_driver_wait.until(lambda x: x.find_element(feature_by, feature_value))

    def find_elements(self, feature, timeout=5, poll=1):
        feature_by = feature[0]
        feature_value = feature[1]

        web_driver_wait = WebDriverWait(self.driver, timeout, poll)
        return web_driver_wait.until(lambda x: x.find_elements(feature_by, feature_value))

    def click(self, feature):
        self.find_element(feature).click()

    def input(self, feature, text):
        self.find_element(feature).send_keys(text)