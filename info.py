from os import environ, getenv
import re
import os

id_pattern = re.compile(r"^.\d+$")


def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default


ADMIN = int(getenv("ADMIN", "5977931010"))
SILICON_PIC = os.environ.get("SILICON_PIC", "https://telegra.ph/file/21a8e96b45cd6ac4d3da6.jpg")
API_ID = int(getenv("API_ID", "12380656"))
API_HASH = str(getenv("API_HASH", "d927c13beaaf5110f25c505b7c071273"))
BOT_TOKEN = str(getenv("BOT_TOKEN", "7803613609:AAHI4VSou6Qs3Du38HSKbfG9_lqhwgyr1iY"))
FORCE_SUB = os.getenv("FORCE_SUB", "AV_BOTz_UPDATE") 
MONGO_DB = str(getenv("MONGO_DB", "mongodb+srv://ranjuvishwakarma50:aman@cluster0.uvah8.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0",))
DEF_CAP = str(
    getenv(
        "DEF_CAP",
        "<b>File Name:- `{file_name}`\n\n{file_size}</b>",
    )
)
