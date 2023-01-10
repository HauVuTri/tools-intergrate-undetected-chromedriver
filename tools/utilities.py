import random
import re
import string

from selenium.common import NoSuchElementException
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from argparse import ArgumentParser
import codecs
import sys

from selenium.webdriver.support.wait import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC

# Local library import.

__version__ = '0.2'

from tools.namegen import nameGenerator

provinces_vietnam = ["HA NOI", "THANH PHO HO CHI MINH", "AN GIANG", "BA RIA-VUNG TAU", "BAC GIANG",
                     "BAC KAN", "BAC LIEU", "BAC NINH", "BEN TRE",
                     "BINH DINH", "BINH DUONG", "BINH PHUOC", "BINH THUAN", "CA MAU", "CAN THO",
                     "CAO BANG",
                     "DAK LAK", "DAK NONG", "DIEN BIEN", "DONG NAI", "DONG THAP", "GIA LAI", "HA GIANG",
                     "HA NAM",
                     "HA TINH", "HAI DUONG", "HAI PHONG", "HAU GIANG", "HOA BINH", "HUNG YEN", "KHANH HOA",
                     "KIEN GIANG", "KON TUM", "LAI CHAU", "LANG SON", "LAO CAI", "LONG AN", "NAM DINH",
                     "NGHE AN",
                     "NINH BINH", "NINH THUAN", "PHU THO", "PHU YEN", "QUANG BINH", "QUANG NAM",
                     "QUANG NGAI",
                     "QUANG NINH", "QUANG TRI", "SOC TRANG", "SON LA", "TAY NINH", "THAI BINH",
                     "THAI NGUYEN",
                     "THANH HOA", "THUA THIEN-HUE", "TIEN GIANG", "TRA VINH", "TUYEN QUANG", "VINH LONG",
                     "VINH PHUC", "YEN BAI"]


def click_element_by_action_chain_css_selector(driver, css_selector):
    btn = driver.find_element(By.CSS_SELECTOR, css_selector)
    new_action = ActionChains(driver)
    new_action.move_to_element(btn)
    new_action.click()
    new_action.perform()


def check_exist_by_selector(driver, selector):
    try:
        driver.find_element(By.CSS_SELECTOR, selector)
    except NoSuchElementException:
        return False
    return True


def no_accent_vietnamese(s):
    s = re.sub('Đ', 'D', s)
    s = re.sub('ð', 'D', s)
    s = re.sub('[áàảãạăắằẳẵặâấầẩẫậ]', 'a', s)
    s = re.sub('[ÁÀẢÃẠĂẮẰẲẴẶÂẤẦẨẪẬ]', 'A', s)
    s = re.sub('[éèẻẽẹêếềểễệ]', 'e', s)
    s = re.sub('[ÉÈẺẼẸÊẾỀỂỄỆ]', 'E', s)
    s = re.sub('[óòỏõọôốồổỗộơớờởỡợ]', 'o', s)
    s = re.sub('[ÓÒỎÕỌÔỐỒỔỖỘƠỚỜỞỠỢ]', 'O', s)
    s = re.sub('[íìỉĩị]', 'i', s)
    s = re.sub('[ÍÌỈĨỊ]', 'I', s)
    s = re.sub('[úùủũụưứừửữự]', 'u', s)
    s = re.sub('[ÚÙỦŨỤƯỨỪỬỮỰ]', 'U', s)
    s = re.sub('[ýỳỷỹỵ]', 'y', s)
    s = re.sub('[ÝỲỶỸỴ]', 'Y', s)
    s = re.sub('đ', 'd', s)
    return s


