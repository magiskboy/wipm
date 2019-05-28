"""
@Author: NguyenKhacThanh
"""

import mongoengine as mongo
from .data import Data
from .dataset import Dataset


__all__ = ["init_app", "Data", "Dataset"]


def init_app(app):
    """Python object mapping for mongo
    :param app Flask object
    :rtype None
    """
    mongo.connect(
        db=app.config["DB_NAME"],
        host=app.config["DB_HOST"],
        port=app.config["DB_PORT"]
    )
