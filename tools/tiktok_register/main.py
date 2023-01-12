# This is a sample Python script.
import os
import random
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

import undetected_chromedriver
from tools.proxy_combination import TMProxy
from tools.utilities import get_element_visibility_located, press_down_n_times_and_press_enter, random_account_profile, \
    get_element_clickable, click_element_by_action_chain_css_selector
from undetected_chromedriver import ChromeOptions
from selenium.webdriver import ActionChains, Keys, Proxy
from selenium.webdriver.support import expected_conditions as EC


def get_hotmail_otp(driver: undetected_chromedriver.Chrome, email_hotmail, password_hotmail):
    driver.tab_new("https://outlook.live.com/owa/")
    driver.switch_to.window(driver.window_handles[1])
    try:
        # Nếu trường hợp vào trang kia mà đc chuyển hướng sang trang https://www.microsoft.com/en-us/microsoft-365/outlook/email-and-calendar-software-microsoft-outlook
        get_element_visibility_located(driver,
                                       "body > header > div > aside > div > nav > ul > li:nth-child(2) > a").click()
    except:
        driver.find_element(By.CSS_SELECTOR, "a[data-bi-cn='SignIn']").click()
        time.sleep(2)
        driver.close()
        driver.switch_to.window(driver.window_handles[1])
        pass
    get_element_visibility_located(driver, "input[type='email']").send_keys(email_hotmail)
    get_element_visibility_located(driver, "input[type='submit']").click()
    get_element_visibility_located(driver, "input[type='password']").send_keys(password_hotmail)
    get_element_visibility_located(driver, "input[type='submit']").click()

    # POPUP Help us protect your account -> CLICK VÀO SKIP FOWW NOW
    try:
        get_element_visibility_located(driver, "#iShowSkip").click()
    except:
        pass

    # click vao nut khogn hien thi lai
    get_element_visibility_located(driver, "#KmsiCheckboxField").click()
    # click nut login
    get_element_visibility_located(driver, "input[type='submit']").click()

    # POpup Break free from your passwords
    try:
        driver.find_element(By.CSS_SELECTOR, "#iCancel").click()
    except:
        pass
    try:
        # tim toi email cua tiktok
        get_element_visibility_located(driver, 'span[title="noreply@account.tiktok.com"]').click()
    except:
        # if not found tiktok email:
        driver.switch_to.window(driver.window_handles[0])
        #click vao button resend
        driver.find_element(By.CSS_SELECTOR,"button[data-e2e='send-code-button']").click()
        driver.switch_to.window(driver.window_handles[1])
        # tim toi email cua tiktok
        get_element_visibility_located(driver, 'span[title="noreply@account.tiktok.com"]').click()

    otp_tikok = None
    otp_tikok = get_element_visibility_located(driver,
                                               "#ReadingPaneContainerId > div > div > div > div.L72vd > div > div:nth-child(2) > div > div > div > div > div > div > div > div > div > div:nth-child(1) > div:nth-child(3) > p:nth-child(2)",
                                               25).text
    print(f"Mã otp tiktok là:{otp_tikok}")
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    return otp_tikok


def solve_captcha():
    # todo: Handle solve captcha if exist
    pass


