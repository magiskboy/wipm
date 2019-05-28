"""
@Author: NguyenKhacThanh
"""

__all__ = ["init_app"]


def _after_request(response):
    """Add headers to after request
    """
    # allowed_origins = [
    #     re.compile("http?://(.*\.)?i2g\.vn"),
    # ]

    # origin = flask.request.headers.get("Origin")
    # if origin:
    #     for allowed_origin in allowed_origins:
    #         if allowed_origin.match(origin):
    #             response.headers["Access-Control-Allow-Origin"] = origin

    # response.headers["Access-Control-Allow-Credentials"] = "true"
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Methods"] = \
            "GET, POST, PUT, DELETE, OPTIONS"
    response.headers["Access-Control-Allow-Headers"] = \
            "Origin, X-Requested-With, Content-Type, Accept, Authorization"

    return response


def init_app(app):
    """Fixed error CORS
    :param app Flask object
    :rtype None
    """
    app.after_request(_after_request)
