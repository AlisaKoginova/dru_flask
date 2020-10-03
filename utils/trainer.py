from sklearn.linear_model import LinearRegression

class Estimator:
    @staticmethod
    def fit(train_x, train_y):
        return LinearRegression().fit(train_x, train_y)
    

    @staticmethod
    def predict(trained, test_x):
        return trained.predict(test_x)
