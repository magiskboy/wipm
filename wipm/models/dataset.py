"""
@Author: NguyenKhacThanh
"""

from datetime import datetime
import numpy as np
import mongoengine as mongo
from .data import Data


class Dataset(mongo.Document):
    """Dataset model
    """
    number_of_input = mongo.IntField(min_value=1)
    bucket = mongo.ListField(mongo.ReferenceField(Data))
    on_create = mongo.DateTimeField(default=datetime.now())

    def combine_data(self, sync=True):
        """Combine all data
        :return: tuple of ndarray
        """
        inputs, target = [], []
        for data in self.bucket:
            if len(data.target) == 0:
                if sync:
                    continue
            else:
                target.append(data.target)
            inputs.append(data.inputs)

        if len(target) < 1:
            raise Exception("Dataset error")
        elif len(target) == 1:
            inputs, target = inputs[0], target[0]
        else:
            inputs = np.concatenate(inputs, axis=0)
            target = np.concatenate(target, axis=0)

        return inputs, target

    @classmethod
    def find(cls, id_dataset):
        """Find dataset by id
        """
        return cls.objects(id=id_dataset).first()

    def __str__(self):
        return str(self.id)
