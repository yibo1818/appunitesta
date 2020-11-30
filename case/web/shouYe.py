# coding=utf-8
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from public.login import Mylogin
from public.houshou import houjinshou
import unittest
import os
import time

class TestShouye(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://101.133.169.100/yuns/index.php/admin/index/index")
        self.driver.maximize_window()
        time.sleep(5)
        print("starttime:" + time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time())))

    def tearDown(self):
        filedir = "D:/test/screenshot/"
        if not os.path.exists(filedir):
            os.makedirs(os.path.join('D:/', 'test', 'screenshot'))
        print("endTime:" + time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time())))
        screen_name = filedir + time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time())) + ".png"
        self.driver.get_screenshot_as_file(screen_name)
        self.driver.quit()


    def testShouye01_01(self):
        '''测试首页导航文案显示是否正常'''
        houjinshou(self.driver).houshou()
        firstPageNavi = self.driver.find_element_by_xpath("//div[@class='top']/span")
        loginText = self.driver.find_element_by_css_selector("div.login>a:nth-child(1)")
        regisText = self.driver.find_element_by_css_selector("div.login>a:nth-child(3)")

        self.assertEqual("亲，欢迎您来到云商系统商城！",firstPageNavi.text)
        self.assertEqual("17731990979", loginText.text)
        self.assertEqual("退出", regisText.text)
        self.assertNotEqual("dd", regisText.text)

        self.assertIn("云商系统商城",firstPageNavi.text)

        self.assertTrue(self.driver.find_element_by_xpath("//div[@class='top']/span").is_displayed())
        self.assertFalse(firstPageNavi.is_displayed())

        if loginText.text == "177****0979":
            print("等于")
        else:
            print("不等于")
            self.driver.find_element_by_xpath("王麻子")



    def testShouye01_02(self):
        '''验证搜索内容无时，提示语是否正常'''
        houjinshou(self.driver).houshou()
        self.driver.find_element_by_xpath("/html/body/div/div/div/div/form/input[1]").send_keys("王麻子")
        self.driver.find_element_by_xpath("/html/body/div/div/div/div/form/input[2]").click()
        time.sleep(2)
        searchText = self.driver.find_element_by_xpath("//div[@class='nomsg']")
        self.assertEqual(searchText.text, "抱歉，没有找到相关的商品")


    def testShouye01_03(self):
        '''查看商品名在浏览页，详情页，购物车页是否一致'''
        houjinshou(self.driver).houshou()
        aa=self.driver.find_element_by_xpath("//div[@style='display:block;']/dl[1]/dt/div/span/a")
        ActionChains(self.driver).move_to_element(aa).perform()    ###########鼠标移动到该控件
        self.driver.find_element_by_xpath("//div[@style='display:block;']/dl[1]/div/div[5]/div/a").click()
        time.sleep(2)
        L=self.driver.find_element_by_xpath("//div[@class='goodsbox']/div[1]/div[3]/div[2]/a").text  #########获取商品名文本信息
        self.driver.find_element_by_xpath("//div[@class='goodsbox']/div[1]").click()
        self.driver.switch_to.window(self.driver.window_handles[1])##############焦点进入新页面
        K=self.driver.find_element_by_xpath("//div[@class='info']/h1").text #####################################获取商品详情页商品名称
        self.driver.find_element_by_xpath("//div[@class='sku_box']/dl[1]/dd/a").click()
        self.driver.find_element_by_xpath("//div[@class='sku_box']/dl[2]/dd/a").click()
        self.driver.find_element_by_xpath("//div[@class='info']/div[4]/div/input[@size='2']").clear()
        self.driver.find_element_by_xpath("//div[@class='info']/div[4]/div/input[@size='2']").send_keys("3")
        self.driver.find_element_by_xpath("//div[@class='con buy_action']/div[2]/a[1]").click()################加入购物车
        time.sleep(2)
        self.driver.find_element_by_xpath("//div[@class='buy_tip']/div[2]/a[1]").click()####################点击弹出的“去付款”进入购物车

        J=self.driver.find_element_by_xpath("//div[@class='ttl']/div[@class='sttl']/a").text###################获取购物车商品名信息
        print(L,K,J)
        self.assertEqual(K,J)
        self.assertIn(L,K)









if __name__ == "__main__":
    unittest.main()


