

import numpy as np


class DataAnalyzer:

    def __init__(self, df):
        self.df = df

    def dataset_info(self):
        print(self.df.info())

    def statistics(self):
        print(self.df.describe())

    def average_age(self):
        print("Average Age:", np.mean(self.df["Age"]))

    def average_cost(self):
        print("Average Cost:", np.mean(self.df["Cost"]))

    def patients_by_disease(self):
        print(self.df.groupby("Disease").size())

    def average_cost_by_disease(self):
        print(self.df.groupby("Disease")["Cost"].mean())

    def average_age_by_city(self):
        print(self.df.groupby("City")["Age"].mean())