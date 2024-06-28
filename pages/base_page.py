from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver import ActionChains


class BasePage:
    def __init__(self, driver:WebDriver):
        self.driver = driver

    def find_element_with_wait(self, locator):
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    def click_on_element(self, locator):
        WebDriverWait(self.driver, 50).until(EC.element_to_be_clickable(locator))
        self.driver.find_element(*locator).click()

    def add_text_to_element(self, locator, text):
        self.find_element_with_wait(locator).send_keys(text)

    def drag_and_drop_on_element(self, locator_one, locator_two):
        draggable = WebDriverWait(self.driver, 15).until(EC.presence_of_element_located(locator_one))
        droppable = WebDriverWait(self.driver, 15).until(EC.presence_of_element_located(locator_two))
        action_chains = ActionChains(self.driver)
        action_chains.drag_and_drop(draggable, droppable).perform()

    def get_value(self, locator):
        element = WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located(locator))
        value = element.text
        return value

    def element_is_not_displayed(self, locator):
        return WebDriverWait(self.driver, 15).until(EC.invisibility_of_element_located(locator))

    def get_current_url(self):
        return self.driver.current_url

    def element_is_present(self, locator):
        return WebDriverWait(self.driver, 15).until(EC.presence_of_element_located(locator))

    def get_text_from_element(self, locator):
        return self.find_element_with_wait(locator).text
