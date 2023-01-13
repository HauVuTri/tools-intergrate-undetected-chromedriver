# This is a sample Python script.
import os
import random
import re
import time

from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from twocaptcha import TwoCaptcha

import undetected_chromedriver
from tools.proxy_combination import TMProxy
from tools.utilities import get_element_visibility_located, random_account_profile, \
    get_element_presence_located, get_list_quotes_random
from undetected_chromedriver import ChromeOptions

token_viotp = '0d2247f6ad364364a22c1cb3abbe4e13'  # Đây là token ở viotp
key_2captcha = '88ec72f21f08c05315757dca2941eaf4'  # Day la  key cua 2captcha


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


def handle_check_solve_captcha(driver):
    iframe = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'iframe[title="reCAPTCHA"]')))
    src = iframe.get_attribute('src')
    if not src:
        raise Exception("Not found src iframe ")

    def get_site_key(src):
        src = "https://www.google.com/recaptcha/api2/anchor?ar=1&k=6LcvQtkhAAAAAF_-x9pdXxBAWCMSpDUur5g9UGpO&co=aHR0cHM6Ly90b24ucGxhY2U6NDQz&hl=en&type=image&v=u35fw2Dx4G0WsO6SztVYg4cV&theme=dark&size=normal&badge=bottomright&cb=pea3mdjaopm6"
        match = re.search("&k=(.+?)&", src)

        if match:
            k_value = match.group(1)
            print(k_value)
            return k_value
        else:
            print("&k value not found")

    # todo: Get site_key from the captcha in the web
    site_key = get_site_key(src)
    solver = TwoCaptcha(apiKey=key_2captcha)
    result = solver.recaptcha(sitekey=site_key, url='https://ton.place/id435978?w=post')
    print(result)
    time.sleep(999)
    pass


def choose_random_image_in_folder(folder_path):
    # get a list of all files in the directory
    files = os.listdir(folder_path)
    # select a random file from the list
    random_file = random.choice(files)
    return random_file


