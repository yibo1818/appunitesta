# aa ="交易号：2020111619171747090"
# bb = aa.split("：")  #################拆分“交易号：2020111619171747090”，号码赋值给bb
# print(aa)
# print(bb[1])
import time

    # self.driver.implicitly_wait(30)
    # self.driver.find_element_by_xpath(
    #     "//android.widget.FrameLayout[@resource-id='cn.xiaochuankeji.tieba:id/publish_item']/android.widget.ImageView[1]").click()
    # self.driver.implicitly_wait(30)
    # ele = self.driver.find_element_by_xpath(
    #     "//android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]")
now = time.strftime('%Y-%m-%d-%H_%M_%S', time.localtime(time.time()))
day = time.strftime('%Y-%m-%d', time.localtime(time.time()))
a = str(now)
print(a)