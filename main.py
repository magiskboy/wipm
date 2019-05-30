"""
@Author: NguyenKhacThanh
"""

import os
import sentry_sdk
from sentry_sdk.integrations.flask import FlaskIntegration
from wipm import create_app

if os.environ.get("FLASK_ENV") == "production":
    SENTRY_KEY = os.environ.get("SENTRY_KEY", "")
    SENTRY_PROJECT = os.environ.get("SENTRY_PROJECT", "")
    sentry_sdk.init(
        dsn=f"https://{SENTRY_KEY}@sentry.io/{SENTRY_PROJECT}",
        integrations=[FlaskIntegration()]
    )
    print(f"Monitoring service by Sentry, project {SENTRY_PROJECT}")

app = create_app()
