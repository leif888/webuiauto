from time import sleep

from selenium.webdriver.common.by import By

from util_tools.basePage import BasePage


class ZhiHuPage(BasePage):
    url = 'https://www.zhihu.com/signin'
    # 写文章按钮
    writes = (By.XPATH, '//*[text()="写文章"]')
    # 标题
    titles = (By.XPATH, '//*[@id="root"]/div/main/div/div[2]/div[2]/div[1]/label/textarea')
    # 多行文本内容
    contents = (By.CLASS_NAME, 'public-DraftEditorPlaceholder-root')

    def write_content(self):
        self.open_url(self.url)
        # 切换到新标签页面的窗口句柄中
        self.click(self.writes)
        sleep(1)
        self.switch_to_new_tab()
        self.send_keys(self.titles, 'labview控制系统')
        sleep(2)
        # self.send_keys(self.contents, '控制系统')
        content = """
        LabVIEW是一种程序开发环境，由美国国家仪器（NI）公司研制开发，类似于C和BASIC开发环境，但是LabVIEW与其他计算机语言的显著区别是：
        其他计算机语言都是采用基于文本的语言产生代码，而LabVIEW使用的是图形化编辑语言G编写程序，产生的程序是框图的形式。
        """
        self.send_keys_actions(self.contents, content)
        self.scroll_to_button()
        sleep(5)
