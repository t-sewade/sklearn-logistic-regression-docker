from __future__ import print_function

import numpy as np
from sklearn.linear_model import LogisticRegression

import mlflow
import mlflow.sklearn

if __name__ == "__main__":
    X = np.array([-2, -1, 0, 1, 2, 1]).reshape(-1, 1)
    y = np.array([0, 0, 1, 1, 1, 0])
    lr = LogisticRegression()
    lr.fit(X, y)
    score = lr.score(X, y)
    mlflow.log_metric("score", score)
    mlflow.sklearn.log_model(lr, "model")
    print("Score: %s" % score)
    print("Model saved in run %s" % mlflow.active_run().info.run_uuid)
