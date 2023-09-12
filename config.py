import re
import sys
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

BOT_TOKEN = getenv("BOT_TOKEN")

MONGO_DB_URI = getenv("MONGO_DB_URI", None)
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID"))
MUSIC_BOT_NAME = getenv("MUSIC_BOT_NAME", "𝐃ɛʂꙷʈͦɪͧղͬ𝐘... ᴍᴜsɪᴄ")

OWNER_ID = list(map(int, getenv("OWNER_ID", "").split()))

HEROKU_API_KEY = getenv("HEROKU_API_KEY", None)
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME", None)

UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/rocks143014/DAXXMUSIC")
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = getenv("GIT_TOKEN", None)

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/XD_BOTSS")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "https://t.me/XD_SUPORT")

SUPPORT_HEHE = SUPPORT_GROUP.split("me/")[1]

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", "200"))
SONG_DOWNLOAD_DURATION = int(getenv("SONG_DOWNLOAD_DURATION_LIMIT", "200"))

AUTO_LEAVING_ASSISTANT = getenv("AUTO_LEAVING_ASSISTANT", "False")
AUTO_LEAVE_ASSISTANT_TIME = int(
    getenv("ASSISTANT_LEAVE_TIME", "5400")
)

AUTO_DOWNLOADS_CLEAR = getenv("AUTO_DOWNLOADS_CLEAR", "True")

PRIVATE_BOT_MODE = getenv("PRIVATE_BOT_MODE", None)

YOUTUBE_DOWNLOAD_EDIT_SLEEP = int(getenv("YOUTUBE_EDIT_SLEEP", "5"))
TELEGRAM_DOWNLOAD_EDIT_SLEEP = int(getenv("TELEGRAM_EDIT_SLEEP", "3"))

SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)

VIDEO_STREAM_LIMIT = int(getenv("VIDEO_STREAM_LIMIT", "5"))
SERVER_PLAYLIST_LIMIT = int(getenv("SERVER_PLAYLIST_LIMIT", "50"))
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", "50"))

CLEANMODE_DELETE_MINS = int(getenv("CLEANMODE_MINS", "12"))

TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", "104857600"))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", "1073741824"))
# https://www.gbmb.org/mb-to-bytes

STRING1 = getenv("STRING_SESSION", BQB_T-V-q4s-EwLaee3F86CkCEzrQxmXekziG7wYUnzPavj-esQssKj27NUCi5OOUE7Djr4Jv9657nAes6Sbj7gsA66Uod0Q58-6tGQ7J1O-XCDJWr1WX8Mkc0OOz6DirjADwf6N5mm45aZQWFaH64PAFpjKcbv3EckgozZ6K1Z6ut0D5A_k5hLLuboNLNgC9Q8tKMWseA1qe57XmyIJP8biV1KFITNexzKOjIEAZ35CFPJelWCWlqWJT4Dgzuo4KMeaBPP8112-EGdXwCCRhNh0Xc9sPK0Pf2YmFok7XVchxkNM5YRKiJwMAGqGC-UlFdNTK1akV9KYrHk31vPVlTSNAAAAATRG5uAA)
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)

BANNED_USERS = filters.user()
YTDOWNLOADER = 1
LOG = 2
LOG_FILE_NAME = "logs.txt"
adminlist = {}
lyrical = {}
chatstats = {}
userstats = {}
clean = {}
autoclean = []


START_IMG_URL = getenv("START_IMG_URL", "https://graph.org/file/3a2b010905848b0a27afc.jpg")

PING_IMG_URL = getenv(
    "PING_IMG_URL",
    "https://graph.org/file/471f5efc4676676c469b8.jpg",
)

PLAYLIST_IMG_URL = "https://graph.org/file/3a2b010905848b0a27afc.jpg"

GLOBAL_IMG_URL = "https://graph.org/file/471f5efc4676676c469b8.jpg"

STATS_IMG_URL = "https://graph.org/file/471f5efc4676676c469b8.jpg"

TELEGRAM_AUDIO_URL = "https://graph.org/file/2369dd282146c7dda1e4e.jpg"

TELEGRAM_VIDEO_URL = "https://graph.org/file/49bd3efbf9a4bb19fb328.jpg"

STREAM_IMG_URL = "https://graph.org/file/cb4bac927c1dc6c837976.jpg"

SOUNCLOUD_IMG_URL = "https://graph.org/file/46ed34b4e909e7e57d603.jpg"

YOUTUBE_IMG_URL = "https://graph.org/file/6e6cf1de5f139608ed431.jpg"

SPOTIFY_ARTIST_IMG_URL = "https://graph.org/file/d470d815c532cda21720d.jpg"

SPOTIFY_ALBUM_IMG_URL = "https://graph.org/file/d470d815c532cda21720d.jpg"

SPOTIFY_PLAYLIST_IMG_URL = "https://graph.org/file/46ed34b4e909e7e57d603.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(
        int(x) * 60**i
        for i, x in enumerate(reversed(stringt.split(":")))
    )


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))
SONG_DOWNLOAD_DURATION_LIMIT = int(
    time_to_seconds(f"{SONG_DOWNLOAD_DURATION}:00")
)


if UPSTREAM_REPO:
    if not re.match("(?:http|https)://", UPSTREAM_REPO):
        print(
            "[ERROR] - Your UPSTREAM_REPO url is wrong. Please ensure that it starts with https://"
        )
        sys.exit()

if PING_IMG_URL:
    if PING_IMG_URL != "assets/Ping.jpeg":
        if not re.match("(?:http|https)://", PING_IMG_URL):
            PING_IMG_URL = "https://graph.org/file/46ed34b4e909e7e57d603.jpg"

if START_IMG_URL:
    if START_IMG_URL != "assets/Ping.jpeg":
        if not re.match("(?:http|https)://", START_IMG_URL):
            START_IMG_URL = "https://graph.org/file/3a2b010905848b0a27afc.jpg"
