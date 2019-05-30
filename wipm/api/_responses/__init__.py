"""
@Author: NguyenKhacThanh
"""

from flask_restplus import fields
from wipm.api import API as api


BASE_RES = api.model("Base", {
    "message": fields.String()
})


ERROR_RES = api.model("ErrorResponse", {
    "message": fields.String(required=True, default="FAIL")
})


SUCCESS_RES = api.model("SuccessResponse", {
    "message": fields.String(required=True, default="SUCCESS")
})
