"""
@Author: NguyenKhacThanh
"""

from sklearn import metrics
from sklearn.model_selection import train_test_split
from sklearn import linear_model
from sklearn.neural_network import MLPRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from xgboost import XGBRegressor
from wipm import models


def _evaluate_model(model, x_test, y_test):
    """Evaluate estimator
    :param: model object of sklearn.base.BaseEstimator
    :param: x_test, float ndarray with (m, n)
    :param: y_test, float ndarray with (m, )
    :return: tuple of (mean_squared_error, mean_absolute_error
    """
    y_pred = model.predict(x_test)
    mse = metrics.mean_squared_error(y_test, y_pred)
    mae = metrics.mean_absolute_error(y_test, y_pred)

    return mse, mae

def _save_estimator(model, type_model):
    """Wrap model into models.Estimator and save to Mongo
    :param: model, object of sklearn.base.BaseEstimator
    :param: type_model, str
    :return: str, id of object in Mongo
    """
    estimator = models.Estimator(type_model=type_model)
    estimator.set_model(model)
    estimator.save()

    return str(estimator)


def create_huber_model(**kwargs):
    """Create huber regression
    :return: id_model, unique str
    """
    model = linear_model.HuberRegressor(**kwargs)
    id_model = _save_estimator(model=model, type_model="huber_regression")

    return id_model


def create_linear_regression_model(**kwargs):
    """Create linear regression
    :return: id_model, unique str
    """
    model = linear_model.LinearRegression(**kwargs)
    id_model = _save_estimator(model=model, type_model="linear_regression")

    return id_model


def create_lasso_model(**kwargs):
    """Create lasso regression
    :return: id_model, unique str
    """
    model = linear_model.Lasso(**kwargs)
    id_model = _save_estimator(model=model, type_model="lasso_regression")

    return id_model


def create_decision_tree_model(**kwargs):
    """Create decision tree regression
    :return: id_model, unique str
    """
    model = DecisionTreeRegressor(**kwargs)
    id_model = _save_estimator(model=model, type_model="decision_tree_regression")

    return id_model


def create_random_forest_model(**kwargs):
    """Create random_forest regression
    :return: id_model, unique str
    """
    model = RandomForestRegressor(**kwargs)
    id_model = _save_estimator(model=model, type_model="random_forest_regression")

    return id_model


def create_xgboost_model(**kwargs):
    """Create xgboost regression
    :return: id_model, unique str
    """
    model = XGBRegressor(**kwargs)
    id_model = _save_estimator(model=model, type_model="xgboost_regression")

    return id_model


def create_neural_network_model(**kwargs):
    """Create neural network regression
    :return: id_model, unique str
    """
    model = MLPRegressor(**kwargs)
    id_model = _save_estimator(model=model, type_model="neural_network_regression")

    return id_model


def train_estimator(id_model, id_dataset, test_size=0.1):
    """Train machine learning model extennd sklearn.base.BaseEstimator
    :param: id_model, str
    :param: id_dataset, str
    :return: tuple of (mean_squared_error, mean_absolute_error)
    if type_model is 'neural_network', result include loss_curve
    """
    # load dataset
    dataset = models.Dataset.find(id_dataset)
    if not dataset:
        raise Exception("Dataset not found")
    inputs, target = dataset.combine_data()
    if not inputs or not target:
        raise Exception("Dataset invalid")

    # load model
    estimator = models.Estimator.find(id_model)
    if not estimator:
        raise Exception("Model not found")
    model = estimator.get_model()

    # prepare data
    x_train, x_test, y_train, y_test = train_test_split(
        inputs, target, test_size=test_size)

    # train model
    model.fit(x_train, y_train)

    # evaluate and save model
    result = _evaluate_model(model, x_test, y_test)
    if estimator.type_model == "neural_network_regression":
        loss_curve = model.loss_curve_
        result = tuple(list([*result, loss_curve]))
    estimator.set_model(model)
    estimator.save()

    return result


def delete_estimator(id_model):
    """Delete estimator object in mongodb
    :param: id_model, str
    :return: None
    """
    estimator = models.Estimator.find(id_model)
    if estimator is None:
        raise Exception("Model not found")
    estimator.model.delete()
    estimator.delete()
