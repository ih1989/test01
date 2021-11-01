from jd.base.base_page import *
from selenium.webdriver.common.by import By
from time import  sleep

class   Jdpage(Basepage):
    aa=''
    input_=(By.XPATH,'//*[@id="key"]')#搜索框输入
    ss_click=(By.XPATH,'//*[@id="search"]/div/div[2]/button')#搜索按钮
    kouhong=(By.XPATH,'//*[@id="J_selector"]/div[1]/div/div[2]/div[1]/ul/li[2]/a')#口红
    sp=(By.XPATH,'//*[@id="J_goodsList"]/ul/li[1]/div/div[3]/a/em')#选择商品
    gwc=(By.XPATH,'//*[@id="InitCartUrl"]')#加入购物车
    qjs=(By.XPATH,'//*[@id="GotoShoppingCart"]')#去购物车结算
    gouxuansp=(By.XPATH,'//*[@id="cart-body"]/div[1]/div[4]/div[1]/div/input')#选择购物车商品
    jiesuan=(By.XPATH,'//*[@id="cart-body"]/div[1]/div[8]/div/div[2]/div/div/div/div[2]/div[2]/div/div[1]/a')#点击结算




    def jd(self):
       self.input_text(self.input_,'花西子')
       sleep(2)
       self.click_(self.ss_click)
       sleep(2)

       self.click_(self.kouhong)
       sleep(2)

       self.gd()#滚动
       sleep(2)

       self.click_(self.sp)
       sleep(2)

       self.qiehuan()#句柄切换
       sleep(2)


       self.click_(self.gwc)#加入购物车
       sleep(20)
       self.click_(self.qjs)#去购物车结算
       sleep(1)
       self.click_(self.gouxuansp)#选择购物车商品
       sleep(1)
       self.click_(self.jiesuan)##点击结算
       sleep(1)


       self.aa=self.driver.current_url
       print(self.aa)


