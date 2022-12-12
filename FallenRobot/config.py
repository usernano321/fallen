class Config(object):
    LOGGER = True

  # Get this value from my.telegram.org/apps
    API_ID = 25924955
    API_HASH = "140d8d0ad7c45e934d82dfcbba019e0d"

    CASH_API_KEY = "MTUCS6JPUFR8XRPO"  # Get this value for currency converter from https://www.alphavantage.co/support/#api-key

    DATABASE_URL = "postgresql://howbutim:jZL_SB6ucCp9D5Tt2oS1i6ZpS85R-GeT@arjuna.db.elephantsql.com:27070/howbutim"  # A sql database url from elephantsql.com

    EVENT_LOGS = (-1001873253940)  # Event logs channel to note down important bot level events

    MONGO_DB_URI = "mongodb+srv://ilem:ilem@cluster0.uewtgbl.mongodb.net/?retryWrites=true&w=majority"  # Get ths value from cloud.mongodb.com

  # Telegraph link of the image which will be shown at start command.
    START_IMG = "https://te.legra.ph/file/63138bb89152d05cdff2d.jpg"

    SUPPORT_CHAT = "satpamajg"  # Your Telegram support group chat username where your users will go and bother you

    TOKEN = "5805856990:AAHixt2Cm-elIJAjDSmAqcEVx22CQfePUl8"  # Get bot token from @BotFather on Telegram

    TIME_API_KEY = "EYO2G96ONPI6"  # Get this value from https://timezonedb.com/api

    OWNER_ID = 1784179805  # User id of your telegram account (Must be integer)

  # Optional fields
    BL_CHATS = []  # List of groups that you want blacklisted.
    DRAGONS = []  # User id of sudo users
    DEV_USERS = []  # User id of dev users
    DEMONS = []  # User id of support users
    TIGERS = []  # User id of tiger users
    WOLVES = []  # User id of whitelist users

    ALLOW_CHATS = True
    ALLOW_EXCL = True
    DEL_CMDS = True
    INFOPIC = True
    LOAD = []
    NO_LOAD = []
    STRICT_GBAN = True
    TEMP_DOWNLOAD_DIRECTORY = "./"
    WORKERS = (8)

class Production(Config):
    LOGGER = True

class Development(Config):
    LOGGER = True
