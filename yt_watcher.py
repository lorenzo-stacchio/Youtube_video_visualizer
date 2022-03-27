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

import argparse

parser = argparse.ArgumentParser(description='Youtube viewer parameters.')

parser.add_argument('--youtube_url', dest='youtube_url', type=str,
                    default="https://www.youtube.com/watch?v=BwWGZJeRVmU",
                    help='Valid url to a youtube video.')

parser.add_argument('--views', dest='views', type=int, default=1,
                    help='Number of views to provide to the selected youtube video.')

parser.add_argument('--sound', dest='sound', type=bool, default=True,
                    help='Sound on if driver not in silent mode.')

parser.add_argument('--language', dest='language', type=str, default="it",
                    help='Language used in youtube, please refer to data/config_text_languages.json to check supported language or add by your own will.')

args = parser.parse_args()


# CHROME DRIVER
chrome_options = webdriver.ChromeOptions()
if not args.sound:
    chrome_options.add_argument("--mute-audio")

# COUNTRY OPTIONS
dict_html_elements_text = load_config_text_languages()

for idx in range(args.views):
    driver = webdriver.Chrome(executable_path=r"drivers/chromedriver.exe", chrome_options=chrome_options)
    driver.get(args.youtube_url)
    delay = 5  # seconds
    try:
        WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.TAG_NAME, 'tp-yt-paper-button')))
        # print("The select youtube video page is fully loaded!")
    except TimeoutException:
        print("Loading took too much time! Exit process")
        exit()

    title = driver.find_element(by=By.XPATH, value="/html/head/title").get_attribute('innerText')
    duration = driver.find_element(by=By.CLASS_NAME, value="ytp-time-duration").text
    yt_video_seconds = convert_string_time_to_seconds(duration)

    print("%s duration is %s. I will wait until it ends and then i will watch it again for other %s times." % (
        title, duration, args.views - (idx + 1)))
    buttons = driver.find_elements(by=By.TAG_NAME, value="tp-yt-paper-button")

    for b in buttons:
        if b.text == dict_html_elements_text["acceptance_terms_button_text"]["it"]:
            b.click()

    # Simulate passing time also providing user feedback
    for _ in tqdm.tqdm(range(yt_video_seconds), total=yt_video_seconds, desc="Actual visualization time in seconds"):
        time.sleep(1)
    driver.close()
