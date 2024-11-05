from data_generator import EmploymentDataGenerator
from analyzer import EmploymentAnalyzer
from visualizer import EmploymentVisualizer

def main():
    # Générer les données d'emploi
    generator = EmploymentDataGenerator()
    data = generator.generate_data()
    generator.save_data(data)

    # Analyser les données
    analyzer = EmploymentAnalyzer(data)
    report = analyzer.generate_report()

    # Générer les visualisations
    visualizer = EmploymentVisualizer(report)
    visualizer.plot_monthly_trends()
    visualizer.plot_regional_performance()
    visualizer.plot_sector_analysis()
    visualizer.plot_employment_clusters()

    return report

if __name__ == "__main__":
    main()
