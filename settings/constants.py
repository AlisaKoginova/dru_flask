import os

DATA_FOLDER = 'app/data'
MODELS_FOLER = 'app/models'
TRAIN_CSV = os.path.join(DATA_FOLDER, 'train.csv')
VAL_CSV = os.path.join(DATA_FOLDER, 'val.csv')
SAVED_ESTIMATOR = os.path.join(MODELS_FOLER, 'LinearRegression.pickle')

