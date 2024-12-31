from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os
from dotenv import load_dotenv


# 環境変数からXの情報を読み込み
load_dotenv()
account_name = os.getenv('ACCOUNT_NAME')
password = os.getenv('PASSWORD')

# ChromeDriverの設定
service = Service(executable_path='chromedriver')
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(service=service, options=options)

# Xのログイン画面を開く
driver.get('https://x.com/i/flow/login')

try:
    # アカウント入力画面まで待機。開いたらアカウント名の入力
    input_account_name = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, '//input[@name="text"]'))
    )
    input_account_name.send_keys(account_name)
    input_account_name.send_keys(Keys.RETURN)

    # パスワード画面まで待機。開いたらパスワードの入力
    input_password = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, '//input[@name="password"]'))
    )
    input_password.send_keys(password)
    input_password.send_keys(Keys.RETURN)

finally:
    # 10秒後にブラウザを閉じる
    time.sleep(10)
    driver.quit()
