"""
@Author: NguyenKhacThanh
"""

import mongoengine as mongo
from wipm import models


def push_data(id_dataset, inputs, target=None):
    """Push data into dataset
    :param: data dict includes target[optional] and inputs
    :param: is_dataset string of bson object for document id in mongo
    :rtype None
    """
    data = models.Data()
    data.inputs = inputs
    if target:
        data.target = target
    data.save()
    if not models.Dataset.find(id_dataset):
        raise mongo.errors.DoesNotExist("Dataset not found")

    models.Dataset.objects(id=id_dataset).update_one(push__bucket=data)


def create_dataset(number_of_input):
    """Create new dataset
    :rtype: str
    """
    dataset = models.Dataset(number_of_input=number_of_input)
    dataset.save()

    return str(dataset)


def delete_dataset(id_dataset):
    """Delete dataset
    :rtype: None
    """
    dataset = _find_dataset_with_id(id_dataset)
    dataset.delete()


def _find_dataset_with_id(id_dataset):
    """Find dataset object with id
    :param: id_dataset, str
    :rtype: object of Document
    """
    dataset = models.Dataset.objects(id=id_dataset).first()
    if dataset is None:
        raise Exception("Dataset not found")

    return dataset
