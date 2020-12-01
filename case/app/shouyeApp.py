import os
import unittest
import time
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction##########触屏操作
from selenium.webdriver.support.ui import WebDriverWait####################toast
from selenium.webdriver.support import expected_conditions as EC###########toast

# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

class AndroidTests(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'###########################平台
        desired_caps['platformVersion'] = '5.1'#########################版本号
        desired_caps['deviceName'] = 'Android Emulator'##################手机名
        desired_caps['noReset'] = "True"#####################不清空app数据##########noReset值true
        #desired_caps['fullReset'] = "True"############清空app数据（卸载再安装）#####fullReset值true
        #desired_caps['app'] = PATH('E:/zuiyou518.apk')########APK路径#############路径+APK名
        #desired_caps['reseKeyboard'] = "True"#################重置输入法========输入中文需要
        #desired_caps['unicodeKeyboard'] = "True"###默认给手机安装appium输入法==输入中文需要
        desired_caps['appPackage'] = "cn.xiaochuankeji.tieba"############包名
        desired_caps['appActivity'] = ".ui.base.SplashActivity"##########页面
        desired_caps['automationName'] = "Uiautomator2"################处理toast
        desired_caps['newCommandTimeout'] = 200
        # #########最右账号：15127409611 密码：a123456

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def tearDown(self):
        #self.driver.quit()
        pass



    def testshouye01_01(self):
        '''验证首页导航栏文案显示是否正常'''
        self.driver.implicitly_wait(30)
        self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/home_item").click()
        self.driver.implicitly_wait(30)
        navText = self.driver.find_elements_by_id("cn.xiaochuankeji.tieba:id/title")
        self.assertEqual(navText[0].text,"关注")
        self.assertEqual(navText[1].text, "推荐")
        self.assertEqual(navText[2].text, "视频")
        self.assertEqual(navText[3].text, "图文")


    def testshouye01_02(self):
        '''验证帖子列表内容跳转'''
        self.driver.implicitly_wait(30)
        aa = self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/expand_content_view")
        bb = aa.text
        aa.click()
        self.driver.implicitly_wait(30)
        forumDetailText = self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/tvTitle")
        cc = self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/ss")
        self.assertEqual(forumDetailText.text,"帖子详情")
        self.assertEqual(bb,cc.text)

#######
    def testshouye01_03(self):
        '''验证评论帖子功能'''
        self.driver.implicitly_wait(30)
        self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/iconTabItem").click()
        self.driver.implicitly_wait(30)
        self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/expand_content_view").click()
        self.driver.implicitly_wait(30)
        self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/etInput").send_keys("text很好")
        self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/send").click()
        sendContent = self.driver.find_elements_by_id("cn.xiaochuankeji.tieba:id/expandTextView")
        sendContentRawList = []
        for i in range(0, len(sendContent)):
            sendContentRawList.append(sendContent[i].text)
        sendContentList = "".join(sendContentRawList)
        self.assertIn("text很好", sendContentList)

  


    def testredian02_04(self):
        '''查看实时热点展示'''
        self.driver.implicitly_wait(30)
        self.driver.find_element_by_xpath("//android.widget.ImageView[@resource-id='cn.xiaochuankeji.tieba:id/ic_search_b']").click()
        self.driver.implicitly_wait(30)
        lst=self.driver.find_elements_by_class_name("android.widget.TextView")
        global list_1
        list_1={}
        for n in range(3,12):
            print('第{}个'.format(n-2),lst[n].text)
            list_1[n]=lst[n].text
        print(list_1)
    

    def testtiezi03_01(self):
        '''查看发帖子功能'''
        self.driver.implicitly_wait(30)
        self.driver.find_element_by_xpath("//android.widget.FrameLayout[@resource-id='cn.xiaochuankeji.tieba:id/publish_item']/android.widget.ImageView[1]").click()
        self.driver.implicitly_wait(30)
        self.driver.find_element_by_xpath("//android.widget.TextView[@resource-id='cn.xiaochuankeji.tieba:id/selected_topic']").click()
        self.driver.implicitly_wait(30)
        self.driver.find_element_by_xpath("//android.widget.TextView[@resource-id='cn.xiaochuankeji.tieba:id/topic_title_tv']").click()
        time.sleep(1)
        ele=self.driver.find_element_by_xpath("//android.widget.EditText[@resource-id='cn.xiaochuankeji.tieba:id/etContent']")

        now = time.strftime('%Y-%m-%d-%H_%M_%S', time.localtime(time.time()))
        #day = time.strftime('%Y-%m-%d', time.localtime(time.time()))
        a=str(now)
        ele.send_keys(a)

        self.driver.implicitly_wait(30)
        self.driver.find_element_by_xpath("//android.widget.TextView[@resource-id='cn.xiaochuankeji.tieba:id/try_publish']").click()##发布
        self.driver.implicitly_wait(30)
        self.driver.find_element_by_xpath("//android.view.View[@resource-id='cn.xiaochuankeji.tieba:id/me_item']/android.widget.ImageView[1]").click()#####点击我的
        self.driver.implicitly_wait(30)
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='我的帖子']").click()
        self.driver.implicitly_wait(30)
        ele_1=self.driver.find_element_by_xpath("//android.widget.TextView[@resource-id='cn.xiaochuankeji.tieba:id/expand_content_view']")
        self.assertIn(a,ele_1.text)
    
    def testtiezi03_02(self):
        '''删除帖子'''
        self.driver.implicitly_wait(30)
        self.driver.find_element_by_xpath("//android.view.View[@resource-id='cn.xiaochuankeji.tieba:id/me_item']/android.widget.ImageView[1]").click()#####点击我的
        self.driver.implicitly_wait(30)
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='我的帖子']").click()
        self.driver.implicitly_wait(30)
        #lst=self.driver.find_elements_by_xpath("//android.widget.TextView[@resource-id='cn.xiaochuankeji.tieba:id/expand_content_view']")
        ele=self.driver.find_elements_by_xpath("//android.widget.TextView[@resource-id='cn.xiaochuankeji.tieba:id/expand_content_view']")
        ele[0].click()
        self.driver.implicitly_wait(30)
        self.driver.find_element_by_xpath("//android.widget.ImageView[@resource-id='cn.xiaochuankeji.tieba:id/ivOption']").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//android.widget.LinearLayout[@resource-id='cn.xiaochuankeji.tieba:id/second_option_container']/android.widget.RelativeLayout[2]/android.widget.ImageView[1]").click()
        self.driver.find_element_by_xpath("//android.widget.TextView[@resource-id='cn.xiaochuankeji.tieba:id/bt_positive']").click()
        self.driver.implicitly_wait(60)
        a=('xpath',".//*[contains(@text,'删除成功')]")
        aa=WebDriverWait(self.driver,20,0.1).until(EC.presence_of_element_located(a))

        KJ=("xpath",'.//*[contains(@text,"删除成功")]')
        el=WebDriverWait(self.driver,20,0.1).until(EC.presence_of_element_located(KJ))
        #print(aa.text)
        #self.assertIn('删除成功',aa.text)
        print(el.text)
        self.assertIn('删除成功',el.text)



    def test_swipe03_03(self):
        self.driver.implicitly_wait(30)
        ele=self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/title")
        time.sleep(5)
        self.driver.swipe(500,1000,500,200,3000)####滑动开始坐标（500,1000），结束坐标（500,200），持续3秒
        # self.driver.swipe(500,200,500,200,100)###########实现点击0.1秒
        # self.driver.swipe(500,200,500,200,3000)##########实现长按3秒


        ######获取手机分辨率
        H=self.driver.get_window_size()['height']
        W=self.driver.get_window_size()['width']
        print(H,W)
        self.driver.swipe(W*0.5,H*0.8,W*0.5,H*0.2,3000)############按照比例滑动，可以适配各种分辨路手机
        self.driver.swipe(W*0.89,H*0.5,W*0.1,H*0.5,500)


if __name__ == "__main__":
    unittest.main()