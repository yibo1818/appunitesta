import time

class Mylogin(object):
    def __init__(self, driver):
        self.driver = driver

    def login(self):
        self.driver.implicitly_wait(60)
        self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/me_item").click()
        time.sleep(2)
        self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/tv_notLogin_goLogin").click()
        time.sleep(1)
        self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/login_mode").click()
        self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/phone_num_edit").send_keys("15127409611")
        self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/code_edit").send_keys("a123456")
        self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/login").click()
        time.sleep(5)
            
            


            
    