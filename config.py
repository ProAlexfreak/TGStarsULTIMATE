import os
from dotenv import load_dotenv

load_dotenv()

# ==============================
# Telegram Configuration
# ==============================

API_ID = int(os.getenv("APP_ID", "0"))
API_HASH = os.getenv("API_HASH", "")
BOT_TOKEN = os.getenv("TG_BOT_TOKEN", "")

# ==============================
# Owner & Admins
# ==============================

OWNER_ID = int(os.getenv("OWNER_ID", "0"))

ADMINS = [
    int(admin)
    for admin in os.getenv("ADMINS", "").split(",")
    if admin.strip()
]

# ==============================
# Database
# ==============================

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "mongodb://localhost:27017"
)

DATABASE_NAME = os.getenv(
    "DATABASE_NAME",
    "telegram_stars_bot"
)

# ==============================
# Bot Settings
# ==============================

BOT_USERNAME = os.getenv("BOT_USERNAME", "")
LOG_CHANNEL = int(os.getenv("LOG_CHANNEL", "0"))

DEBUG = os.getenv("DEBUG", "False").lower() == "true"

# ==============================
# Validation
# ==============================

if not BOT_TOKEN:
    raise ValueError("TG_BOT_TOKEN is missing.")

if API_ID == 0:
    raise ValueError("APP_ID is missing.")

if not API_HASH:
    raise ValueError("API_HASH is missing.")

if OWNER_ID == 0:
    raise ValueError("OWNER_ID is missing.")
