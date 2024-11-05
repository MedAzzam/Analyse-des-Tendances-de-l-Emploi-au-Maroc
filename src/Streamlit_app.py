import streamlit as st
import pandas as pd
from employment_analyzer import EmploymentAnalyzer
from employment_visualizer import EmploymentVisualizer

def main():
    st.title("Employment Data Visualization App")

    # File uploader for CSV files
    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

    if uploaded_file is not None:
        try:
            # Read the CSV file into a DataFrame
            data = pd.read_csv(uploaded_file)

            # Check for required columns
            required_columns = ['date', 'job_offers', 'placements', 'avg_salary', 'region', 'sector']
            if not all(col in data.columns for col in required_columns):
                st.error("Uploaded CSV must contain the following columns: " + ", ".join(required_columns))
                return
            
            # Display the DataFrame
            st.write("Data Preview:")
            st.dataframe(data)

            # Analyser les données with loading indicator
            with st.spinner("Analyzing data..."):
                analyzer = EmploymentAnalyzer(data)
                report = analyzer.generate_report()

            # Générer les visualisations
            visualizer = EmploymentVisualizer(report)

            # Plotting functions with checkboxes for user selection
            if st.checkbox("Show Monthly Trends"):
                fig_monthly_trends = visualizer.plot_monthly_trends()
                st.pyplot(fig_monthly_trends)

            if st.checkbox("Show Regional Performance"):
                fig_regional_performance = visualizer.plot_regional_performance()
                st.pyplot(fig_regional_performance)

            if st.checkbox("Show Sector Analysis"):
                fig_sector_analysis = visualizer.plot_sector_analysis()
                st.pyplot(fig_sector_analysis)

            if st.checkbox("Show Employment Clusters"):
                fig_employment_clusters = visualizer.plot_employment_clusters()
                st.pyplot(fig_employment_clusters)

        except Exception as e:
            st.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()