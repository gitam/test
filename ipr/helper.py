from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import NoSuchElementException


class HelperClass(object):

    def if_click(self, element_xpath):
        try:
            self.check_element_present(element_xpath)

            element = self.wd.find_element_by_xpath(element_xpath)
            self.wd.execute_script("arguments[0].scrollIntoView();", element)

            if self.wd.find_element_by_xpath(element_xpath).is_enabled() and self.wd.find_element_by_xpath(element_xpath).is_displayed():
                element.click()
                return True
        except Exception:
            print('Error clicking on: %s' % element_xpath)

    def if_send(self, element_xpath, text):
        try:
            self.check_element_present(element_xpath)

            element = self.wd.find_element_by_xpath(element_xpath)
            self.wd.execute_script("arguments[0].scrollIntoView();", element)

            if self.wd.find_element_by_xpath(element_xpath).is_enabled() and self.wd.find_element_by_xpath(element_xpath).is_displayed():
                element.send_keys(text)
        except Exception:
            print('Error entering text on: %s' % element_xpath)

    def check_element_present(self, element_xpath):
        try:
            element = WebDriverWait(self.wd, 20).until(
                ec.presence_of_element_located((By.XPATH, element_xpath))
             )
        except NoSuchElementException:
            print('Element is not present: %s' % element_xpath)
            raise