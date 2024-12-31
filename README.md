# seleniumの自動DMテスト

## 事前準備

最初に使用しているPCに合ったChromeDriverを用意してください。

https://googlechromelabs.github.io/chrome-for-testing/#stable

（Stable/chromedriver の欄から選択してください）

ダウンロード後、zipファイルを解凍し chromedriver（chromedriver.exe ）を、ルートディレクトリ直下に置いてください。

<br>

## 環境のインストール

chromedriver を設置したら、下記コマンドで環境をインストール

```
pip install -r requirements.txt
```

<br>

## 環境変数の設置

下記コマンドを実行して.envを設置、その後ファイル内にXのアカウントを記入してください。

```
cp .example.env .env
```

<br>

FROM_ACCOUNT=送信元アカウント名

PASSWORD=送信元パスワード

TO_ACCOUNT=送信先アカウント名

<br>

## 実行コマンド

ターミナルから下記コマンドを実行でDM自動送信を実行できます。

```
python main.py
```