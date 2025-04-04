import requests
import time
import random
from mnemonic import Mnemonic
from bitcoinlib.wallets import Wallet

# تنظیمات
mnemo = Mnemonic("english")
num_iterations = 5  # تعداد کیف پول‌ها
telegram_token = "7424373311:AAG0WvIbWo--1_G-dSSP4ncllVHbHhewNo8"
chat_id = "299233265"

for i in range(num_iterations):
    # تولید عبارت یادآوری ۱۲ کلمه‌ای
    mnemonic_phrase = mnemo.generate(strength=128)
    
    # ایجاد نام منحصربه‌فرد برای کیف پول
    wallet_name = f"Wallet_{i}_{int(time.time())}"

    # ✅ ایجاد کیف پول بیت‌کوین و دریافت آدرس
    wallet = Wallet.create(wallet_name, keys=mnemonic_phrase, network='bitcoin')
    btc_address = wallet.get_key().address

    # دریافت موجودی بیت‌کوین از Blockchain.com (بدون نیاز به API Key)
    btc_url = f"https://blockchain.info/q/addressbalance/{btc_address}"
    response = requests.get(btc_url)
    btc_balance = response.text if response.status_code == 200 else "نامشخص"

    # ⏳ تأخیر تصادفی بین ۳ تا ۷ ثانیه برای جلوگیری از بلاک شدن
    time.sleep(random.randint(3, 7))

    # ساخت پیام برای ارسال به تلگرام
    message = f"""🔹 random wallet name     {wallet_name}
📌 pharse key:       {mnemonic_phrase}


💰 adress BTC:                  {btc_address}
📊 موجدی BTC: {btc_balance}      satoshi
"""

    # ارسال پیام به تلگرام از طریق میانجی
    url = f"https://api.telegram.org/bot{telegram_token}/sendMessage?chat_id={chat_id}&text={message}"
    darkhast = {
        "UrlBox": url,
        "AgentList": "Google Chrome",
        "versionlist": "HTTP/1.1",
        "MethodList": "POST"
    }
    requests.post("https://www.httpdebugger.com/Tools/ViewHttpHeaders.aspx", darkhast)

    print(f"📨 اطلاعات کیف پول '{wallet_name}' ارسال شد.")

    # ⏳ تأخیر نهایی بین هر کیف پول برای جلوگیری از بلاک شدن
    time.sleep(random.randint(5, 10))

print("✅ همه پیام‌ها ارسال شدند.")
