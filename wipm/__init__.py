"""
@Author: NguyenKhacThanh
"""

from flask import Flask
from wipm import config
from wipm.extensions import cors
from wipm.extensions import exceptions
from wipm.extensions import logger
from wipm import models
from wipm import services
from wipm import api


def create_app():
    """Function factory
    """
    app = Flask(__name__)

    app.config.from_object(config)

    cors.init_app(app)
    logger.init_app(app)

    api.init_app(app)
    models.init_app(app)

    return app
