import os
from flask import Flask, request, render_template, jsonify, send_from_directory
import pandas as pd
from employment_analyzer import EmploymentAnalyzer
from employment_visualizer import EmploymentVisualizer

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure the upload folder exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return "No file part", 400
    
    file = request.files['file']
    
    if file.filename == '':
        return "No selected file", 400
    
    # Save the uploaded file to the uploads folder
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(filepath)

    # Read the CSV file into a DataFrame
    data = pd.read_csv(filepath)

    # Check for required columns
    required_columns = ['date', 'job_offers', 'placements', 'avg_salary', 'region', 'sector']
    if not all(col in data.columns for col in required_columns):
        return "Uploaded CSV must contain the following columns: " + ", ".join(required_columns), 400

    # Analyze the data
    analyzer = EmploymentAnalyzer(data)
    report = analyzer.generate_report()

    # Generate visualizations
    visualizer = EmploymentVisualizer(report)
    
    # Save figures to files in the uploads folder or a subdirectory for images
    monthly_trends_path = os.path.join(app.config['UPLOAD_FOLDER'], 'monthly_trends.png')
    visualizer.plot_monthly_trends(save=True, filename=monthly_trends_path)

    regional_performance_path = os.path.join(app.config['UPLOAD_FOLDER'], 'regional_performance.png')
    visualizer.plot_regional_performance(save=True, filename=regional_performance_path)

    sector_analysis_path = os.path.join(app.config['UPLOAD_FOLDER'], 'sector_analysis.png')
    visualizer.plot_sector_analysis(save=True, filename=sector_analysis_path)

    employment_clusters_path = os.path.join(app.config['UPLOAD_FOLDER'], 'employment_clusters.png')
    visualizer.plot_employment_clusters(save=True, filename=employment_clusters_path)

    # Render results page with data preview and visualizations
    data_preview_html = data.to_html(classes='data')
    
    return render_template('result.html',
                           data_preview=data_preview_html,
                           monthly_trends=monthly_trends_path,
                           regional_performance=regional_performance_path,
                           sector_analysis=sector_analysis_path,
                           employment_clusters=employment_clusters_path)

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == "__main__":
    app.run(debug=True)