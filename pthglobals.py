import os

RATE_LIMIT = 2.5
RATE_LIMIT_PUSHOVER = 5.0
RATE_LIMIT_PUSHBULLET = 5.0  # Note: This is just a guess, Pushbullet has a complex rate limiting system!

CONFIG_FILE = os.path.abspath(os.path.join(os.path.expanduser("~"), ".pthfree/config"))
CONFIG_SECTION = "pthfree"
CONFIG_USERNAME_ARG = "username"
CONFIG_PASSWORD_ARG = "password"

CONFIG_USE_SMTP_ARG = "use_smtp"
CONFIG_SMTP_SERVER_ARG = "smtp_server"
CONFIG_SMTP_PORT_ARG = "smtp_port"
CONFIG_SMTP_TLS_ARG = "smtp_tls"
CONFIG_SMTP_USER_ARG = "smtp_user"
CONFIG_SMTP_PASSWORD_ARG = "smtp_password"
CONFIG_SMTP_EMAIL_ARG = "smtp_email"
CONFIG_SENDTO_ARG = "send_to"

CONFIG_USE_PUSHOVER_ARG = "use_pushover"
CONFIG_PUSHOVER_API_TOKEN_ARG = "pushover_api_token"
CONFIG_PUSHOVER_USER_TOKEN_ARG = "pushover_user_token"

CONFIG_USE_PUSHBULLET_ARG = "use_pushbullet"
CONFIG_PUSHBULLET_ACCESS_TOKEN_ARG = "pushbullet_token"
# Pushbullet devices not yet supported by pthfree
# CONFIG_PUSHBULLET_USE_SPECIFIC_DEVICE = "pushbullet_use_device"
# CONFIG_PUSHBULLET_DEVICE_ID = "pushbullet_device"

DATABASE_FILE = os.path.abspath(os.path.join(os.path.expanduser("~"), ".pthfree/freeleeches.db"))

AJAX_PAGE = "https://passtheheadphones.me/ajax.php"
LOGIN_PAGE = "https://passtheheadphones.me/login.php"
LOGOUT_PAGE = "https://passtheheadphones.me/logout.php"
TORRENT_PAGE = "https://passtheheadphones.me/torrents.php"

PUSHOVER_API_TARGET = "https://api.pushover.net/1/messages.json"
PUSHBULLET_API_TARGET = "https://api.pushbullet.com/v2/pushes"
