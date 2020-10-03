import pandas as pd
import numpy as np
import re

class DataLoader(object):
    def fit(self, dataset):
        self.dataset = dataset.copy()

    def load_data(self):
        self.dataset = self.dataset.drop('black', axis=1)
        return self.dataset
