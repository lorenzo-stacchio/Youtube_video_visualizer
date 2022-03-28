import time
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)
from selenium import webdriver
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
import os

tor_folder = "D:/Programs/Tor/Tor Browser/"

# YOU MUST EXECUTE THE start script before of creating a tor browser, to enable search
# THIS IS COMMENTED BECAUSE YOU SHOULD DO IT BY YOURSELF ONCE AND LEAVE THE CONNECTION OPEN!
# script_connect_tor = "%sStart Tor Browser.lnk" % tor_folder
# os.startfile(script_connect_tor)
# time.sleep(10) # wait tor connects

binary = FirefoxBinary(r"%sBrowser/firefox.exe" % tor_folder)
# profile = FirefoxProfile(r"%sBrowser/TorBrowser/Data/Browser/profile.default/" % tor_folder)
# profile_path = "D:/Programs/Tor/Tor Browser/Browser/TorBrowser/Data/Browser/profile.default"
# profile = FirefoxProfile(profile_path)
# driver = webdriver.Firefox(profile, binary, executable_path = "../drivers/geckodriver.exe")
driver = webdriver.Firefox(firefox_binary = binary, executable_path = "../drivers/geckodriver.exe")
driver.get("https://www.youtube.com/watch?v=BwWGZJeRVmU")
