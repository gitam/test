import unittest
import os
from drivers_setup import SeleniumObject
from helper import HelperClass

URL = os.environ.get('URL', 'http://www.google.com')


class ContactForm(SeleniumObject, HelperClass, unittest.TestCase):

    def setUp(self):
        # initialise browser and get URL
        self.wd = self.init_wd()
        self.wd.get(URL)

        #accepting terms
        cookie = {'name': 'agreed', 'value': '1'}
        self.wd.add_cookie(cookie)
        self.wd.refresh()

    def tearDown(self):
        # close driver and quit
        self.wd.close()
        self.wd.quit()

    def testFirstContactForm(self):
        self.if_send('//*[@id="name"]', 'Test')
        self.if_send('//*[@id="age"]', '19')
        self.if_send('//*[@id="email"]', 'test@test.com')
        self.if_send('//*[@id="phone"]', '01234567890')

        self.if_click('//*[@id="toSetupTime"]')
        self.if_send('//*[@id="date"]', '07/04/2019')
        self.if_send('//*[@id="message"]', 'Message Test')

        self.if_click('//*[@id="send-advanced-message"]') #sending off details button commented out not to spam user
        #captcha here, need to disable

    def testSecondContactForm(self):
        self.if_click('//*[@id="leo-element-view"]/div[5]/div/div/div[2]/div[2]/div[2]/div/div[3]/strong/a/span')
        #captcha here, need to disable

if __name__ == '__main__':
    unittest.main()