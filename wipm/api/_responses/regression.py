"""
@Author: NguyenKhacThanh
"""

from flask_restplus import fields
from wipm.api import API as api
from . import BASE_RES


CREATE_MODEL_RES = api.inherit("CreateModelResponse", BASE_RES, {
    "id": fields.String(desciption="model_id", required=True)
})


TRAIN_MODEL_BASE_RES = api.model("TrainModelBaseResponse", {
    "mean_squared_error": fields.Float(min=0, required=True),
    "mean_absolute_error": fields.Float(min=0, required=True)
})


TRAIN_NEURAL_NETWORK_MODEL_RES = api.inherit(
    "TrainNeuralNetworkResponse",
    TRAIN_MODEL_BASE_RES, {
        "loss_curve": fields.List(fields.Float, required=True, min_items=1)
    }
)
