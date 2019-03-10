import os
from http import client as httplib
import socket

from selenium.webdriver.remote.command import Command
from selenium import webdriver

from arconai import cache

options = webdriver.ChromeOptions()
options.add_argument("--headless")
try:
    driver = webdriver.Chrome(options=options)
except:
    pass

try:
    driver = webdriver.Chrome("./chromedriver", options=options)
except:
    import AutoChromedriver
    current_file_path = os.path.dirname(os.path.realpath(__file__))
    AutoChromedriver.download_chromedriver(version="2.34", location=current_file_path)
    driver = webdriver.Chrome(
            os.path.join(current_file_path, "chromedriver"), options=options)

def is_alive(driver):
    try:
        driver.execute(Command.STATUS)
        return True
    except (socket.error, httplib.CannotSendRequest):
        return False

def quitdriver():
    driver.quit()
    cache.save()

import atexit
atexit.register(quitdriver)
