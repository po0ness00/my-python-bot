import requests
from mnemonic import Mnemonic
from bitcoinlib.wallets import Wallet
from bitcoinlib.services.services import Service

# ایجاد یک شی از کلاس Mnemonic برای زبان انگلیسی
mnemo = Mnemonic("english")

# تعداد دفعاتی که می‌خواهید عبارت یادآوری و آدرس جدید ایجاد کنید
num_iterations = 5

# حلقه برای ایجاد چندین عبارت یادآوری و آدرس جدید
for i in range(num_iterations):
    # تولید عبارت یادآوری (12 کلمه‌ای)
    mnemonic_phrase = mnemo.generate(strength=128)
    
    # ساخت کیف پول از عبارت یادآوری
    wallet = Wallet.create(f"Wallet_{i}", keys=mnemonic_phrase, network='bitcoin')
    
    # بازیابی آدرس کیف پول از کیف پول ایجاد شده
    address = wallet.get_key().address
    
    print(f"عبارت یادآوری {i+1}: {mnemonic_phrase}")
    print(f"آدرس کیف پول {i+1}: {address}")
    
    # استفاده از API بلاک‌چین برای چک کردن موجودی
    service = Service()
    balance = service.getbalance(address)  # استفاده از getbalance
    b=(f"موجودی آدرس {i+1}: {balance} ساتوشی.\n")


url = ("https://api.telegram.org/bot7424373311:AAG0WvIbWo--1_G-dSSP4ncllVHbHhewNo8/sendmessage?chat_id=299233265&text="+str(b))
darkhast = {
"UrlBox" : url,
"AgentList" : "Google Chrome",
"versionlist":"HTTP/1.1",
"MethodList": "POST"

}
req = requests.post("https://www.httpdebugger.com/Tools/ViewHttpHeaders.aspx",darkhast) 
print(req)