import os

API_ID = API_ID = 29693199

API_HASH = os.environ.get("API_HASH", "3f74b60e72e2bd8a3ebefed11c0e3e86")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "7497562785:AAGUEPUtmo1dUvCwK8wsf9jxBDhkXQEL6Ds")

PASS_DB = int(os.environ.get("PASS_DB", "721"))

OWNER = int(os.environ.get("OWNER", 6227196459))

LOG = -1002101213985

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "5987970971").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)


