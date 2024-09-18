import requests
from bs4 import BeautifulSoup
from time import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.wait import WebDriverWait

# Initialize Firefox/Gecko WebDriver
driver = webdriver.Firefox()
firefox_options = Options()


driver.get('https://vk.com/dating')

# Log in to your account (You must provide your own login credentials)
# login_username = driver.find_element_by_name(\"email\")
# login_username.send_keys(\"Your username goes here\")
# password = login_username.find_element_by_xpath(\".//..//..//..//..//..//*[local-name()='span' and @class='vk_login_text']/..//..//..//..//*[local-name()='input' and @name='password']\")
# password.send_keys(\"Your password goes here\")
# login_button = driver.find_element_by_xpath(\"//*[local-name()='span' and @class='vk_login_button vk_login_button_primary']/..\")
# login_button.click()
# time.sleep(5)

# Click on all the 'Like' buttons
# likes = driver.find_elements_by_class_name('vkuiTappable__stateLayer')
while True:
    keyDown('>')

#zdY03b82 zvMigqbX