def random_account_profile(**kwargs):
    """
    Hàm gen profile mỗi account
    """
    stringRandom = string.ascii_lowercase  # use for playerid
    digit_random = string.digits  # use for number

    listName = nameGenerator()
    fullname = (' '.join(listName))
    onlyName = no_accent_vietnamese(listName[-1])
    onlyFamilyName = no_accent_vietnamese(listName[0])

    full_name_no_accent = no_accent_vietnamese(fullname).upper()
    x = random.randint(1, 5)
    if x == 1:
        player_id = (onlyName.lower() + onlyFamilyName.lower() + (
            ''.join(random.choice(digit_random) for i in range(6)))).lower()
        # password = (''.join(random.choice(stringRandom) for i in range(10))).lower() + ''.join(random.choice(digit_random) for i in range(3))
        withdraw_pin = (''.join(random.choice(digit_random) for i in range(8)))
        email = (onlyName.lower() + onlyFamilyName.lower() + (
            ''.join(random.choice(digit_random) for i in range(4))) + "@gmail.com").lower()
    if x == 2:
        player_id = (onlyName.lower() + onlyFamilyName.lower() + (
            ''.join(random.choice(digit_random) for i in range(4)))).lower()
        # password = (''.join(random.choice(stringRandom) for i in range(8))).lower() + ''.join(random.choice(digit_random) for i in range(2))
        withdraw_pin = (''.join(random.choice(digit_random) for i in range(10)))
        email = (onlyName.lower() + onlyFamilyName.lower() + (
            ''.join(random.choice(digit_random) for i in range(3))) + "@gmail.com").lower()
    if x == 3:
        player_id = (onlyName.lower() + (
            ''.join(random.choice(digit_random) for i in range(6)))).lower()
        # password = (''.join(random.choice(stringRandom) for i in range(6))).lower() + ''.join(random.choice(digit_random) for i in range(2))
        withdraw_pin = (''.join(random.choice(digit_random) for i in range(8)))
        email = (onlyName.lower() + (
            ''.join(random.choice(digit_random) for i in range(8))) + "@gmail.com").lower()
    if x == 4:
        player_id = (onlyFamilyName.lower() + onlyName.lower() + (
            ''.join(random.choice(digit_random) for i in range(4)))).lower()
        # password = (''.join(random.choice(stringRandom) for i in range(6))).lower() + ''.join(random.choice(digit_random) for i in range(2))
        withdraw_pin = (''.join(random.choice(digit_random) for i in range(8)))
        email = (onlyFamilyName.lower() + onlyName.lower() + (
            ''.join(random.choice(digit_random) for i in range(4))) + "@gmail.com").lower()
    if x == 5:
        player_id = (onlyFamilyName.lower() + onlyName.lower() + (
            ''.join(random.choice(digit_random) for i in range(3)))).lower()
        # password = player_id + str(random.randint(1970, 1995))
        withdraw_pin = (''.join(random.choice(digit_random) for i in range(8)))
        email = (player_id.lower() + onlyName.lower() + (
            ''.join(random.choice(digit_random) for i in range(1))) + "@gmail.com").lower()

    # bank_account = bank_account_start_with + (
    #     ''.join(random.choice(digit_random) for i in range(bank_account_len - len(bank_account_start_with))))
    bank_type = random.choice(['Vietinbank', 'Vietcombank', 'ACB', 'Techcombank'])
    if (bank_type == 'Vietinbank'):
        bank_account = '10' + (
            ''.join(random.choice(digit_random) for i in range(12 - len('10'))))
    if (bank_type == 'Vietcombank'):
        bank_account = '071100' + (
            ''.join(random.choice(digit_random) for i in range(13 - len('071100'))))
    if (bank_type == 'ACB'):
        bank_account = '8' + (
            ''.join(random.choice(digit_random) for i in range(9 - len('8'))))
    if (bank_type == 'Techcombank'):
        bank_account = '1903' + (
            ''.join(random.choice(digit_random) for i in range(14 - len('1903'))))
    bank_branch = random.choice(provinces_vietnam)
    phone = random.choice(
        ['32', '33', '34', '35', '37', '38', '39', '70', '79', '77', '76', '36', '78', '83', '84', '85', '81', '56']) + (''.join(random.choice(digit_random) for i in range(7)))
    password = (''.join(random.choice(string.ascii_uppercase) for i in range(1))) + (''.join(random.choice(string.ascii_lowercase) for i in range(5))) + (''.join(random.choice(string.digits) for i in range(4)))
    if kwargs.get('password_uppercase_character_require'):
        password = random.choice(string.ascii_uppercase) + password
    if kwargs.get('password_special_character_require'):
        password = random.choice('~!@#$%^&*()_+') + password
    if kwargs.get('password_limit') and kwargs.get('password_limit') > 0:
        password = password[:kwargs.get('password_limit')]

    return (full_name_no_accent, player_id, password, phone, withdraw_pin, bank_account, email, bank_branch, bank_type)


def get_element_visibility_located(driver, css_selector, time=15):
    return WebDriverWait(driver, time).until(EC.visibility_of_element_located((By.CSS_SELECTOR, css_selector)))


def get_element_presence_located(driver, css_selector, time=15):
    return WebDriverWait(driver, time).until(EC.presence_of_element_located((By.CSS_SELECTOR, css_selector)))


def get_element_clickable(driver, css_selector, time=15):
    return WebDriverWait(driver, time).until(EC.element_to_be_clickable((By.CSS_SELECTOR, css_selector)))


def press_down_n_times_and_press_enter(driver, n=1):
    actions = ActionChains(driver)
    for _ in range(n):
        actions = actions.send_keys(Keys.DOWN)
        actions.pause(0.05)
    actions.send_keys(Keys.ENTER)
    actions.perform()
