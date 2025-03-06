import os
from datetime import datetime

import pytesseract
from PIL import Image
from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait

from config import setting
from util_tools.handle_data.configParse import ConfigParse
from util_tools.logs_util.recordlog import logs


class BasePage(object):
    """
    封装浏览器的一些操作，对象webDriver里面的一些方法进行二次开发
    此类封装所有的操作，所有页面继承该类
    """

    def __init__(self, driver):
        # 浏览器对象初始化
        self.__driver = driver
        # 显示等待初始化
        self.__wait = WebDriverWait(self.__driver, setting.WAIT_TIME)
        self.conf = ConfigParse()

    def window_max(self):
        """浏览器窗口最大化"""
        self.__driver.maximize_window()

    def window_full(self):
        """全屏窗口"""
        self.__driver.fullscreen_window()

    def screenshot(self):
        """浏览器截屏"""
        self.__driver.get_screenshot_as_png()

    def refresh(self):
        """页面刷新"""
        self.__driver.refresh()

    def scroll_to_button(self):
        """
        使用JavaScript滚动页面到最底部
        :return:
        """
        self.__driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")

    @property
    def current_url(self):
        """获取当前页面的URL"""
        return self.__driver.current_url

    @property
    def title(self, ):
        """获取页面标题"""
        return self.__driver.title

    def open_url(self, url):
        """打开测试页面"""
        if url.startswith('http') or url.startswith('https'):
            self.__driver.get(url)
            logs.info(f'打开页面：{url}')
        else:
            new_url = self.conf.get_host('host') + url
            self.__driver.get(new_url)
            logs.info(f'打开页面：{new_url}')

    def get_tag_text(self, locator: tuple):
        """获取页面标签文本内容"""
        try:
            element = self.location_element(*locator)
            element_text = element.text
            logs.info(f'获取标签文本内容：{element_text}')
            return element_text
        except Exception as e:
            logs.error(f'获取标签文本内容出现异常，{str(e)}')

    @property
    def switch_to(self):
        """切换switch_to"""
        return self.__driver.switch_to

    def iframe(self, frame):
        """切换到iframe内联框架中"""
        try:
            self.switch_to.frame(frame)
            logs.info(f'切换到{frame}--iframe内部框架中')
        except:
            logs.error('切换iframe框架失败！')

    def switch_to_new_tab(self):
        """浏览器打开新的标签页，切换窗口句柄"""
        try:
            original_window = self.__driver.window_handles[0]  # 获取当前窗口的句柄作为原始窗口
            all_window = self.__driver.window_handles  # 获取所有窗口的句柄列表
            new_window = None
            for window in all_window:
                if window != original_window:  # 找到不等于原始窗口句柄的新窗口句柄
                    new_window = window
                    break

            if new_window:
                self.switch_to.window(new_window)  # 切换到新窗口，以便在新窗口上执行后续操作
                logs.info('成功切换到新标签页')
        except TimeoutException:
            logs.error('等待新标签打开超时')
        except NoSuchElementException:
            logs.error('未找到新标签页句柄')
        except Exception as e:
            logs.error(f'切换窗口时发生异常：{str(e)}')

    def switch_to_tab_by_index(self, index):
        """
        当需要切换多个标签页时
        :param index: 标签页的索引，从0开始
        :return:
        """
        try:
            all_window = self.__driver.window_handles  # 获取所有窗口的句柄列表
            if 0 <= index < len(all_window):
                target_window = all_window[index]  # 获取目标窗口句柄
                self.switch_to.window(target_window)  # 切换到目标窗口
                logs.info(f'成功切换到第{index + 1}个标签页')
            else:
                logs.error('指定的窗口索引超出范围')
        except Exception as e:
            logs.error(f'切换窗口时发生异常：{str(e)}')

    def exit_iframe(self):
        """退出iframe框架"""
        self.switch_to.default_content()

    @property
    def alert(self):
        """alert弹框处理"""
        return self.__wait.until(ec.alert_is_present())  # 等待直到页面上出现弹框，存在就返回Alert对象，不存在就返回False

    def alert_confirm(self):
        """点击alert弹框中确定操作"""
        self.alert.accept()

    def alert_cancel(self):
        """点击alert弹框中取消操作"""
        self.alert.dismiss()

    def location_element(self, by, value):
        """
        二次封装find_element方法，定位页面元素
        :param by: 定位方式，比如By.ID，By.XPATH
        :param value: 定位表达式
        :return:
        """
        try:
            element = self.__wait.until(ec.presence_of_element_located((by, value)))
            logs.info(f"找到元素：{by} = {value}")
            return element
        except Exception as e:
            logs.error(f"未找到元素：{by} = {value}")
            raise e

    def location_elements(self, by, value):
        """
        二次封装find_elements方法，定位页面元素列表
        :param by: 定位方式，比如By.ID，By.XPATH
        :param value: 定位表达式
        :return:
        """
        try:
            self.__wait.until(ec.presence_of_all_elements_located((by, value)))
            elements = self.__driver.find_elements(by, value)
            logs.info(f"找到元素列表：{by} = {value}")
            return elements
        except Exception as e:
            logs.error(f"未找到元素列表：{by} = {value}")
            raise e

    def visibility_of_element_located(self, by, value):
        """
        等待元素可见性
        :param by:
        :param value:
        :return:
        """
        try:
            element = self.__wait.until(ec.visibility_of_element_located((by, value)))
            logs.info(f"找到元素：{by} = {value}")
            return element
        except Exception as e:
            logs.error(f"在设定时间内未找到元素：{by} = {value}")
            raise e

    def click(self, locator: tuple, force=False):
        """
        封装点击操作
        :param locator: （tuple）定位元素信息，等于(By.ID,'j_idt88:j_idt93')
        :param force: 可选参数，表示是否使用强制点击，默认为False
        :return:
        """
        try:
            element = self.location_element(*locator)
            if not force:
                self.__driver.execute_script("arguments[0].click()", element)
            else:
                self.__driver.execute_script("arguments[0].click({force:true})", element)
            logs.info(f"元素被点击：{locator}")
        except NoSuchElementException as e:
            logs.error(f"元素无法定位：{e}")
            raise e

    def click_actions(self, locator: tuple):
        """
        封装模拟鼠标点击操作
        :param locator: （tuple）定位元素信息，等于(By.ID,'j_idt88:j_idt93')
        :return:
        """
        element = self.visibility_of_element_located(*locator)
        ActionChains(self.__driver).click(element).perform()

    def send_keys(self, locator: tuple, data):
        """
        封装输入操作，对send_keys方法进行二次封装
        :param locator: （tuple）定位元素信息，等于(By.ID,'j_idt88:j_idt93')
        :param data: 输入的内容
        :return:
        """
        try:
            element = self.location_element(*locator)
            element.send_keys(data)
            logs.info(f"元素被输入内容：{locator}，输入的内容为：{data}")
        except NoSuchElementException as e:
            logs.error(f"元素无法定位：{e}")
            raise e

    def send_keys_actions(self, locator: tuple, data):
        """
        模拟键盘的输入操作
        :param locator: （tuple）定位元素信息，等于(By.ID,'j_idt88:j_idt93')
        :param data: 输入的内容
        :return:
        """
        try:
            element = self.location_element(*locator)
            ActionChains(self.__driver).move_to_element(element).click().send_keys(data).perform()
            logs.info(f"元素被输入内容：{locator}，输入的内容为：{data}")
        except NoSuchElementException as e:
            logs.error(f"元素无法定位：{e}")
            raise e

    def selects(self, locator: tuple, index):
        """
        封装下拉菜单选择
        :param locator: （tuple）定位元素信息
        :param index: 要选择的下拉选项
        :return:
        """
        try:
            select = Select(self.location_element(*locator))
            select.select_by_index(index)
            logs.info(f'选择下拉菜单第{index}条数据')
        except NoSuchElementException as e:
            logs.error(f"元素无法定位：{e}")
            raise e

    def enter(self):
        """
        封装键盘回车的操作
        :return:
        """
        try:
            ActionChains(self.__driver).send_keys(Keys.ENTER).perform()
            logs.info('按下回车键')
        except NoSuchElementException as e:
            logs.error(f"元素无法定位：{e}")
            raise e

    def right_click(self, locator: tuple):
        """
        封装右键点击操作
        :param locator: （tuple）定位页面元素
        :return:
        """
        try:
            element = self.location_element(*locator)
            ActionChains(self.__driver).context_click(element).perform()
            logs.info('执行右键点击操作')
        except NoSuchElementException as e:
            logs.error(f"元素无法定位：{e}")
            raise e

    def double_click(self, locator: tuple):
        """
        封装双击操作
        :param locator: （tuple）定位页面元素
        :return:
        """
        try:
            element = self.location_element(*locator)
            ActionChains(self.__driver).double_click(element).perform()
            logs.info('执行双击操作')
        except NoSuchElementException as e:
            logs.error(f"元素无法定位：{e}")
            raise e

    def mouse_hover_actions(self, locator: tuple):
        """
        封装鼠标悬停展示内容或弹框
        :param locator: （tuple）定位页面元素
        :return:
        """
        try:
            move_element = self.location_element(*locator)
            ActionChains(self.__driver).move_to_element(move_element).perform()
            logs.info('鼠标悬停')
        except Exception as e:
            logs.error(f"鼠标悬停出现异常：{e}")
            raise e

    def screenshots(self, image_name):
        """
        封装截图的方法
        :param image_name: 文件名
        :return:
        """
        current_time = datetime.now().strftime("%Y%m%d%H%M%S")  # 获取当前的时间
        file_name = f'{image_name}-{current_time}.png'
        file_path = os.path.join(setting.FILE_PATH.get('screenshot'), file_name)
        self.__driver.get_screenshot_as_file(file_path)

    def screenshots_png(self):
        """
        页面截屏，保存为PNG格式
        :return:
        """
        return self.__driver.get_screenshot_as_png()

    def clear(self, locator: tuple):
        """
        清空
        :param locator: 定位方式
        :return:
        """
        try:
            element = self.location_element(*locator)
            element.clear()
            logs.info('清空文本')
        except NoSuchElementException as e:
            logs.error(f"元素无法定位：{e}")
            raise e

    def ocr_captcha(self, locator: tuple):
        """
        1）定位到图形验证码，保存图片
        2）调用Image去打开图像
        3）调用pytesseract模块进行OCR识别
        :param locator: 定位方法和定位表达式，（tuple）元组
        :return:
        """
        captcha_element = self.location_element(*locator)
        # 截取图形验证码
        captcha_path = setting.FILE_PATH['screenshot'] + '/captcha.png'
        captcha_element.screenshot(captcha_path)
        # 调用Image去打开图像
        captcha_image = Image.open(captcha_path)
        try:
            # 调用pytesseract进行OCR识别
            captcha_text = pytesseract.image_to_string(captcha_image)
            logs.info(f'识别到的验证码为：{captcha_text}')
            return captcha_text
        except pytesseract.pytesseract.TesseractNotFoundError:
            logs.error("找不到tesseract,这是因为pytesseract模块依赖于TesseractOCR引擎来进行图像识别！")

    def is_element_present(self, locator: tuple):
        """判断元素是否存在"""
        try:
            self.__wait.until(ec.presence_of_element_located(*locator))
            return True
        except:
            logs.error(f'{locator}元素未找到或不存在')
            return False

    def assert_is_element_present(self, locator: tuple):
        """
        断言元素存在
        :param locator: 元素定位表达式
        :return:
        """
        try:
            element = self.__driver.find_element(*locator)
            assert element.is_displayed(), '元素不存在'
        except NoSuchElementException as e:
            logs.error(f'元素未找到，{e}')
            raise AssertionError('元素不存在')

    def assert_element_not_visible(self, locator: tuple):
        """
        断言元素不可见或不存在
        :param locator:
        :return:
        """
        try:
            self.__wait.until(ec.invisibility_of_element_located(locator))
        except TimeoutException:
            logs.error('元素可见')

    def assert_title(self, expect_title):
        """
        断言预期标题文本是否包含在实际文本页面的标题中
        :param expect_title: 预期文本标题
        :return:
        """
        assert expect_title in self.title

    def assert_element_to_be_clickable(self, locator: tuple):
        """
        断言元素是否可被点击操作
        :param locator: （tuple）元素定位表达式
        :return:
        """
        try:
            element = self.__wait.until(
                ec.element_to_be_clickable(locator)
            )
            # 执行断言或其他操作
            assert element.is_enabled(), "元素未启用交互"
            logs.info('断言结果：元素是可点击的，并且可以进行交互')
            # 例如，点击元素
            element.click()
        except Exception as e:
            logs.error(f"发生错误: {e}")

    def assert_alert_present(self):
        """
        断言页面是否出现alert弹框
        :return:
        """
        try:
            alert = self.__wait.until(ec.alert_is_present())
            return True
        except TimeoutException:
            return False
