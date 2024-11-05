import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class EmploymentVisualizer:
    def __init__(self, report):
        self.report = report

    def plot_monthly_trends(self, save=False, filename='visualizations/monthly_trends.png'):
        """Trace les tendances mensuelles de l'emploi"""
        monthly_stats = self.report['monthly_trends']
        
        fig, ax1 = plt.subplots(figsize=(12, 6))
        ax1.plot(monthly_stats['date'], monthly_stats['job_offers'], label='Offres d\'emploi')
        ax1.plot(monthly_stats['date'], monthly_stats['placements'], label='Placements')
        ax1.set_title('Tendances Mensuelles de l\'Emploi')
        ax1.set_xlabel('Date')
        ax1.set_ylabel('Nombre')
        ax1.legend()
        
        ax2 = ax1.twinx()
        ax2.plot(monthly_stats['date'], monthly_stats['placement_rate'], color='g', label='Taux de Placement')
        ax2.set_ylabel('Taux de Placement (%)', color='g')
        ax2.tick_params('y', colors='g')
        ax2.legend()
        
        if save:
            plt.savefig(filename)  # Save the figure if requested
            plt.close(fig)  # Close the figure to free memory
        else:
            return fig
        # print(f"Graphique sauvegardé dans {filename}")

    def plot_regional_performance(self,save=False, filename='visualizations/regional_performance.png'):
        """Trace les performances régionales"""
        regional_stats = self.report['regional_analysis']
        
        fig, ax = plt.subplots(figsize=(14, 6))  # Increased width for better label visibility
        ax.bar(regional_stats['region'], regional_stats['job_offers'])
        ax.set_title('Performances Régionales')
        ax.set_xlabel('Région')
        ax.set_ylabel('Offres d\'emploi')
        
        ax.set_xticks(range(len(regional_stats['region'])))
        ax.set_xticklabels(regional_stats['region'], rotation=90)
        
        plt.tight_layout()
    
        if save:
            plt.savefig(filename)  
            plt.close(fig)  
        else:
            return fig        
        # print(f"Graphique sauvegardé dans {filename}")
    
    def plot_sector_analysis(self, save=False, filename='visualizations/sector_analysis.png'):
        """Trace les analyses par secteur"""
        sector_stats = self.report['sector_analysis']
        
        fig, ax = plt.subplots(figsize=(14, 6))  # Increased width for better label visibility
        ax.bar(sector_stats['sector'], sector_stats['job_offers'])
        ax.set_title('Analyses par Secteur')
        ax.set_xlabel('Secteur')
        ax.set_ylabel('Offres d\'emploi')
        
        ax.set_xticks(range(len(sector_stats['sector'])))
        ax.set_xticklabels(sector_stats['sector'], rotation=90)
        
        plt.tight_layout()
    
        if save:
            plt.savefig(filename)  
            plt.close(fig)  
        else:
            return fig        
        # print(f"Graphique sauvegardé dans {filename}")

    def plot_employment_clusters(self, save=False, filename='visualizations/employment_clusters.png'):
        """Trace les clusters d'emploi"""
        regional_stats = self.report['employment_clusters']
        
        fig, ax = plt.subplots(figsize=(12, 6))
        sns.scatterplot(x='job_offers', y='placement_rate', hue='cluster',
                        data=regional_stats, ax=ax)
        ax.set_title('Clusters d\'Emploi')
        ax.set_xlabel('Offres d\'emploi')
        ax.set_ylabel('Taux de Placement')
        
        if save:
            plt.savefig(filename)  
            plt.close(fig) 
        else:
            return fig
        print(f"Graphique sauvegardé dans {filename}")
