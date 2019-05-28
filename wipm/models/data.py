"""
@Author: NguyenKhacThanh
"""

import mongoengine as mongo


class Data(mongo.Document):
    """Picce data in dataset
    """
    inputs = mongo.ListField(mongo.ListField(mongo.FloatField()),
                             required=True)
    target = mongo.ListField(mongo.FloatField())

    def __repr__(self):
        return f"Data: {str(self.id)}"

    def __str__(self):
        return str(self.id)
