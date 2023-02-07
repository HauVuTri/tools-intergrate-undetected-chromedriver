import random
import re
import string

import requests
from selenium.common import NoSuchElementException
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from argparse import ArgumentParser
import codecs
import sys

from selenium.webdriver.support.wait import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

# Local library import.

__version__ = '0.2'

# from namegen import nameGenerator

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
        # actions.pause(0.05)
    actions.send_keys(Keys.ENTER)
    actions.perform()


def get_list_quotes_random(limit=3, tag='love'):
    URL = f'https://api.quotable.io/quotes?limit={limit}&tags={tag}'
    # sending post request and saving response as response object
    r = requests.get(url=URL)
    data = r.json()
    return data['results']


print((get_list_quotes_random(10))[0]['content'])


def zoom_out_selenium(driver, percent_zoom=80):
    driver.execute_script(f"document.body.style.zoom='{percent_zoom}%'")
