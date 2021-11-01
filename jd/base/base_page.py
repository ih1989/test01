class Basepage():
    def __init__(self,driver):
        self.driver=driver

    def get_url(self,url):
        self.driver.get(url)

    def find_ele(self,*str):
        self.driver.find_element(*str)

    #输入
    def input_text(self,str,text):
        self.driver.find_element(*str).send_keys(text)

    #点击
    def click_(self,str):
        self.driver.find_element(*str).click()

    #滚动
    def gd(self):
        self.js='window.scrollTo(0,500)'
        return  self.driver.execute_script(self.js)

    #页面切换
    def qiehuan(self):
        return  self.driver.switch_to.window(self.driver.window_handles[-1])
