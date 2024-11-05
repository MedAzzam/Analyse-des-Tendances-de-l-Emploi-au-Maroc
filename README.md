# Analyse des Tendances de l'Emploi au Maroc

## Description
Ce projet analyse les tendances de l'emploi au Maroc en utilisant des données simulées basées sur des patterns réels du marché du travail. Il fournit des insights sur les opportunités d'emploi par région, secteur et période.

## Objectifs
1. Analyser les tendances d'emploi par région et secteur
2. Identifier les clusters d'emploi
3. Générer des visualisations interactives avec Power BI
4. Fournir des recommandations pour l'adaptation des formations professionnelles

## Structure du Projet
```
emploi_maroc_analysis/
├── src/                 # Code source
├── data/               # Données brutes et traitées
├── visualizations/     # Graphiques et tableaux de bord
├── reports/            # Rapports d'analyse
├── requirements.txt    # Dépendances
└── README.md          # Documentation
```

## Installation
```bash
# Cloner le repository
git clone [URL_DU_REPO]

# Installer les dépendances
pip install -r requirements.txt
```

## Utilisation
1. Exécuter l'analyse principale :
   ```python
   python src/script_main.py
   ```
2. Ouvrir le dashboard Power BI dans `visualizations/dashboard.pbix`

## Technologies Utilisées
- Python 3.12+
- pandas, numpy pour l'analyse de données
- scikit-learn pour le clustering
- matplotlib, seaborn pour la visualisation
- Power BI pour les tableaux de bord interactifs
