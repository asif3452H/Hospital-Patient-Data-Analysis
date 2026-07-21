
from services.data_loader import DataLoader
from services.analyzer import DataAnalyzer
from services.visualizer import Visualizer


def main():

    loader = DataLoader("data/patients.csv")

    df = loader.load_data()

    analyzer = DataAnalyzer(df)

    visualizer = Visualizer(df)

    analyzer.dataset_info()
    analyzer.statistics()
    analyzer.average_age()
    analyzer.average_cost()
    analyzer.patients_by_disease()
    analyzer.average_cost_by_disease()
    analyzer.average_age_by_city()

    visualizer.bar_chart()
    visualizer.histogram()
    visualizer.pie_chart()
    visualizer.box_plot()

    print("\nAnalysis Complete.")
    print("Charts saved inside images folder.")


if __name__ == "__main__":
    main()