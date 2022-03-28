from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

tor_folder = "D:/Programs/Tor/Tor Browser/"
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary


def action_play_video_tor_driver(args, driver, dict_html_elements_text):
    delay = 5
    acceptance_element_found = False
    while not acceptance_element_found:
        try:
            WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.TAG_NAME, 'tp-yt-paper-button')))
            acceptance_element_found = True
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


def action_play_video_chrome_driver(args, driver, dict_html_elements_text):
    delay = 10
    acceptance_element_found = False
    while not acceptance_element_found:
        try:
            WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.TAG_NAME, 'tp-yt-paper-button')))
            acceptance_element_found = True
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


def action_play_video(args, driver, dict_html_elements_text):
    if args.browser == "chrome":
        return action_play_video_chrome_driver(args, driver, dict_html_elements_text)
    elif args.browser == "tor":
        return action_play_video_tor_driver(args, driver, dict_html_elements_text)
