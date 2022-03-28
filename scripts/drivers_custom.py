from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile

tor_folder = "D:/Programs/Tor/Tor Browser/"


def load_tor_driver(args):
    profile_path = "D:/Programs/Tor/Tor Browser/Browser/TorBrowser/Data/Browser/profile.default"
    profile = FirefoxProfile(profile_path)
    binary = FirefoxBinary(r"%sBrowser/firefox.exe" % tor_folder)
    return webdriver.Firefox(firefox_profile=profile, firefox_binary=binary, executable_path=args.driver_path)


def load_chrome_driver(args):
    chrome_options = webdriver.ChromeOptions()
    if args.silent_mode:
        chrome_options.headless = True
        chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])
        chrome_options.add_argument("--mute-audio")  # include it with silent mode
    elif not args.sound:  # valid only in non-silent mode
        chrome_options.add_argument("--mute-audio")

    return webdriver.Chrome(executable_path=args.driver_path, chrome_options=chrome_options)


def load_driver(args):
    if args.browser == "chrome":
        return load_chrome_driver(args)
    elif args.browser == "tor":
        return load_tor_driver(args)
