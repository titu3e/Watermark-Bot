# (c) @AbirHasan2005

# Don't Forget That I Made This!
# So Give Credits!


import os


class Config(object):
	BOT_TOKEN = os.environ.get("BOT_TOKEN","5089217311:AAEDNOmo_MYlu-eSldUeuwf_spGTZl0unHc")
	API_ID = int(os.environ.get("API_ID", 8626831))
	API_HASH = os.environ.get("API_HASH","db23330a6edf4a517ee186b35cedec71")
	STREAMTAPE_API_PASS = os.environ.get("STREAMTAPE_API_PASS", "pljJmMzYlAfRvO")
	STREAMTAPE_API_USERNAME = os.environ.get("STREAMTAPE_API_USERNAME", "7fe7a36c3e242c48a52c")
	LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL",-1001598625668))
	UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", -1001598625668)
	DOWN_PATH = os.environ.get("DOWN_PATH", "./downloads")
	PRESET = os.environ.get("PRESET", "ultrafast")
	OWNER_ID = int(os.environ.get("OWNER_ID", 1593338093))
	CAPTION = "By @Tanjiro_Aibot"
	BOT_USERNAME = os.environ.get("BOT_USERNAME", "Tanjiro_Aibot")
	DATABASE_URL = os.environ.get("DATABASE_URL","mongodb+srv://dbmab:eUtbAuei6mpLoinz@cluster0.r2c3m.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
	BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", True))
	ALLOW_UPLOAD_TO_STREAMTAPE = bool(os.environ.get("ALLOW_UPLOAD_TO_STREAMTAPE", True))
	USAGE_WATERMARK_ADDER = """
Hi, I am Video Watermark Adder Bot!

**How to Added Watermark to a Video?**
**Usage:** First Send a JPG Image/Logo, then send any Video. Better add watermark to a MP4 or MKV Video.

__Note: I can only process one video at a time. As my server is Heroku, my health is not good. If you have any issues with Adding Watermark to a Video, then please Report at [Dev](https://t.me/Sungjinwooarc).__

Desgined by @Sungjinwooarc
"""
	PROGRESS = """
Percentage : {0}%
Done ✅: {1}
Total 🌀: {2}
Speed 🚀: {3}/s
ETA 🕰: {4}
"""
