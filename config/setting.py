import os
import sys

# 获取当前项目的根目录，并将该目录添加到python模块搜索路径中
DIR_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(DIR_PATH)

# 隐示等待时间设置，默认为10s
WAIT_TIME = 10

# 设置浏览器
browser_type = 'edge'

# 钉钉机器人
secret = "SECb163daa45904540212492d8ad7bf7c3ce428fae5211c2e94b1f0926be0778191"
webhook = "https://oapi.dingtalk.com/robot/send?access_token=df849617e1f9593fd9c31f75ce4fdf2fea8fec39c7b714a65f20413444f5cea5"
# 设置是否发送钉钉群消息
is_dd_msg = False

# 设置文件路径
FILE_PATH = {
    'log': os.path.join(DIR_PATH, 'log'),
    'screenshot': os.path.join(DIR_PATH, 'screenshot'),
    'ini': os.path.join(DIR_PATH, 'config', 'config.ini')
}
