import warnings

warnings.filterwarnings("ignore", category=DeprecationWarning)

import time
import tqdm
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from utils import *
import random
import argparse

parser = argparse.ArgumentParser(description='Youtube viewer parameters.')

parser.add_argument('--youtube_url', dest='youtube_url', type=str,
                    default="https://www.youtube.com/watch?v=BwWGZJeRVmU",
                    help='Valid url to a youtube video.')

parser.add_argument('--views', dest='views', type=int, default=1,
                    help='Number of views to provide to the selected youtube video.')

parser.add_argument('--watch_full', dest='watch_full', action='store_true',
                    help='If used, the entire video will be watched (recommended for short videos).')

parser.add_argument('--chrome_driver_path', dest='chrome_driver_path', type=str, default="drivers/chromedriver.exe",
                    help='Path to the chrome driver to use.')

parser.add_argument('--silent_mode', dest='silent_mode', action='store_true',
                    help='Use the driver in silent mode.')

parser.add_argument('--sound', dest='sound', action='store_true',
                    help='Sound on if driver not in silent mode.')

parser.add_argument('--language', dest='language', type=str, default="en",
                    help='Language used in youtube, please refer to data/config_text_languages.json to check supported language or add by your own will.')

args = parser.parse_args()

# CHROME DRIVER
chrome_options = webdriver.ChromeOptions()

if args.silent_mode:
    chrome_options.headless = True
    chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])
    chrome_options.add_argument("--mute-audio")  # include it with silent mode
elif not args.sound:  # valid only in non-silent mode
    chrome_options.add_argument("--mute-audio")

# COUNTRY OPTIONS
dict_html_elements_text = load_config_text_languages()

for idx in range(args.views):
    driver = webdriver.Chrome(executable_path=args.chrome_driver_path, chrome_options=chrome_options)
    # driver.get(args.youtube_url)
    driver.get(
        args.youtube_url + "&hl=%s&persist_hl=1" % args.language)  # TESTING DIFFERENT LANGUAGE, please check data/testing_post_fix_change_language.txt
    delay = 5  # seconds
    try:
        WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.TAG_NAME, 'tp-yt-paper-button')))
        # print("The select youtube video page is fully loaded!")
    except TimeoutException:
        print("Loading took too much time! Exit process")
        exit()

    # CLICK ON ACCEPTANCE BUTTON
    buttons = driver.find_elements(by=By.TAG_NAME, value="tp-yt-paper-button")
    check_found = False
    for b in buttons:
        if b.text == dict_html_elements_text["acceptance_terms_button_text"][args.language]:
            b.click()
            check_found = True
    if not check_found:
        raise Exception(
            "Acceptance button not found, please update data/config_text_languages.json for your language and use non-silent mode for testing.")

    # Simulate passing time also providing user feedback
    # Time to watch is decided by the user choice
    title = driver.find_element(by=By.XPATH, value="/html/head/title").get_attribute('innerText')
    duration = driver.find_element(by=By.CLASS_NAME, value="ytp-time-duration").text

    if args.watch_full:
        yt_video_seconds = convert_string_time_to_seconds(duration)
    else:
        yt_video_seconds = random.randrange(30, 50)	  # minimum seconds to watch to count a visualization

    print(
        "%s duration is %s. I will watch it for %s seconds and then again for other %s times." % (
            title, duration, yt_video_seconds, args.views - (idx + 1)))

    for _ in tqdm.tqdm(range(yt_video_seconds), total=yt_video_seconds, desc="Actual visualization time in seconds"):
        time.sleep(1)
    driver.close()
