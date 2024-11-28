import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Charger les données
df = pd.read_csv('C:\\Users\Admin\\Documents\\prog\\github\\country_covide19.csv')

# Nettoyer et harmoniser les noms de colonnes
df.columns = df.columns.str.strip().str.lower()  # Supprimer les espaces et mettre en minuscules

# Vérifier les colonnes disponibles
print("Colonnes disponibles :", df.columns)

    # Filtrer les colonnes nécessaires
selected_columns = df[['country/region', 'deaths']]
    
    # Supprimer les doublons ou lignes vides
selected_columns = selected_columns.dropna().drop_duplicates()
    
    # Trier les données par le nombre de cas confirmés
selected_columns = selected_columns.sort_values(by='deaths', ascending=False)
    
    # Afficher les premières lignes pour confirmer
print(selected_columns.head())

    # Créer un barplot des 10 pays ayant le plus de cas confirmés
plt.figure(figsize=(12, 8))
sns.barplot(data=selected_columns.head(10), x='deaths', y='country/region', palette='coolwarm')
plt.title("Top 10 des pays avec le plus de cas de morts")
plt.xlabel("Cas mort")
plt.ylabel("Pays")
plt.tight_layout()  # Ajuster la mise en page
plt.show()


