from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver: WebDriver, base_url: str):
        self.driver = driver
        self.base_url = base_url
        self.wait = WebDriverWait(driver, 15)

    def open(self, path: str = "/"):
        self.driver.get(self.base_url.rstrip("/") + path)

    def click(self, locator):
        el = self.wait.until(EC.element_to_be_clickable(locator))
        el.click()
        return el

    def type(self, locator, text: str, clear=True):
        el = self.wait.until(EC.presence_of_element_located(locator))
        if clear:
            el.clear()
        el.send_keys(text)
        return el

    def visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))
