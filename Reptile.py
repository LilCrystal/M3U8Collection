import os
import subprocess
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_driver = r'C:\Users\11470\Downloads\chromedriver_win32\chromedriver'


cmd = '"C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe" ' \
      '--remote-debugging-port=9222 ' \
      '--user-data-dir="D:\\Data\\Reptile\\UserDate"'


def start_reptile(link, path):
    print("Starting")
    print("Starting2")
    chrome_options = Options()
    print("Starting3")
    chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")

    driver = webdriver.Chrome(executable_path=chrome_driver, chrome_options=chrome_options)
    file_name = driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[7]/div/div[2]/div[1]").text

    file_name = file_name.replace(' ', '')
    file_name = file_name.replace('\r', '')
    file_name = file_name.replace('\n', '')
    file_name = file_name.replace('。', '')
    file_name = file_name.replace('&', '')
    print("HHHHHHHHHHHHHHHHH is" + file_name)
    m3u8_url = driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[7]/div/div[2]/div[3]/div[1]/div[1]/input")\
        .get_attribute("value")
    print(m3u8_url)
    command = "ffmpeg -i " + m3u8_url\
              + " -c copy " + path + file_name + ".mp4"
    print(command)
    os.system(command)

