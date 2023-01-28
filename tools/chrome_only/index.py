# This is a sample Python script.

import undetected_chromedriver
from proxy_combination import TMProxy
from utilities import get_element_visibility_located
from undetected_chromedriver import ChromeOptions

token_viotp = '0d2247f6ad364364a22c1cb3abbe4e13'  # Đây là token ở viotp
key_2captcha = '88ec72f21f08c05315757dca2941eaf4'  # Day la  key cua 2captcha


def chrome_initial(**kwargs):
    status = "Bắt đầu Reg"

    """Đây là những setting khi khởi tạo Chrome Undetected """
    user_data_dir = kwargs.get('user_data_dir')
    proxy = kwargs.get('proxy')
    protocol_proxy = kwargs.get('protocol_proxy')
    port = 0
    enable_cdp_events = False
    service_args = None
    service_creationflags = None
    desired_capabilities = None
    advanced_elements = False
    service_log_path = None
    keep_alive = True
    log_level = 0
    headless = False
    version_main = None
    patcher_force_close = False
    suppress_welcome = True
    use_subprocess = True
    debug = False
    no_sandbox = True
    # Hết các thuộc tính init Chrome Undetected

    chrome_option = ChromeOptions()
    chrome_option.add_argument("--window-size=1920,1080")
    if proxy:
        chrome_option.add_argument('--proxy-server=' + proxy)
    driver = undetected_chromedriver.Chrome(options=chrome_option, user_data_dir=user_data_dir)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    tmproxy = TMProxy("53d8148ddd854f3f58a3a8ea6cf46d6d")
    protocol_proxy = "http"
    proxy = tmproxy.get_new_proxy(raise_except=False)
    chrome_initial(proxy=proxy, protocol_proxy=protocol_proxy)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
