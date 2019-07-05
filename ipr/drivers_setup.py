# This class allows Selenium tests to either be run:
# - headless chrome browser localy (chrome browser driver has to be installed before)
# - run tests remotely in BrowserStack on iPhone 8 Plus

import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

CHROME_DRIVER_PATH = os.environ.get('CHROME_DRIVER_PATH','/usr/local/bin/chromedriver')
#To change browser used, write this in console:
#export BTEST_DRIVER=HCHROME
#export BTEST_DRIVER=BROWSERSTACK

#Selenium support for PhantomJS has been deprecated, default now will be headless chrome
DRIVER = os.environ.get('BTEST_DRIVER', 'HCHROME')
BROWSERSTACK_LINK = os.environ.get('BROWSERSTACK_LINK', 'HCHROME')

class SeleniumObject(object):

  def init_wd(self):
    print('Driver is %s' % DRIVER)

    if DRIVER == 'HCHROME' or BROWSERSTACK_LINK == 'HCHROME':
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        wd = webdriver.Chrome(CHROME_DRIVER_PATH, options=chrome_options)
        wd.set_window_size(480, 800)
    elif DRIVER == 'BROWSERSTACK':
        desired_cap = {
            'browserName': 'iPhone',
            'device': 'iPhone 8 Plus',
            'realMobile': 'true',
            'os_version': '11',
            'name': 'Bstack-[Python] Sample Test'
        }
        wd = webdriver.Remote(
            command_executor=BROWSERSTACK_LINK,
            desired_capabilities=desired_cap)

    return wd