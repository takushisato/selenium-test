from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

service = Service(executable_path='chromedriver')

# ログ出力をオフ
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

driver = webdriver.Chrome(service=service, options=options)

# Googleでseleniumを検索
driver.get('https://www.google.com')
WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.CLASS_NAME, 'gLFyf'))
)
input_element = driver.find_element(By.CLASS_NAME, 'gLFyf')
input_element.send_keys('selenium' + Keys.ENTER)

# 検索結果をクリック
WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, 'selenium'))
)
link = driver.find_element(By.PARTIAL_LINK_TEXT, 'selenium')
link.click()

# 10秒後に閉じる
time.sleep(10)
driver.quit()
