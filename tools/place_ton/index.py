# This is a sample Python script.
import os
import random
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

import undetected_chromedriver
from tools.proxy_combination import TMProxy
from tools.utilities import get_element_visibility_located, press_down_n_times_and_press_enter, random_account_profile, \
    get_element_clickable, click_element_by_action_chain_css_selector, get_element_presence_located
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
        # click vao button resend
        driver.find_element(By.CSS_SELECTOR, "button[data-e2e='send-code-button']").click()
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


def place_ton_register(email_mail, password_mail, **kwargs):
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
    chrome_option.add_argument("--window-size=1920,1080")
    if proxy:
        chrome_option.add_argument('--proxy-server=' + proxy)
    driver = undetected_chromedriver.Chrome(options=chrome_option, user_data_dir=user_data_dir)
    status = "Khởi tạo chrome thành công"
    driver.implicitly_wait(15)
    driver.get("https://mail.google.com/mail/")
    # driver.find_element(By.CSS_SELECTOR,"input[type='email']").send_keys(email_mail)
    get_element_visibility_located(driver, "input[type='email']").send_keys(email_mail)
    ActionChains(driver).send_keys(Keys.ENTER).perform()
    # driver.find_element(By.CSS_SELECTOR,"input[type='password']").send_keys(password_mail)
    get_element_visibility_located(driver, "input[type='password']").send_keys(password_mail)
    ActionChains(driver).send_keys(Keys.ENTER).perform()
    driver.tab_new('https://ton.place/')
    driver.switch_to.window(driver.window_handles[1])

    # click vào join now
    get_element_visibility_located(driver,
                                   "#root > div > div.Content__wrap.fullWidth > div > div > div.Landing__wrapper.__header > div > div.Landing__header__content > div.Landing__header__btns > div.Button.default.normal").click()
    sign_in_with_google =  get_element_visibility_located(driver,
                                   "#root > div > div.Content__wrap.fullWidth > div > div > div.AuthPopover__wrapper > div.AuthPopover > div > div > div.Auth > div.Auth__socials > div:nth-child(2)")
    time.sleep(2)
    sign_in_with_google.click()
    try:
        get_element_visibility_located(driver, f"div[data-identifier='{email_mail.strip().lower()}']").click()
    except:
        sign_in_with_google.click()
        get_element_visibility_located(driver, f"div[data-identifier='{email_mail.strip().lower()}']").click()

    # todo: thiếu bước nhập player_id -> rồi enter
    get_element_visibility_located(driver,"#root > div > div.Content__wrap > div.Form > div:nth-child(1) > div.Form__item__cont > div > div.Input__wrapper > input").send_keys(player_id)
    time.sleep(3)
    get_element_presence_located(driver,"#root > div > div.Content__wrap > div.Form > div:nth-child(2) > div > div").click()


    # click vào thể loại muốn theo đuổi -> chọn cái đầu tiên
    get_element_visibility_located(driver, "#root > div > div.Placeholder__actions > div > div:nth-child(1)").click()

    driver.get("https://ton.place/feed?section=following")
    # vào trang my Page
    myPageElem = driver.find_element(By.CSS_SELECTOR, "#root > div > div.App__desktop_menu > div > a:nth-child(2)")
    #ở đây đã lấy đc id của user này
    idUser = myPageElem.get_attribute("href")
    myPageElem.click()
    # Đổi avatar
    driver.find_element(By.CSS_SELECTOR,
                        "#profile_scrollView > div > div.ptr__children > div.Profile > div.Profile__info_block > div.Profile__common_info > div.UnitPhoto.large.active > img").click()
    # click change photo
    driver.find_element(By.CSS_SELECTOR,"#action_sheet > div > div.BottomSheet__sheet_wrap > div > div.BottomSheet__content.hasScroll > div > div:nth-child(1) > div > div > div.ListItem__content > div > input").click()

    #select image to update
    driver.find_element(By.CSS_SELECTOR,"#action_sheet > div > div.BottomSheet__sheet_wrap > div > div.BottomSheet__content.hasScroll > div > div:nth-child(1) > div:nth-child(2) > div > div.ListItem__content > div > input").send_keys(os.getcwd() + "/images/1.png")
    time.sleep(999)




def readTxtData():
    dir_path = os.getcwd()
    # gmail, password, email_recovery = ("test", "test","test")
    # register_tiktok_by_email("test", "test", user_data_dir=f"{dir_path}/profiles/{gmail}")
    # Read each line txt file -> get google accounts -> using this account to register place.ton
    with open('data/file.txt', 'r') as f:
        for line in f:
            gmail, password, email_recovery = line.strip().split('|')
            # print(gmail, password)
            # do something with the gmail and password
            tmproxy = TMProxy("53d8148ddd854f3f58a3a8ea6cf46d6d")
            protocol_proxy = "http"
            proxy = tmproxy.get_new_proxy()
            place_ton_register(gmail, password, user_data_dir=f"{dir_path}/profiles/{gmail}", proxy=proxy,
                               protocol_proxy=protocol_proxy, profile_buff='@haulaptrinh')
            time.sleep(tmproxy.get_rest_time_to_next_proxy())


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    readTxtData()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
