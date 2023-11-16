import os
from dotenv import load_dotenv

load_dotenv()

API_ID = os.getenv("API_ID", "21568806").strip()
API_HASH = os.getenv("API_HASH", "83c41043d5ada58ad3dc95652afa70d5").strip()
BOT_TOKEN = os.getenv("BOT_TOKEN", "6819381670:AAGHM2b7aJHP_GE0LnXI8elW9odocGopieA").strip()
DATABASE_URL = os.getenv("DATABASE_URL", "postgres://lkgzsfsd:Y6LWnnMLbUAcQ4QV2pTU_zcDJtfpz3hw@isabelle.db.elephantsql.com/lkgzsfsd").strip()
MUST_JOIN = os.getenv("MUST_JOIN", "@we_are_universee")

if not API_ID:
    print("No API_ID found. Exiting...")
    raise SystemExit
if not API_HASH:
    print("No API_HASH found. Exiting...")
    raise SystemExit
if not BOT_TOKEN:
    print("No BOT_TOKEN found. Exiting...")
    raise SystemExit
if not DATABASE_URL:
    print("No DATABASE_URL found. Exiting...")
    raise SystemExit

try:
    API_ID = int(API_ID)
except ValueError:
    print("API_ID is not a valid integer. Exiting...")
    raise SystemExit

if "postgres" in DATABASE_URL and "postgresql" not in DATABASE_URL:
    DATABASE_URL = DATABASE_URL.replace("postgres", "postgresql")
