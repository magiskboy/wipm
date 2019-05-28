"""
@Author: NguyenKhacThanh
"""

from flask import Blueprint
from flask_restplus import Api

__all__ = ["init_app", "API"]


_BP = Blueprint("api", __name__)

API = Api(
    app=_BP,
    doc="/docs",
    description="WIPM backend"
)

def init_app(app):
    """Register blueprint for app
    """
    app.register_blueprint(_BP, url_prefix="/api/v1")


from .dataset import NS as dataset_ns
API.add_namespace(dataset_ns, path="/dataset")