def place_ton_register(email_mail, password_mail, **kwargs):
    status = "Bắt đầu Reg"
    (first_name, player_id, password_fake, phone, withdraw_pin, bank_account, email_fake, bank_branch,
     bank_type) = random_account_profile(password_uppercase_character_require=True,
                                         password_special_character_require=True, password_limit=20)
    print(first_name, player_id, password_fake, phone, withdraw_pin, bank_account, email_fake, bank_branch, bank_type)
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
    get_element_visibility_located(driver, "input[type='email']").click()
    time.sleep(1)
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
    sign_in_with_google = get_element_visibility_located(driver,
                                                         "#root > div > div.Content__wrap.fullWidth > div > div > div.AuthPopover__wrapper > div.AuthPopover > div > div > div.Auth > div.Auth__socials > div:nth-child(2)")
    time.sleep(2)
    sign_in_with_google.click()
    try:
        get_element_visibility_located(driver, f"div[data-identifier='{email_mail.strip().lower()}']").click()
    except:
        sign_in_with_google.click()
        get_element_visibility_located(driver, f"div[data-identifier='{email_mail.strip().lower()}']").click()

    # todo: thiếu bước nhập player_id -> rồi enter
    get_element_visibility_located(driver, "#root > div > div.Content__wrap > div.Form > div:nth-child(1) > div.Form__item__cont > div > div.Input__wrapper > input").send_keys(player_id)
    time.sleep(3)
    get_element_presence_located(driver, "#root > div > div.Content__wrap > div.Form > div:nth-child(2) > div > div").click()
    time.sleep(5)
    driver.find_element(By.CSS_SELECTOR, '#root > div > div.Placeholder__actions > div > div:nth-child(1) > div > div.ListItem__content > div').click()

    # (WebDriverWait(driver, 15).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, '#root > div > div.Placeholder__actions > div > div:nth-child(1) > div > div.ListItem__content > div'), 'Info & Entertainment'))).parent().parent().parent().click()
    try:
        # click vào thể loại muốn theo đuổi -> chọn cái đầu tiên
        get_element_visibility_located(driver, "#root > div > div.Placeholder__actions > div > div:nth-child(1)", 10).click()
    except:
        pass
    driver.get("https://ton.place/feed?section=following")
    # vào trang my Page
    myPageElem = driver.find_element(By.CSS_SELECTOR, "#root > div > div.App__desktop_menu > div > a:nth-child(2)")
    # ở đây đã lấy đc id của user này
    user_id = myPageElem.get_attribute("href")
    print(f"User id là: {user_id}")
    myPageElem.click()
    # Đổi avatar
    driver.find_element(By.CSS_SELECTOR,
                        "#profile_scrollView > div > div.ptr__children > div.Profile > div.Profile__info_block > div.Profile__common_info > div.UnitPhoto.large.active > img").click()
    # click change photo
    # get_element_visibility_located(driver,"#action_sheet > div > div.BottomSheet__sheet_wrap > div > div.BottomSheet__content.hasScroll > div > div:nth-child(1) > div > div > div.ListItem__content > div > input").click()
    # driver.find_element(By.CSS_SELECTOR,
    #                     "#action_sheet > div > div.BottomSheet__sheet_wrap > div > div.BottomSheet__content.hasScroll > div > div:nth-child(1) > div > div > div.ListItem__content > div > input")

    # select image to update
    driver.find_element(By.CSS_SELECTOR,
                        "#action_sheet > div > div.BottomSheet__sheet_wrap > div > div.BottomSheet__content.hasScroll > div > div:nth-child(1) > div > div > div.ListItem__content > div > input").send_keys(
        os.getcwd() + f"/images/{choose_random_image_in_folder(os.getcwd() + '/images')}")

    # Update cover picture:
    driver.find_element(By.CSS_SELECTOR, "#profile_scrollView > div > div.ptr__children > div.Profile__cover.active.visible.empty > input").send_keys(
        os.getcwd() + f"/images/{choose_random_image_in_folder(os.getcwd() + '/images')}")
    time.sleep(2)
    # Click save btn
    # get_element_visibility_located(driver,"#root > div > div.App__desktop_cont > div > div.Modal__wrap > div > div.BottomBar.row > div > div > div").click()
    driver.execute_script('document.querySelector("#root > div > div.App__desktop_cont > div > div.Modal__wrap > div > div.BottomBar.row > div > div > div").click()')
    time.sleep(4)
    # driver.find_element(By.CSS_SELECTOR, "#root > div > div.App__desktop_cont > div > div.Modal__wrap > div > div.BottomBar.row > div > div > div").click()
    # Đăng status
    driver.find_element(By.CSS_SELECTOR, "#profile_scrollView > div > div.ptr__children > div.Profile > div.Profile__info_block > div.Profile__common_info > div.Profile__common_info__cont > a").click()
    random_11_quotes = get_list_quotes_random(limit=11)
    if not random_11_quotes:
        random_11_quotes = [{"content": "Hello"}, {"content": "Hello"}, {"content": "Hello"}, {"content": "Hello"}, {"content": "Hello"}, {"content": "Hello"}, {"content": "Hello"}, {"content": "Hello"},
                            {"content": "Hello"}, {"content": "Hello"}, {"content": "Hello"}]

    get_element_visibility_located(driver, "#root > div > div.App__desktop_cont > div > div.Modal__wrap > div > div.ScrollView > div > div > div > div.Form__item__cont > div > input").send_keys(
        random_11_quotes[0]['content'])
    time.sleep(1)
    # get_element_visibility_located(driver, "#root > div > div.App__desktop_cont > div > div.Modal__wrap > div > div.BottomBar.row > div > div > div").click()
    driver.execute_script('document.querySelector("#root > div > div.App__desktop_cont > div > div.Modal__wrap > div > div.BottomBar.row > div > div > div").click()')

    # driver.find_element(By.CSS_SELECTOR, "#root > div > div.App__desktop_cont > div > div.Modal__wrap > div > div.BottomBar.row > div > div > div").click()

    # Đăng post(bài viết)
    def post_news(driver, quote="Hello", is_check_captcha=False):
        print(f"quote la: {quote}")
        get_element_visibility_located(driver, "#profile_scrollView > div > div.ptr__children > div.Profile > a > div > div").click()
        get_element_visibility_located(driver, "#ql_editor > div > div.ql-editor.ql-blank").send_keys(quote)
        get_element_visibility_located(driver, "#root > div > div.App__desktop_cont > div > div.Modal__wrap > div > div.BottomBar.fixed.row > div > div > div").click()
        if is_check_captcha:
            handle_check_solve_captcha(driver)
    time.sleep(4)
    post_news(driver, quote=random_11_quotes[1]['content'], is_check_captcha=True)
    for i in range(9):
        post_news(driver, quote=random_11_quotes[i + 2]['content'], is_check_captcha=False)
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
