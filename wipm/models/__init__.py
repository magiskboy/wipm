"""
@Author: NguyenKhacThanh
"""

import mongoengine as mongo
from .data import Data
from .dataset import Dataset
from .estimator import Estimator


__all__ = ["init_app", "Data", "Dataset", "Estimator"]


def init_app(app):
    """Python object mapping for mongo
    :param app Flask object
    :rtype None
    """
    @app.before_request
    def connect_database():
        mongo.connect(
            db=app.config["DB_NAME"],
            host=app.config["DB_HOST"],
            port=app.config["DB_PORT"]
        )
