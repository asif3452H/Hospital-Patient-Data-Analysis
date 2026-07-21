

import matplotlib.pyplot as plt


class Visualizer:

    def __init__(self, df):
        self.df = df

    def bar_chart(self):
        self.df.groupby("Disease").size().plot(kind="bar")
        plt.title("Patients by Disease")
        plt.tight_layout()
        plt.savefig("images/bar_chart.png")
        plt.close()

    def histogram(self):
        plt.hist(self.df["Age"], bins=5)
        plt.title("Age Distribution")
        plt.tight_layout()
        plt.savefig("images/histogram.png")
        plt.close()

    def pie_chart(self):
        self.df.groupby("Disease").size().plot(kind="pie", autopct="%1.1f%%")
        plt.ylabel("")
        plt.tight_layout()
        plt.savefig("images/pie_chart.png")
        plt.close()

    def box_plot(self):
        plt.boxplot(self.df["Cost"])
        plt.title("Treatment Cost")
        plt.tight_layout()
        plt.savefig("images/boxplot.png")
        plt.close()