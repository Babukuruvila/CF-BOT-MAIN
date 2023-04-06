import re
from os import environ

from Script import script

id_pattern = re.compile(r"^.\d+$")


def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default


# Bot information
SESSION = environ.get("SESSION", "Media_search")
API_ID = int(environ.get('API_ID', '19680279'))
API_HASH = environ.get('API_HASH', 'a32f974ade51b2dc74e8db4bb049ad01')
BOT_TOKEN = environ.get('BOT_TOKEN', '5394607721:AAFComt0NOGWyN92Du91Ak-D8byiZnMGT_I')
USER_SESSION = environ.get('USER_SESSION', 'AQEpr2kAUx4jbeIeLY2i7FMplptKQvI-wR6nfAkghJ9Ti0ruEjDs8XgQngnOD2eUZFPdJmizLj9lY6rJMULthK96cpSSTTDwdvApx8X6c148lS-xpYswCQVLQBwIFGZoHE52XvINPVlIeoahEhZ-v5lDFPPnTT1Tslsa5AUUTLvuqQLsbMM0fPAzITnBxzZdSwKXvIAkDx9s-09K_dfggN8Ao--ckGvdO4OpmnwKl-7ykRBVaiIakth-kqDvNSxVNL59rFx1Zt_eoUoiYXHK7A7SKrN_GXNkaWpsxNP1peijfGStrY7QtkpQCzCZAg1vScdpyUogYzHTSWBWlcxfe5xLyIo88wAAAAFKJzfwAA')
# Bot settings
CACHE_TIME = int(environ.get("CACHE_TIME", 300))
USE_CAPTION_FILTER = bool(environ.get("USE_CAPTION_FILTER", True))

PICS = (
    environ.get(
        'PICS',
        'https://telegra.ph/file/0c107cb24bbe1d55c43a7.jpg',
    )
).split()
NOR_IMG = environ.get("NOR_IMG", "https://telegra.ph/file/46443096bc6895c74a716.jpg")
MELCOW_VID = environ.get(
    "MELCOW_VID", "https://telegra.ph/file/38f0eb662349c122d28f5.mp4"
)
SPELL_IMG = environ.get(
    "SPELL_IMG", "https://telegra.ph/file/5e2d4418525832bc9a1b9.jpg"
)

# Admins, Channels & Users
ADMINS = [
    int(admin) if id_pattern.search(admin) else admin
    for admin in environ.get('ADMINS', '1129673243 5394954571').split()
]
CHANNELS = [
    int(ch) if id_pattern.search(ch) else ch
    for ch in environ.get('CHANNELS', '-1001532592684').split()
]
auth_users = [
    int(user) if id_pattern.search(user) else user
    for user in environ.get("AUTH_USERS", "").split()
]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []
auth_channel = environ.get('AUTH_CHANNEL', '-1001661898845')
auth_grp = environ.get('AUTH_GROUP')
AUTH_CHANNEL = (
    int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else None
)
AUTH_GROUPS = [int(ch) for ch in auth_grp.split()] if auth_grp else None
support_chat_id = environ.get('SUPPORT_CHAT_ID', '-1001679715980')
reqst_channel = environ.get('REQST_CHANNEL_ID', '-1001593500302')
REQST_CHANNEL = int(reqst_channel) if reqst_channel and id_pattern.search(reqst_channel) else None
SUPPORT_CHAT_ID = int(support_chat_id) if support_chat_id and id_pattern.search(support_chat_id) else None
NO_RESULTS_MSG = bool(environ.get("NO_RESULTS_MSG", "False"))

# MongoDB information
DATABASE_URI = environ.get('DATABASE_URI', "mongodb+srv://dulquer:dulquer@dulquer.betpe5w.mongodb.net/?retryWrites=true&w=majority")
DATABASE_NAME = environ.get('DATABASE_NAME', "dulquer")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Telegram_files')

