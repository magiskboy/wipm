"""
@Author: NguyenKhacThanh
"""

from flask import request
from flask_restplus import Resource, Namespace
from wipm.services import regression as serv_regression
from ._requests import regression as req_regression
from ._responses import regression as res_regression
from ._responses import BASE_RES


NS = Namespace("regression", description="Regression algorithm")


@NS.route("/huber", methods=["POST", "PUT"])
class HuberCreate(Resource):
    """Huber Model resource class
    """
    @NS.expect(req_regression.CREATE_HUBER_MODEL_PARAMS, validate=True)
    @NS.marshal_with(res_regression.CREATE_MODEL_RES, description="SUCCESS")
    def post(self):
        """Create huber regression model
        """
        params = request.get_json()
        id_model = serv_regression.create_huber_model(**params)

        return {"id": id_model, "message": "SUCCESS"}

    @NS.expect(req_regression.TRAIN_MODEL_PARAMS)
    @NS.marshal_with(res_regression.TRAIN_MODEL_BASE_RES, description="SUCCESS")
    def put(self):
        """Train huber regression model
        """
        params = request.get_json()
        mean_squared_error, mean_absolute_error = serv_regression.train_estimator(**params)

        return {
            "mean_squared_error": mean_squared_error,
            "mean_absolute_error": mean_absolute_error
        }


@NS.route("/lasso", methods=["POST", "PUT"])
class LassoCreate(Resource):
    """"Lasso Model resource class
    """
    @NS.expect(req_regression.CREATE_LASSO_MODEL_PARAMS, validate=True)
    @NS.marshal_with(res_regression.CREATE_MODEL_RES, description="SUCCESS")
    def post(self):
        """Create lasso regression model
        """
        params = request.get_json()
        id_model = serv_regression.create_lasso_model(**params)

        return {"id": id_model, "message": "SUCCESS"}

    @NS.expect(req_regression.TRAIN_MODEL_PARAMS)
    @NS.marshal_with(res_regression.TRAIN_MODEL_BASE_RES, description="SUCCESS")
    def put(self):
        """Train lasso regression model
        """
        params = request.get_json()
        mean_squared_error, mean_absolute_error = serv_regression.train_estimator(**params)

        return {
            "mean_squared_error": mean_squared_error,
            "mean_absolute_error": mean_absolute_error
        }


@NS.route("/linear_regression", methods=["POST", "PUT"])
class LinearRegressionCreate(Resource):
    """Linear Regression Model resource class
    """
    @NS.expect(req_regression.CREATE_LINEAR_REGRESSION_MODEL_PARAMS, validate=True)
    @NS.marshal_with(res_regression.CREATE_MODEL_RES, code=200, description="SUCCESS")
    def post(self):
        """Create linear regression model
        """
        params = request.get_json()
        id_model = serv_regression.create_linear_regression_model(**params)

        return {"id": id_model, "message": "SUCCESS"}

    @NS.expect(req_regression.TRAIN_MODEL_PARAMS)
    @NS.marshal_with(res_regression.TRAIN_MODEL_BASE_RES, description="SUCCESS")
    def put(self):
        """Train linear regression model
        """
        params = request.get_json()
        mean_squared_error, mean_absolute_error = serv_regression.train_estimator(**params)
        return {
            "mean_squared_error": mean_squared_error,
            "mean_absolute_error": mean_absolute_error
        }
        pass


@NS.route("/decision_tree", methods=["POST", "PUT"])
class DecisionTreeCreate(Resource):
    """Decision Tree Regression Model resource class
    """
    @NS.expect(req_regression.CREATE_DECISION_TREE_MODEL_PARAMS, validate=True)
    @NS.marshal_with(res_regression.CREATE_MODEL_RES, description="SUCCESS")
    def post(self):
        """Create decision tree regression model
        """
        params = request.get_json()
        id_model = serv_regression.create_decision_tree_model(**params)

        return {"id": id_model, "message": "SUCCESS"}

    @NS.expect(req_regression.TRAIN_MODEL_PARAMS)
    @NS.marshal_with(res_regression.TRAIN_MODEL_BASE_RES, description="SUCCESS")
    def put(self):
        """Train decision tree regression model
        """
        params = request.get_json()
        mean_squared_error, mean_absolute_error = serv_regression.train_estimator(**params)
        return {
            "mean_squared_error": mean_squared_error,
            "mean_absolute_error": mean_absolute_error
        }


