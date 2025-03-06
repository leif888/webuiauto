from time import sleep
from selenium.webdriver.common.by import By
from util_tools.basePage import BasePage


class CSDNPage(BasePage):
    url = 'https://passport.csdn.net/login'
    # 发布
    publish = (By.XPATH, '//*[@id="csdn-toolbar"]/div/div/div[3]/div/div[6]/a')
    # 写文章按钮
    write_publish_button = (By.XPATH, '//*[@id="csdn-toolbar-write"]/div/ul/li[1]/a/i')
    # 弹框模板库
    mode_alert = (By.CLASS_NAME, 'modal__inner-2')
    cancel_button = (By.XPATH, '//*[@id="reset_inner"]/div/div[6]/div[4]/div[1]')
    # 使用富文本编辑器按钮
    rich_text_button = (By.XPATH, '/html/body/div[1]/div[1]/div[2]/div/div[1]/nav/div[2]/div[1]/div[30]/button')
    # 输入标题
    rich_input_title = (By.CLASS_NAME, 'el-textarea__inner')
    # 输入正文内容
    rich_input_content = (By.CSS_SELECTOR, 'body')
    # 插入图片
    rich_images_button = (By.XPATH, '//*[text()="图像"]')
    # 上传图片
    rich_upload_images = (By.CLASS_NAME, 'el-upload__input')
    # 发布文章
    publish_button = (By.XPATH, '/html/body/div[1]/div[1]/div[1]/div/div[3]/button[2]')
    # 添加文章标签
    rich_article_tag = (By.XPATH, '//*[@id="moreDiv"]/div[1]/div/div/div[1]/button')
    # 添加标签输入
    rich_article_input = (By.XPATH, '//*[@id="moreDiv"]/div[1]/div/div/div[2]/div[2]/div/div[1]/input')
    # 选择搜索标签结果
    rich_choice_tag_result = (By.XPATH, '//*[@id="el-autocomplete-9266-item-0"]')
    # 最终发布文章
    rich_last_publish_article_button = (By.XPATH, '//*[@id="moreDiv"]/div[9]/div/div/div[2]/button[2]/span')

    def publish_an_article(self):
        self.open_url(self.url)
        sleep(10)
        self.mouse_hover_actions(self.publish)
        sleep(3)
        self.click(self.write_publish_button)
        # self.switch_to_new_tab()
        self.switch_to_tab_by_index(1)
        sleep(2)
        if self.visibility_of_element_located(*self.cancel_button) is not None:
            self.click_actions(self.cancel_button)
        sleep(2)
        self.click_actions(self.rich_text_button)
        # self.switch_to_new_tab()
        self.switch_to_tab_by_index(2)
        sleep(4)
        self.clear(self.rich_input_title)
        self.send_keys_actions(self.rich_input_title, 'LabVIEW开发LED驱动电源测试系统')
        sleep(2)
        self.send_keys_actions(self.rich_input_content, '电源测试系统')
        sleep(5)
        self.scroll_to_button()