# Others
DELETE_CHANNELS = [
    int(dch) if id_pattern.search(dch) else dch
    for dch in environ.get("DELETE_CHANNELS", "-1001564479472").split()
]
MAX_B_TN = environ.get("MAX_B_TN", "6")
MAX_BTN = is_enabled((environ.get("MAX_BTN", "True")), True)
GRP_LNK = environ.get("GRP_LNK", "https://t.me/CinemaFactory_Chat")
CHNL_LNK = environ.get("CHNL_LNK", "https://t.me/CinemaFactoryOfficiaI")
MSG_ALRT = environ.get("MSG_ALRT", "❤️")
LOG_CHANNEL = int(environ.get("LOG_CHANNEL", "-1001593500302"))
SUPPORT_CHAT = environ.get("SUPPORT_CHAT", "MCMovieRobot")
FILE_CHANNEL = int(environ.get('FILE_CHANNEL', '-1001884926609'))
FILE_CHANNEL_LINK = environ.get('FILE_CHANNEL_LINK', 'https://t.me/+85eFsWXgRMY3MDFl')
P_TTI_SHOW_OFF = is_enabled((environ.get("P_TTI_SHOW_OFF", "True")), False)
IMDB = is_enabled((environ.get("IMDB", "True")), True)
AUTO_FFILTER = is_enabled((environ.get('AUTO_FFILTER', "True")), True)
AUTO_DELETE = is_enabled((environ.get('AUTO_DELETE', "True")), True)
MAUTO_DELETE = is_enabled((environ.get('MAUTO_DELETE', "True")), True)
DELETE_TIME = int(environ.get('DELETE_TIME', 300))
SINGLE_BUTTON = is_enabled((environ.get("SINGLE_BUTTON", "True")), True)
CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", f"{script.CAPTION}")
BATCH_FILE_CAPTION = environ.get("BATCH_FILE_CAPTION", CUSTOM_FILE_CAPTION)
IMDB_TEMPLATE = environ.get("IMDB_TEMPLATE", f"{script.IMDB_TEMPLATE_TXT}")
LONG_IMDB_DESCRIPTION = is_enabled(environ.get("LONG_IMDB_DESCRIPTION", "True"), False)
SPELL_CHECK_REPLY = is_enabled(environ.get("SPELL_CHECK_REPLY", "False"), False)
MAX_LIST_ELM = environ.get("MAX_LIST_ELM", None)
INDEX_REQ_CHANNEL = int(environ.get("INDEX_REQ_CHANNEL", LOG_CHANNEL))
FILE_STORE_CHANNEL = [int(ch) for ch in (environ.get("FILE_STORE_CHANNEL", "-1001593500302")).split()]
MELCOW_NEW_USERS = is_enabled((environ.get("MELCOW_NEW_USERS", "False")), True)
PROTECT_CONTENT = is_enabled((environ.get("PROTECT_CONTENT", "False")), False)
PUBLIC_FILE_STORE = is_enabled((environ.get("PUBLIC_FILE_STORE", "True")), True)

LOG_STR = "Current Cusomized Configurations are:-\n"
LOG_STR += (
    "IMDB Results are enabled, Bot will be showing imdb details for you queries.\n"
    if IMDB
    else "IMBD Results are disabled.\n"
)
LOG_STR += (
    "P_TTI_SHOW_OFF found , Users will be redirected to send /start to Bot PM instead of sending file file directly\n"
    if P_TTI_SHOW_OFF
    else "P_TTI_SHOW_OFF is disabled files will be send in PM, instead of sending start.\n"
)
LOG_STR += (
    "SINGLE_BUTTON is Found, filename and files size will be shown in a single button instead of two separate buttons\n"
    if SINGLE_BUTTON
    else "SINGLE_BUTTON is disabled , filename and file_sixe will be shown as different buttons\n"
)
LOG_STR += (
    f"CUSTOM_FILE_CAPTION enabled with value {CUSTOM_FILE_CAPTION}, your files will be send along with this customized caption.\n"
    if CUSTOM_FILE_CAPTION
    else "No CUSTOM_FILE_CAPTION Found, Default captions of file will be used.\n"
)
LOG_STR += (
    "Long IMDB storyline enabled."
    if LONG_IMDB_DESCRIPTION
    else "LONG_IMDB_DESCRIPTION is disabled , Plot will be shorter.\n"
)
LOG_STR += (
    "Spell Check Mode Is Enabled, bot will be suggesting related movies if movie not found\n"
    if SPELL_CHECK_REPLY
    else "SPELL_CHECK_REPLY Mode disabled\n"
)
LOG_STR += (
    f"MAX_LIST_ELM Found, long list will be shortened to first {MAX_LIST_ELM} elements\n"
    if MAX_LIST_ELM
    else "Full List of casts and crew will be shown in imdb template, restrict them by adding a value to MAX_LIST_ELM\n"
)
LOG_STR += f"Your current IMDB template is {IMDB_TEMPLATE}"
