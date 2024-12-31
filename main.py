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
from_account = os.getenv('FROM_ACCOUNT')
password = os.getenv('PASSWORD')
to_account = os.getenv('TO_ACCOUNT')

# ChromeDriverの設定
service = Service(executable_path='chromedriver')
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(service=service, options=options)


try:
    # DM送信元アカウントのログイン画面を開く
    driver.get('https://x.com/i/flow/login')

    # アカウント入力画面まで待機。開いたらアカウント名の入力
    from_account_name = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, '//input[@name="text"]'))
    )
    from_account_name.send_keys(from_account)
    from_account_name.send_keys(Keys.RETURN)

    # パスワード画面まで待機。開いたらパスワードの入力
    input_password = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, '//input[@name="password"]'))
    )
    input_password.send_keys(password)
    input_password.send_keys(Keys.RETURN)

    # ログインが完了するまで10秒待機
    time.sleep(10)

    # DM送信先のユーザーのHOME画面を開く
    to_account_home = 'https://x.com/' + to_account
    driver.get(to_account_home)

    # DMボタンを探してクリック。DM画面へ遷移
    dm_button = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="sendDMFromProfile"]'))
    )
    dm_button.click()

    # 待機
    time.sleep(5)

    # メッセージ入力フィールドを探して入力
    message_box = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="dmComposerTextInput"]'))
    )
    message = "お久しぶりです"  # DM本文
    message_box.send_keys(message)
    message_box.send_keys(Keys.RETURN)

finally:
    # 10秒後にブラウザを閉じる
    time.sleep(10)
    driver.quit()
