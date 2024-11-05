import pandas as pd
import numpy as np
from datetime import datetime

class EmploymentDataGenerator:
    def __init__(self, start_date='2023-01-01', end_date='2023-12-31'):
        self.start_date = start_date
        self.end_date = end_date
        self.regions = [
            'Casablanca-Settat', 'Rabat-Salé-Kénitra', 
            'Fès-Meknès', 'Marrakech-Safi', 
            'Tanger-Tétouan-Al Hoceïma', 'Souss-Massa'
        ]
        self.sectors = [
            'Industrie', 'Services', 'Agriculture', 
            'Technologies', 'Tourisme'
        ]

    def generate_data(self):
        """Génère des données d'emploi réalistes"""
        dates = pd.date_range(start=self.start_date, end=self.end_date, freq='ME')
        data = []

        # Facteurs saisonniers pour rendre les données plus réalistes
        seasonal_factors = {
            'Tourisme': {1: 0.7, 6: 1.3, 7: 1.5, 8: 1.5},  # Haute saison en été
            'Agriculture': {3: 1.3, 4: 1.3, 9: 1.4, 10: 1.3},  # Périodes de récolte
            'Technologies': {1: 1.2, 9: 1.3}  # Pics de recrutement
        }

        for region in self.regions:
            # Facteurs régionaux
            regional_factor = 1.0
            if region == 'Casablanca-Settat':
                regional_factor = 1.5
            elif region == 'Rabat-Salé-Kénitra':
                regional_factor = 1.3

            for sector in self.sectors:
                for date in dates:
                    # Appliquer les facteurs saisonniers
                    seasonal_factor = seasonal_factors.get(sector, {}).get(date.month, 1.0)
                    
                    base_offers = np.random.normal(500, 100) * regional_factor * seasonal_factor
                    job_offers = max(int(base_offers), 0)
                    
                    # Calculer les placements en fonction de l'offre
                    placement_rate = np.random.uniform(0.4, 0.8)
                    placements = int(job_offers * placement_rate)
                    
                    # Salaire moyen avec variation par secteur et région
                    base_salary = 5000
                    if sector == 'Technologies':
                        base_salary *= 1.6
                    elif sector == 'Services':
                        base_salary *= 1.2
                    
                    avg_salary = int(np.random.normal(base_salary, base_salary * 0.1))
                    
                    data.append({
                        'date': date,
                        'region': region,
                        'sector': sector,
                        'job_offers': job_offers,
                        'placements': placements,
                        'avg_salary': avg_salary
                    })

        return pd.DataFrame(data)

    def save_data(self, data, filename='data/employment_data.csv'):
        """Sauvegarde les données générées"""
        data.to_csv(filename, index=False)
        print(f"Données sauvegardées dans {filename}")

if __name__ == "__main__":
    generator = EmploymentDataGenerator()
    data = generator.generate_data()
    generator.save_data(data)
