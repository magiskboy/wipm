"""
@Author: NguyenKhacThanh
"""

from flask import request
from flask_restplus import Resource, Namespace
from wipm.services import dataset as serv_dataset
from ._requests import dataset as req_dataset
from ._responses import dataset as res_dataset


NS = Namespace("dataset", description="Dataset api")


@NS.route("", defaults={"id_dataset": None}, methods=["POST"])
@NS.route("/<string:id_dataset>", methods=["PUT", "DELETE"])
class Dataset(Resource):
    """Dataset resource class
    """
    @NS.expect(req_dataset.CREATE_DATASET_PARAMS, validate=True)
    @NS.marshal_with(res_dataset.CREATE_DATASET_RES, description="SUCCESS")
    def post(self, **kwargs):
        """Create dataset for push data
        """
        params = request.get_json()
        id_dataset = serv_dataset.create_dataset(**params)

        return {"message": "Create dataset success", "id": id_dataset}

    @NS.expect(req_dataset.PUSH_DATASET_PARAMS, validate=True)
    @NS.marshal_with(res_dataset.BASE_RES, description="SUCCESS")
    def put(self, id_dataset):
        """Push data into dataset
        :param: id_dataset str
        """
        content = request.get_json()
        serv_dataset.push_data(id_dataset, **content)

        return {"message": "Push data success"}

    @NS.marshal_with(res_dataset.BASE_RES, description="SUCCESS")
    def delete(self, id_dataset):
        """Delete dataset
        :param: id_dataset str
        """
        serv_dataset.delete_dataset(id_dataset)

        return {"message": "Delete dataset success"}
