"""
@Author: NguyenKhacThanh
"""

from datetime import datetime
import mongoengine as mongo
from .data import Data


class Dataset(mongo.Document):
    """Dataset model
    """
    number_of_input = mongo.IntField(min_value=1)
    bucket = mongo.ListField(mongo.ReferenceField(Data))
    on_create = mongo.DateTimeField(default=datetime.now())

    def __repr__(self):
        return f"Data: {str(self.id)}"

    def __str__(self):
        return str(self.id)
