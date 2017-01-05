import os

RATE_LIMIT = 2.5
RATE_LIMIT_PUSHOVER = 5.0

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

DATABASE_FILE = os.path.abspath(os.path.join(os.path.expanduser("~"), ".pthfree/freeleeches.db"))

AJAX_PAGE = "https://passtheheadphones.me/ajax.php"
LOGIN_PAGE = "https://passtheheadphones.me/login.php"
LOGOUT_PAGE = "https://passtheheadphones.me/logout.php"
TORRENT_PAGE = "https://passtheheadphones.me/torrents.php"

PUSHOVER_API_TARGET = "https://api.pushover.net/1/messages.json"
