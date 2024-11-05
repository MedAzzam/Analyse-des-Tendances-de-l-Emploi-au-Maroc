import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class EmploymentVisualizer:
    def __init__(self, report):
        self.report = report

    def plot_monthly_trends(self, filename='visualizations/monthly_trends.png'):
        """Trace les tendances mensuelles de l'emploi"""
        monthly_stats = self.report['monthly_trends']
        
        fig, ax1 = plt.subplots(figsize=(12, 6))
        
        # Tracer les lignes pour les offres d'emploi et les placements
        ax1.plot(monthly_stats['date'], monthly_stats['job_offers'], label='Offres d\'emploi', color='blue')
        ax1.plot(monthly_stats['date'], monthly_stats['placements'], label='Placements', color='orange')
        
        # Ajuster la position des étiquettes pour éviter le chevauchement
        for label in ax1.get_xticklabels():
            label.set_rotation(45)
            label.set_ha('right')
            label.set_fontsize(8)
        
        ax1.set_title('Tendances Mensuelles de l\'Emploi')
        ax1.set_xlabel('Date')
        ax1.set_ylabel('Nombre d\'offres et de placements', color='blue')
        ax1.tick_params(axis='y', labelcolor='blue')
        ax1.legend(loc='upper left')  # Place legend on the left side
        
        # Ajouter l'axe secondaire pour le taux de placement
        ax2 = ax1.twinx()
        ax2.plot(monthly_stats['date'], monthly_stats['placement_rate'], color='green', linestyle='--', label='Taux de Placement')
        ax2.set_ylabel('Taux de Placement (%)', color='green')
        ax2.tick_params(axis='y', labelcolor='green')
        ax2.legend(loc='upper right')  # Place legend on the right side
        
        # Ajuster la position des étiquettes de l'axe secondaire
        for label in ax2.get_yticklabels():
            label.set_fontsize(8)
        
        plt.savefig(filename)
        print(f"Graphique sauvegardé dans {filename}")

    def plot_regional_performance(self, filename='visualizations/regional_performance.png'):
        """Trace les performances régionales"""
        regional_stats = self.report['regional_analysis']
        
        fig, ax = plt.subplots(figsize=(14, 6))
        ax.bar(regional_stats['region'], regional_stats['job_offers'])
        ax.set_title('Performances Régionales')
        ax.set_xlabel('Région')
        ax.set_ylabel('Offres d\'emploi')
        ax.set_xticks(range(len(regional_stats['region'])))
        ax.set_xticklabels(regional_stats['region'], rotation=90)
        
        plt.savefig(filename)
        print(f"Graphique sauvegardé dans {filename}")

    def plot_sector_analysis(self, filename='visualizations/sector_analysis.png'):
        """Trace les analyses par secteur"""
        sector_stats = self.report['sector_analysis']
        
        fig, ax = plt.subplots(figsize=(12, 6))
        ax.bar(sector_stats['sector'], sector_stats['job_offers'])
        ax.set_title('Analyses par Secteur')
        ax.set_xlabel('Secteur')
        ax.set_ylabel('Offres d\'emploi')
        ax.set_xticks(range(len(sector_stats['sector'])))        
        ax.set_xticklabels(sector_stats['sector'], rotation=90)
        
        plt.savefig(filename)
        print(f"Graphique sauvegardé dans {filename}")

    def plot_employment_clusters(self, filename='visualizations/employment_clusters.png'):
        """Trace les clusters d'emploi"""
        regional_stats = self.report['employment_clusters']

        fig, ax = plt.subplots(figsize=(12, 6))

        # Créer un dictionnaire pour associer une couleur unique à chaque cluster
        cluster_colors = {0: 'r', 1: 'g', 2: 'b'}

        # Tracer les points avec leurs étiquettes
        for cluster, cluster_data in regional_stats.groupby('cluster'):
            ax.scatter(cluster_data['job_offers'], cluster_data['placement_rate'], 
                       color=cluster_colors[cluster], label=f'Cluster {cluster}')

            # Ajouter les étiquettes pour chaque point
            for i, (job_offers, placement_rate) in enumerate(zip(cluster_data['job_offers'], cluster_data['placement_rate'])):
                ax.text(job_offers, placement_rate, f'Cluster {cluster}', fontsize=8, 
                        ha='left', va='bottom', rotation=45)

        ax.set_title('Clusters d\'Emploi')
        ax.set_xlabel('Offres d\'emploi')
        ax.set_ylabel('Taux de Placement')
        ax.legend()

        plt.savefig(filename)
        print(f"Graphique sauvegardé dans {filename}")
