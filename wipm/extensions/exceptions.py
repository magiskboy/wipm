"""
@Author: NguyenKhacThanh
"""


def init_app(api):
    """Register function
    :param: app object of Api class
    """
    @api.errorhandler(Exception)
    def handle_exception(error):
        return {"message": str(error)}, 400
