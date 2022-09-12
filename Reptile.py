import subprocess
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_driver = r'C:\Users\11470\Downloads\chromedriver_win32\chromedriver.exe'


cmd = '"C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe" ' \
      '--remote-debugging-port=9222 ' \
      '--user-data-dir="D:\\Data\\Reptile\\UserDate"'


def get_title_from_url(url):
    print("Getting title from url:" + url)

    result = "default"
    return result


def start_reptile(link, path):
    print("Starting")
    # try:
    #     subprocess.run(cmd)
    # except subprocess.SubprocessError as error:
    #     print(error)
    # print("Starting111")
    # time.sleep(1)
    # print("Starting222")
    chrome_options = Options()
    chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
    print("Trying to start0")
    driver = webdriver.Chrome(executable_path=chrome_driver, options=chrome_options)
    print("Trying to start")
    print(driver.title)

    title = get_title_from_url(link)
    print("Title: " + title)
