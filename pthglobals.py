import os

RATE_LIMIT = 2.0

CONFIG_FILE = os.path.abspath(os.path.join(os.path.expanduser("~"), ".pthfree/config"))
CONFIG_SECTION = "pthfree"
CONFIG_USERNAME_ARG = "username"
CONFIG_PASSWORD_ARG = "password"
CONFIG_DIR_ARG = "directory"

AJAX_PAGE = "https://passtheheadphones.me/ajax.php"
LOGIN_PAGE = "https://passtheheadphones.me/login.php"
LOGOUT_PAGE = "https://passtheheadphones.me/logout.php"
TORRENT_PAGE = "https://passtheheadphones.me/torrents.php"
