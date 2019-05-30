"""
@Author: NguyenKhacThanh
"""

from flask import Blueprint
from flask_restplus import Api
from wipm import exceptions

__all__ = ["init_app", "API"]


_BP = Blueprint("api", __name__)

API = Api(
    app=_BP,
    doc="/docs",
    description="WIPM backend"
)
exceptions.init_app(API)

def init_app(app):
    """Register blueprint for app
    """
    app.register_blueprint(_BP, url_prefix="/api/v1")


from .dataset import NS as dataset_ns
from .regression import NS as regression_ns

API.add_namespace(dataset_ns, path="/dataset")
API.add_namespace(regression_ns, path="/regression")
