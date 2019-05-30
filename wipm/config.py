"""
@Author: NguyenKhacThanh
"""

import os


_ENV = os.environ

DEBUG = False or _ENV.get("DEBUG", "0") == "1"

TESTING = False or _ENV.get("TESTING", "0") == "1"

SECRET_KEY = _ENV.get("SECRET_KEY", "secret")

DB_HOST = _ENV.get("DB_HOST", "127.0.0.1")

DB_PORT = int(_ENV.get("DB_PORT", 27017))

DB_NAME = _ENV.get("DB_NAME", "wipm")
