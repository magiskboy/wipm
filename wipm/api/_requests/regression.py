"""
@Author: NguyenKhacThanh
"""

from flask_restplus import fields
from wipm.api import API as api


CREATE_HUBER_MODEL_PARAMS = api.model("CreateHuberModelParams", {
    "epsilon": fields.Float(min=1, default=1.35, \
            description="The parameter epsilon controls the number of \
                        samples that should be classified as outliers.\
                        The smaller the epsilon, the more robust it\
                        is to outliers."
            ),
    "max_iter": fields.Integer(min=1, default=1000, max=20000, \
            description="Maximum number of iterations that \
            scipy.optimize.fmin_l_bfgs_b should run for."
            ),
    "tol": fields.Float(min=1e-5, default=1e-5,\
            description="The iteration will stop when max{|proj g_i |i = 1, \
                        ..., n} <= tol where pg_i is the i-th component of \
                        the projected gradient."
            ),
    "alpha": fields.Float(min=0.0001, default=0.0001, \
            description="Regularization parameter.")
})


CREATE_LINEAR_REGRESSION_MODEL_PARAMS = api.model(
    "CreateLinearRegressionModelParams", {
        "normalize": fields.Boolean(default=False, \
                description="If True, the regressors X will be normalized \
                before regression by subtracting the mean and dividing by\
                the l2-norm"
            )
    }
)


CREATE_LASSO_MODEL_PARAMS = api.model("CreateLassoModelParams", {
    "max_iter": fields.Integer(min=1, default=1000, max=20000, \
            description="Maximum number of iterations that \
            scipy.optimize.fmin_l_bfgs_b should run for."
            ),
    "tol": fields.Float(min=1e-5, default=1e-5,\
            description="The iteration will stop when max{|proj g_i |i = 1, \
                        ..., n} <= tol where pg_i is the i-th component of \
                        the projected gradient."
            ),
    "alpha": fields.Float(min=0.0001, default=0.0001, \
            description="Regularization parameter."),
    "random_state": fields.Integer(min=-1, default="-1", \
            description="The seed of the pseudo random number generator \
            that selects a random feature to update")
})


CREATE_DECISION_TREE_MODEL_PARAMS = api.model(
        "CreateDecisionTreeRegressionParams", {
            "max_depth": fields.Integer(min=0, default=0, \
                    description="The maximum depth of the tree. If None,\
                    then nodes are expanded until all leaves are pure or until all \
                    leaves contain less than min_samples_split samples."),
            "max_features": fields.Integer(min=0, default=0, \
                    description="The number of features to consider when looking \
                    for the best split."),
            "min_samples_split": fields.Integer(min=2, default=2, \
                    description="The minimum number of samples required to split an \
                    internal node:"),
            "random_state": fields.Integer(min=-1, default=-1,\
                    description="random_state is the seed used by the random number \
                    generator")
        }
) 


CREATE_RANDOM_FOREST_MODEL_PARAMS = api.model(
        "CreateDecisionTreeRegressionParams", {
            "n_estimators": fields.Integer(min=1, default=10,\
                    description="The number of trees in the forest."),
            "max_depth": fields.Integer(min=0, default=0, \
                    description="The maximum depth of the tree. If None,\
                    then nodes are expanded until all leaves are pure or until all \
                    leaves contain less than min_samples_split samples."),
            "max_features": fields.Integer(min=0, default=0, \
                    description="The number of features to consider when looking \
                    for the best split."),
            "min_samples_split": fields.Integer(min=2, default=2, \
                    description="The minimum number of samples required to split an \
                    internal node:"),
            "random_state": fields.Integer(min=-1, default=-1,\
                    description="random_state is the seed used by the random number \
                    generator")
        }
) 


CREATE_XGBOOST_MODEL_PARAMS = api.model("CreateXGBoostModelParams", {
    "booster": fields.String(enum=("gbtree", "dart")),
    "eta": fields.Float(min=1e-5, max=1, default=0.3, \
            description="learning rate"),
    "gamma": fields.Float(min=0, default=0, \
            description="Minimum loss reduction required to make a \
            further partition on a leaf node of the tree. The larger gamma \
            is, the more conservative the algorithm will be."),
    "max_depth": fields.Integer(min=1, default=6,\
            description="Maximum depth of a tree. Increasing this value \
            will make the model more complex and more likely to overfit."),
    "lambda": fields.Float(min=0, default=1, \
            desciption="L2 regularization term on weights. Increasing this\
            value will make model more conservative."),
    "alpha": fields.Float(min=0, default=0, \
            description="L1 regularization term on weights. Increasing \
            this value will make model more conservative."),
    "rate_drop": fields.Float(min=0, max=1, \
            description="Dropout rate (a fraction of previous trees to drop\
            during the dropout)."),
    "skip_drop": fields.Float(min=0, max=1, \
            description="Probability of skipping the dropout procedure \
            during a boosting iteration.")
})


CREATE_NEURAL_NETWORK_MODEL_PARAMS = api.model(
        "CreateNeuralNetworkModelParams", {
            "activation": fields.String(
                enum=("identity", "logistic", "tanh", "relu"),
                description="Activation function for the hidden layer."
            ),
            "solver": fields.String(enum=("adam", "sgd", "lbfgs"), \
                    description="The solver for weight optimization."),
            "alpha": fields.Float(min=1e-5, default=0.0001, \
                    description="L2 penalty (regularization term) parameter."),
            "batch_size": fields.Integer(min=1, default=200, \
                    description="Size of minibatches for stochastic \
                    optimizers. If the solver is ‘lbfgs’, the classifier\
                    will not use minibatch."),
            "learning_rate_init": fields.Float(min=1e-5, default=1e-3,\
                    description="The initial learning rate used. \
                    It controls the step-size in updating the weights.\
                    Only used when solver=’sgd’ or ‘adam’."),
            "max_iter": fields.Float(min=1, default=200, \
                    description="Maximum number of iterations."),
            "random_state": fields.Integer(min=-1, default=-1, \
                    description="random_state is the seed used by the \
                    random number generator;"),
            "tol": fields.Float(min=1e-4, default=1e-4, \
                    description="Tolerance for the optimization."),
            "early_stopping": fields.Boolean(default=False, \
                    description="Whether to use early stopping to terminate \
                    training when validation score is not improving."),
            "hidden_layer_sizes": fields.List(fields.Integer(min=1, max=1000),\
                    min_items=1, max_items=10, \
                    description="The ith element represents the number of \
                    neurons in the ith hidden layer.")
        }
)


TRAIN_MODEL_PARAMS = api.model("TrainModelParams", {
    "id_model": fields.String(length=24, required=True),
    "id_dataset": fields.String(length=24, required=True)
})
