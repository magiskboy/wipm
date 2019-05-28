"""
@Author: NguyenKhacThanh
"""

from flask_restplus import fields
from wipm.api import API as api


BASE_RES = api.model("Base", {
    "message": fields.String()
})
