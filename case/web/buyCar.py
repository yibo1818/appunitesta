# coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ppp
import unittest
import os
import time
from public.login import Mylogin        ########################封装的完成登录的class，直接调用可以不用登录
from public.houshou import houjinshou
class Gouwuche(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://101.133.169.100/yuns/index.php/admin/index/index")
        self.driver.maximize_window()
        time.sleep(3)

    def tearDown(self):
        filedir = "D:/test/screenshot/"
        if not os.path.exists(filedir):
            os.makedirs(os.path.join('D:/', 'test', 'screenshot'))
        screen_name = filedir + time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time())) + ".png"
        self.driver.get_screenshot_as_file(screen_name)
        self.driver.quit()


    def testGouwu01_04(self):
        '''购物车为空时文案显示是否正常'''
        houjinshou(self.driver).houshou()                 ########################直接调用登录函数
        self.driver.find_element_by_xpath("//div[@class='small_cart_name']/span").click()
        time.sleep(3)
        emptyGouwuText = self.driver.find_element_by_xpath("//div[@class='r']/span")
        print(emptyGouwuText.text)
        self.assertEqual("购物车内暂时没有商品",emptyGouwuText.text)


    def testGouwu01_05(self):
        '''付款后查看我的订单是否一致'''
        houjinshou(self.driver).houshou()
        self.driver.find_element_by_xpath("//div[@class='sch']/div/form/input[1]").send_keys("女装")
        self.driver.find_element_by_xpath("//div[@class='sch']/div/form/input[2]").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//div[@class='goodsbox']/div[1]").click()
        time.sleep(2)
        self.driver.switch_to.window(self.driver.window_handles[1])  ##############焦点进入新页面

        self.driver.find_element_by_xpath("//div[@class='sku_box']/dl[1]/dd/a[2]").click()
        self.driver.find_element_by_xpath("//div[@class='sku_box']/dl[2]/dd/a").click()
        self.driver.find_element_by_xpath("//div[@class='info']/div[4]/div/input[@size='2']").clear()
        self.driver.find_element_by_xpath("//div[@class='info']/div[4]/div/input[@size='2']").send_keys("2")
        self.driver.find_element_by_xpath("//div[@class='con buy_action']/div[2]/a[1]").click()################加入购物车
        time.sleep(2)
        self.driver.find_element_by_xpath("//div[@class='buy_tip']/div[2]/a[1]").click()####################点击弹出的“去付款”进入购物车
        time.sleep(2)
        self.driver.find_element_by_xpath("//div[@class='cart_pay']/div/input").click() ####################点击去结算
        time.sleep(1)
        self.driver.find_element_by_xpath("//input[@type='radio']").click()#################################选择收货地址
        self.driver.find_element_by_xpath("//input[@type='submit']").click()################################点击下单支付
        time.sleep(1)
        self.driver.find_element_by_xpath("//div[@class='con']/div[3]").click()#############################选择余额支付
        self.driver.find_element_by_xpath("//div[@class='lbox']/div[4]/a").click()##########################点击确认支付
        time.sleep(2)
        #aa=self.driver.find_element_by_xpath("//div[@class='opr'][1]/div[1]").text##########################获取订单号
        #bb=aa.split("：")#################拆分“交易号：2020111619171747090”，号码赋值给bb
        self.driver.find_element_by_xpath("//div[@class='logout']/a[1]").click()
        time.sleep(0.5)
        self.driver.find_element_by_xpath("//div[@class='help']/a[2]").click()#######################进入我的订单
        aa=self.driver.find_element_by_xpath("//table/tbody[2]/tr//td/span[1][@class='order_span']").text##########################获取订单号
        global bb
        bb= aa.split("：")#################拆分“交易号：2020111619171747090”，号码赋值给bb

        self.driver.switch_to.window(self.driver.window_handles[0])  #######################################焦点进入之前页面
        time.sleep(3)

        self.driver.get("http://101.133.169.100/yuns/index.php/admin/index/index")####################登录后台账号
        #self.driver.find_element_by_id("username").send_keys("admin")
        #self.driver.find_element_by_id("password").send_keys("admin")
        #self.driver.find_element_by_name("submit").click()
        time.sleep(3)
        self.driver.find_element_by_xpath("//div/ul/a[2]").click()
        time.sleep(3)
        self.driver.switch_to.frame("content")#############################################切入ifarme
        self.driver.find_element_by_xpath("//form/div/input[1]").send_keys(bb[1])
        self.driver.find_element_by_xpath("//form/div/input[2]").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//div[@class='main']/table/tbody/tr[3]/td[8]/a[1]").click()
        time.sleep(0.5)
        self.driver.find_element_by_link_text("确认线下支付").click()
        self.driver.switch_to.window(self.driver.window_handles[1])  #######################################焦点回到客户端页面
        time.sleep(2)
        self.driver.find_element_by_xpath("//div[@class='logo']/div/a/img").click()#######################回到首页
        self.driver.find_element_by_xpath("//div[@class='help']/a[2]").click()#######################进入我的订单
        time.sleep(5)
        self.driver.find_element_by_xpath("//div[@class='con_tab']/a[3]").click()#####################进入待发货
        hh=self.driver.find_element_by_xpath("/html/body/div[3]/div/div/div[2]/div[2]/table/tbody[2]/tr[1]/td/span[1]").text####################################################查找订单号
        print(aa)
        print(bb,bb[1])
        print(hh)
        self.assertEqual(aa,hh)
        return bb


    def testWuliu01_06(self):
        '''后台发货'''
        self.driver.find_element_by_id("username").send_keys("admin")
        self.driver.find_element_by_id("password").send_keys("admin")
        self.driver.find_element_by_name("submit").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//div/ul/a[2]").click()
        time.sleep(3)
        self.driver.switch_to.frame("content")#############################################切入ifarme

        self.driver.find_element_by_xpath("//form/div/input[1]").send_keys(bb[1])
        self.driver.find_element_by_xpath("//form/div/input[2]").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//div[@class='main']/table/tbody/tr[3]/td[8]/a[1]").click()
        time.sleep(0.5)
        a=self.driver.find_element_by_name("kd_code")
        Select(a).select_by_visible_text("申通速递")
        self.driver.find_element_by_xpath("//form/dl[2]/dd/input").send_keys(bb[1])
        self.driver.find_element_by_xpath("//form/dl[3]/dd/input").click()
        #ele=WebDriverWait(self.driver,5,0.5).until(ppp.presence_of_element_located((By.XPATH,"//div[@class='com_box']/span")))
        #self.driver.implicitly_wait(5)
        #ele=self.driver.find_element_by_xpath("//div[@class='com_box']").text
        #zz=ele.text
        #print(ele)


    def testShouPing01_07(self):
        '''收货并且评价'''
        houjinshou(self).houshou()
        time.sleep(2)
        self.driver.find_element_by_xpath("//div[@class='help']/a[2]").click()#######################进入我的订单
        self.driver.find_element_by_xpath("//tbody[2]/tr/td[7]").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//div[@class='act']/a").click()
        time.sleep(2)
        self.driver.switch_to.alert.accept()
        time.sleep(2)
        self.driver.switch_to.alert.accept()
        time.sleep(1)
        self.driver.find_element_by_xpath("//div[@class='logo']/div/a/img").click()#######################回到首页
        self.driver.find_element_by_xpath("//div[@class='help']/a[2]").click()#######################进入我的订单
        self.driver.find_element_by_link_text("商品评价").click()
        self.driver.find_element_by_xpath("//img[@title='gorgeous']").click()#######################点五星
        self.driver.find_element_by_xpath("// textarea").send_keys("我很美，更美了")#######################评价
        self.driver.find_element_by_xpath("//div[@class='sub']/input").click()#####################提交评价
        time.sleep(2)
        self.driver.switch_to.alert.accept()
























if __name__ == "__main__":
    unittest.main()


