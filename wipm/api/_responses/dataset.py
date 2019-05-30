"""
@Author: NguyenKhacThanh
"""

from flask_restplus import fields
from wipm.api import API as api
from . import BASE_RES


__all__ = ["CREATE_DATASET_RES"]


CREATE_DATASET_RES = api.inherit("CreateDatasetResponse", BASE_RES, {
    "id": fields.String(required=True, min_length=24, max_length=24)
})
