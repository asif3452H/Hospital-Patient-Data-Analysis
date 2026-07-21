

import pandas as pd


class DataLoader:

    def __init__(self, filename):
        self.filename = filename

    def load_data(self):
        return pd.read_csv(self.filename)