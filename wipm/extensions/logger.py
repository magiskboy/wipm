"""
@Author: NguyenKhacThanh
"""

import os
import logging
import logging.config


def init_app(app):
    """Logging register
    """
    gunicorn_logger = logging.getLogger("gunicorn.error")
    app.logger.handlers = gunicorn_logger.handlers
    app.logger.setLevel(gunicorn_logger.level)
    logging_config_path = os.path.join("etc", "logging.ini")
    logging.config.fileConfig(logging_config_path)
