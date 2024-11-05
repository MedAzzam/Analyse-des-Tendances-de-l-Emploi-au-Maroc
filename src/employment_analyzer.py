import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

class EmploymentAnalyzer:
    def __init__(self, data):
        self.data = data
        self.monthly_stats = None
        self.regional_stats = None
        self.sector_stats = None

    def compute_monthly_trends(self):
        """Calcule les tendances mensuelles de l'emploi"""
        self.monthly_stats = self.data.groupby('date').agg({
            'job_offers': 'sum',
            'placements': 'sum',
            'avg_salary': 'mean'
        }).reset_index()
        
        self.monthly_stats['placement_rate'] = (
            self.monthly_stats['placements'] / self.monthly_stats['job_offers'] * 100
        )
        return self.monthly_stats

    def analyze_regional_performance(self):
        """Analyse les performances par région"""
        self.regional_stats = self.data.groupby('region').agg({
            'job_offers': 'sum',
            'placements': 'sum',
            'avg_salary': 'mean'
        }).reset_index()
        
        self.regional_stats['placement_rate'] = (
            self.regional_stats['placements'] / self.regional_stats['job_offers'] * 100
        )
        return self.regional_stats

    def sector_analysis(self):
        """Analyse les tendances par secteur"""
        self.sector_stats = self.data.groupby('sector').agg({
            'job_offers': 'sum',
            'placements': 'sum',
            'avg_salary': 'mean'
        }).reset_index()
        
        self.sector_stats['placement_rate'] = (
            self.sector_stats['placements'] / self.sector_stats['job_offers'] * 100
        )
        return self.sector_stats

    def identify_employment_clusters(self):
        """Identifie les clusters d'emploi basés sur les indicateurs clés"""
        # Préparer les données pour le clustering
        cluster_data = self.regional_stats[['job_offers', 'placement_rate', 'avg_salary']]
        scaler = StandardScaler()
        scaled_data = scaler.fit_transform(cluster_data)
        
        # Appliquer K-means
        kmeans = KMeans(n_clusters=3, random_state=42)
        self.regional_stats['cluster'] = kmeans.fit_predict(scaled_data)
        
        return self.regional_stats

    def generate_report(self):
        """Génère un rapport complet d'analyse"""
        report = {
            'summary': {
                'total_job_offers': self.data['job_offers'].sum(),
                'total_placements': self.data['placements'].sum(),
                'average_placement_rate': (self.data['placements'].sum() / 
                                        self.data['job_offers'].sum() * 100),
                'average_salary': self.data['avg_salary'].mean()
            },
            'monthly_trends': self.compute_monthly_trends(),
            'regional_analysis': self.analyze_regional_performance(),
            'sector_analysis': self.sector_analysis(),
            'employment_clusters': self.identify_employment_clusters()
        }
        return report
