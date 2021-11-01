from jd.page.jd_page import *
from selenium import webdriver
from time import  time
import unittest
class mytest(unittest.TestCase):
    def setUp(self) -> None:
        pass
    def tearDown(self) -> None:
        pass

    @classmethod
    def setUpClass(cls) -> None:
        # pass
        cls.driver=webdriver.Chrome('../../chromedriver.exe')
        cls.driver.get('https://www.jd.com/')
        cls.driver.implicitly_wait(8)
        cls.driver.maximize_window()
        sleep(2)




    @classmethod
    def tearDownClass(cls) -> None:
        # pass
        cls.driver.quit()

    def test_001(self):
        Jdpage(self.driver).jd()
        # print('l')
        # self.assertNotIn('https://trade.jd.com/',Jdpage.aa)


if __name__ == '__main__':
    unittest.main()