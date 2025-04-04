import requests
import time
from mnemonic import Mnemonic
from bitcoinlib.wallets import Wallet

# تنظیمات
mnemo = Mnemonic("english")
num_iterations = 1  # تعداد کیف پول‌ها
telegram_token = "7424373311:AAG0WvIbWo--1_G-dSSP4ncllVHbHhewNo8"
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

    # ارسال هر پیام از طریق سایت میانجی
    url = f"https://api.telegram.org/bot{telegram_token}/sendMessage?chat_id={chat_id}&text={message}"
    
    darkhast = {
        "UrlBox": url,
        "AgentList": "Google Chrome",
        "versionlist": "HTTP/1.1",
        "MethodList": "POST"
    }

    # ارسال درخواست به میانجی برای هر کیف پول
    req = requests.post("https://www.httpdebugger.com/Tools/ViewHttpHeaders.aspx", darkhast)
    
    print(f"📨 اطلاعات کیف پول '{wallet_name}' ارسال شد.")

print("✅ همه پیام‌ها ارسال شدند.")
