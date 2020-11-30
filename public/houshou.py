import time
from selenium import webdriver

class houjinshou(object):
    def __init__(self, driver):
        self.driver = driver

    def houshou(self):

        time.sleep(3)
        self.driver.find_element_by_id("username").send_keys("admin")
        time.sleep(1)
        self.driver.find_element_by_id("password").send_keys("admin")
        self.driver.find_element_by_name("submit").click()
        time.sleep(2)

        self.driver.find_element_by_link_text("会员").click()
        time.sleep(2)
        #self.driver.find_element_by_id("content")
        self.driver.switch_to.frame("content")
        self.driver.find_element_by_xpath("//table[@class='ltable']/tbody/tr[1]/td/div/a").click()
        time.sleep(2)

        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])

        self.driver.find_element_by_xpath("//div[@class='img']/a/img").click()

        time.sleep(2)




