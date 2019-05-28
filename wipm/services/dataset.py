"""
@Author: NguyenKhacThanh
"""

import mongoengine.queryset as queryset
from wipm import models


def push_data(id_dataset, inputs, target=None):
    """Push data into dataset
    :param: data dict includes target[optional] and inputs
    :param: is_dataset string of bson object for document id in mongo
    :rtype None
    """
    dataset = _find_dataset_with_id(id_dataset)
    data = models.Data()
    data.inputs = inputs
    if target:
        data.target = target
    data.save()
    dataset.bucket.append(data)
    dataset.save()


def create_dataset():
    """Create new dataset
    :rtype: str
    """
    dataset = models.Dataset()
    dataset.save()
    return str(dataset.id)


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