def register_tiktok_by_email(email_mail, password_mail, **kwargs):
    status = "Bắt đầu Reg"
    (first_name, player_id, password_fake, phone, withdraw_pin, bank_account, email_fake, bank_branch,
     bank_type) = random_account_profile(password_uppercase_character_require=True,
                                         password_special_character_require=True, password_limit=20)
    print(first_name, player_id, password_fake, phone, withdraw_pin, bank_account, email_fake, bank_branch, bank_type)
    """Đây là những setting khi khởi tạo Chrome Undetected """
    user_data_dir = kwargs.get('user_data_dir')
    # todo Tạm thời để None để test đã
    user_data_dir = None
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

    print(email_mail, password_mail)
    if not email_mail or not password_mail:
        raise Exception('dont exist email or password')
    chrome_option = ChromeOptions()
    chrome_option.add_argument("--window-size=1366,768")
    # if proxy:
    #
    #     if protocol_proxy == "https" or protocol_proxy == "http":
    #         proxy_object = Proxy({
    #             "proxyType": "MANUAL",
    #             "httpProxy": proxy,
    #         })
    #     elif protocol_proxy == "sock5" or protocol_proxy == "sock":
    #         proxy_object = Proxy({
    #             "proxyType": "MANUAL",
    #             "socksProxy": proxy,
    #         })
    #     chrome_option.proxy = proxy_object

    if proxy:
        chrome_option.add_argument('--proxy-server=' + proxy)
    driver = undetected_chromedriver.Chrome(options=chrome_option, user_data_dir=user_data_dir)
    status = "Khởi tạo chrome thành công"
    driver.implicitly_wait(20)
    driver.get("https://www.tiktok.com/signup")
    status = "Vào tiktok thành công"
    # Sử dụng số điện thoại hoặc email -> clíck()
    # driver.find_element(By.CSS_SELECTOR, "#loginContainer > div > div > a > div").click()
    get_element_visibility_located(driver, "#loginContainer > div > div > a > div").click()
    WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'a[href="/signup/phone-or-email/email"]'))).click()

    get_element_visibility_located(driver, "#loginContainer > div > form > div > div:nth-child(1) > div").click()
    # Chon thang sinh
    press_down_n_times_and_press_enter(driver, random.randint(1, 12))
    action = ActionChains(driver)
    action.send_keys(Keys.TAB).perform()
    time.sleep(1)
    # Chon ngay sinh
    press_down_n_times_and_press_enter(driver, random.randint(1, 25))
    action.send_keys(Keys.TAB).perform()
    time.sleep(1)
    # Chon nam sinh
    press_down_n_times_and_press_enter(driver, random.randint(20, 50))
    # Email address
    get_element_visibility_located(driver, "#loginContainer > div > form > div > div > input[name='email']").send_keys(
        email_mail)
    get_element_visibility_located(driver,
                                   "#loginContainer > div > form > div > div > input[type='password']").send_keys(
        password_fake)
    time.sleep(1)
    ActionChains(driver).move_by_offset(150, 250).click().perform()
    time.sleep(1)
    click_element_by_action_chain_css_selector(driver, "#loginContainer > div > form > div:nth-child(8) > div > button")

    # Nếu tiktok bắt giải captcha
    try:
        get_element_visibility_located(driver, "#captcha_container", 5)
    except:
        solve_captcha()
    try:
        get_element_visibility_located(driver,"div[type='error']",5)
    except:
        status = "Lỗi sau khi ấn Send Code Otp: Sorry, something went wrong, please try again later"

    otp_mail = get_hotmail_otp(driver, email_mail, password_mail)
    # Nhập OTP
    get_element_visibility_located(driver, "div.code-input > input").send_keys(otp_mail)
    # Click nhận thông báo
    get_element_visibility_located(driver, "#loginContainer > div > form > div > div > label > i").click()
    # Click next btn
    get_element_visibility_located(driver, "#loginContainer > div > form > button").click()
    # get_element_visibility_located(driver,"input[name='new-username']").send_keys(player_id)
    get_element_visibility_located(driver, "#loginContainer > div > form > div:nth-child(5)").click()

    # Đã đăng ký thành công vào giao diện tiktok
    if kwargs.get('profile_buff'):
        # Eg: @haulaptrinh
        driver.get(f"https://www.tiktok.com/{kwargs.get('profile_buff')}")
        get_element_visibility_located(driver,
                                       "#app > div > div > div > div > div > div > div:nth-child(1) > div > div > div > a > div > div > img").click()
        get_element_visibility_located(driver, "span[data-e2e='browse-like-icon']").click()
    time.sleep(999)


def readTxtData():
    dir_path = os.getcwd()
    # email, password, created_at = ("test", "test","test")
    # register_tiktok_by_email("test", "test", user_data_dir=f"{dir_path}/profiles/{email}")
    # Read each line txt file
    with open('data/file.txt', 'r') as f:
        for line in f:
            email, password, created_at = line.strip().split('|')
            # print(email, password)
            # do something with the email and password
            tmproxy = TMProxy("53d8148ddd854f3f58a3a8ea6cf46d6d")
            protocol_proxy = "http"
            proxy = tmproxy.get_new_proxy()
            register_tiktok_by_email(email, password, user_data_dir=f"{dir_path}/profiles/{email}", proxy=proxy,
                                     protocol_proxy=protocol_proxy, profile_buff='@haulaptrinh')
            time.sleep(tmproxy.get_rest_time_to_next_proxy())


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    readTxtData()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
