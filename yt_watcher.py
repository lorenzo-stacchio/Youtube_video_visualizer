import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

import time
import tqdm
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException


def convert_string_time_to_seconds(time_youtube_string):
    # Go by trials
    time_not_codified = time_youtube_string.split(":")
    if len(time_not_codified) == 3:
        h, m, s = [int(x) for x in time_not_codified]
        return (h * 3600) + (m * 60) + s
    elif len(time_not_codified) == 2:
        m, s = [int(x) for x in time_not_codified]
        return (m * 60) + s
    else:
        return int(time_not_codified)


# ARGUMENTS
sound = False
views = 100
yt_url = "https://www.youtube.com/watch?v=BwWGZJeRVmU"


# CHROME DRIVER
chrome_options = webdriver.ChromeOptions()
if not sound:
    chrome_options.add_argument("--mute-audio")

for _ in range(views):
    driver = webdriver.Chrome(executable_path=r"drivers/chromedriver.exe", chrome_options=chrome_options)
    driver.get(yt_url)
    delay = 5  # seconds
    try:
        WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.TAG_NAME, 'tp-yt-paper-button')))
        print("The select youtube video page is fully loaded!")
    except TimeoutException:
        print("Loading took too much time!")

    title = driver.find_element(by=By.XPATH, value="/html/head/title").get_attribute('innerText')
    duration = driver.find_element(by=By.CLASS_NAME, value="ytp-time-duration").text
    yt_video_seconds = convert_string_time_to_seconds(duration)

    print("%s duration is %s. I will wait to it ends and then keep watching it." % (title, duration))
    buttons = driver.find_elements(by=By.TAG_NAME, value="tp-yt-paper-button")

    for b in buttons:
        if b.text == "ACCETTO":
            b.click()

    # Simulate passing time also providing user feedback
    for _ in tqdm.tqdm(range(yt_video_seconds), total = yt_video_seconds):
        time.sleep(1)
    driver.close()
