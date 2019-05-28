"""
@Author: NguyenKhacThanh
"""

from flask_restplus import fields
from wipm.api import API as api


CREATE_DATASET_PARAMS = api.model("CreateDatasetParams", {
    "number_of_input": fields.Integer(min=1, required=True)
})


PUSH_DATASET_PARAMS = api.model("Data", {
    "target": fields.List(fields.Float, required=False),
    "inputs": fields.List(fields.List(fields.Float), required=True)
})