@NS.route("/random_forest", methods=["POST", "PUT"])
class RandomForestCreate(Resource):
    """Random Forest Model resource class
    """
    @NS.expect(req_regression.CREATE_RANDOM_FOREST_MODEL_PARAMS,
               validate=True)
    @NS.marshal_with(res_regression.CREATE_MODEL_RES, description="SUCCESS")
    def post(self):
        """Create random forest regression model
        """
        params = request.get_json()
        id_model = serv_regression.create_random_forest_model(**params)

        return {"id": id_model, "message": "SUCCESS"}

    @NS.expect(req_regression.TRAIN_MODEL_PARAMS)
    @NS.marshal_with(res_regression.TRAIN_MODEL_BASE_RES, description="SUCCESS")
    def put(self):
        """Train random forset regression model
        """
        params = request.get_json()
        mean_squared_error, mean_absolute_error = serv_regression.train_estimator(**params)
        return {
            "mean_squared_error": mean_squared_error,
            "mean_absolute_error": mean_absolute_error
        }


@NS.route("/xgboost", methods=["POST", "PUT"])
class XGBoostCreate(Resource):
    """XGBoost Model resource class
    """
    @NS.expect(req_regression.CREATE_XGBOOST_MODEL_PARAMS, validate=True)
    @NS.marshal_with(res_regression.CREATE_MODEL_RES, description="SUCCESS")
    def post(self):
        """Create huber regression model
        """
        params = request.get_json()
        id_model = serv_regression.create_xgboost_model(**params)

        return {"id": id_model, "message": "SUCCESS"}

    @NS.expect(req_regression.TRAIN_MODEL_PARAMS)
    @NS.marshal_with(res_regression.TRAIN_MODEL_BASE_RES, description="SUCCESS")
    def put(self):
        """Train xgboost regression model
        """
        params = request.get_json()
        mean_squared_error, mean_absolute_error = serv_regression.train_estimator(**params)

        return {
            "mean_squared_error": mean_squared_error,
            "mean_absolute_error": mean_absolute_error
        }


@NS.route("/neural_network", methods=["POST", "PUT"])
class NeuralNetworkCreate(Resource):
    """Neural Network Model resource class
    """
    @NS.expect(req_regression.CREATE_NEURAL_NETWORK_MODEL_PARAMS,
               validate=True)
    @NS.marshal_with(res_regression.CREATE_MODEL_RES, description="SUCCESS")
    def post(self):
        """Create neural network regression model
        """
        params = request.get_json()
        id_model = serv_regression.create_neural_network_model(**params)

        return {"id": id_model, "message": "SUCCESS"}

    @NS.expect(req_regression.TRAIN_MODEL_PARAMS)
    @NS.marshal_with(res_regression.TRAIN_NEURAL_NETWORK_MODEL_RES,
                     description="SUCCESS")
    def put(self):
        """Train neural network regression model
        """
        params = request.get_json()
        mean_squared_error, mean_absolute_error, loss_curve = \
                serv_regression.train_estimator(**params)

        return {
            "mean_squared_error": mean_squared_error,
            "mean_absolute_error": mean_absolute_error,
            "loss_curve": loss_curve
        }


@NS.route("/<string:id_model>", methods=["DELETE"])
class DeleteModel(Resource):
    """Delete model
    """
    @NS.marshal_with(BASE_RES, description="SUCCESS")
    def delete(self, id_model):
        """Delete model api
        """
        serv_regression.delete_estimator(id_model)

        return {"message": "Delete success"}
