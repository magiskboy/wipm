"""
@Author: NguyenKhacThanh
"""

import os
from datetime import datetime
import joblib
import pickle
import mongoengine as mongo


class Estimator(mongo.Document):
    """Store binary file for sklearn.base.Estimator
    """
    model = mongo.FileField(required=True)
    type_model = mongo.StringField(required=True)
    on_create = mongo.DateTimeField(default=datetime.now())
    is_trained = mongo.BooleanField(default=False)
    last_access = mongo.DateTimeField(default=None)


    def set_model(self, model):
        """Set model attribute
        :param: model, object of sklearn.base.BaseEstimator
        """
        bin_data = pickle.dumps(model)
        self.model.delete()
        self.model.put(bin_data)

        return self

    def get_model(self):
        """Load model binary file to python object
        """
        model = None
        if self.model:
            try:
                bin_data = self.model.read()
                model = pickle.loads(bin_data)
            except Exception as err:
                raise Exception("Load model fail")

        return model

    @classmethod
    def find(cls, id_estimator):
        """Find object with id
        """
        return cls.objects(id=id_estimator).first()

    def __str__(self):
        return str(self.id)
