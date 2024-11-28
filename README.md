Analyse COVID-19 : Visualisation des données
Ce projet vise à analyser et visualiser les données relatives aux décès liés au COVID-19 par pays. L'objectif principal est d'identifier les 10 pays ayant enregistré le plus grand nombre de décès et de visualiser ces informations sous forme de graphique.

Contenu
Chargement et préparation des données
Nettoyage des colonnes et sélection des données pertinentes
Création d'une visualisation : Top 10 des pays avec le plus de décès
Prérequis
Bibliothèques Python utilisées :
pandas : Pour la manipulation des données
seaborn : Pour la création de visualisations
matplotlib : Pour la personnalisation des graphiques
Installation des dépendances
Assurez-vous d'avoir Python 3.7 ou une version ultérieure installée. Ensuite, installez les bibliothèques nécessaires avec la commande suivante :

bash
Copy code
pip install pandas seaborn matplotlib
Structure des fichiers
covid19.csv : Dataset contenant les données COVID-19 à analyser.
covid_analysis.py : Script Python pour exécuter l'analyse et générer la visualisation.
README.md : Documentation pour configurer et exécuter le projet.
Instructions
Clonez ce dépôt GitHub :

bash
Copy code
git clone https://github.com/<votre-utilisateur>/covid19-analysis.git
cd covid19-analysis
Assurez-vous que le fichier covid19.csv est dans le dossier du projet.

Exécutez le script Python :

bash
Copy code
python
Résultat attendu :

Un graphique s'affichera montrant les 10 pays ayant enregistré le plus de décès.
Exemple de sortie
Colonnes analysées :
text
Copy code
Colonnes disponibles : Index(['country/region', 'deaths'], dtype='object')
Graphique généré :
Un barplot montrant le Top 10 des pays avec le plus de décès liés au COVID-19.

Personnalisation
Si vous souhaitez inclure d'autres colonnes dans l'analyse, modifiez la section selected_columns dans le script Python.
Vous pouvez également ajuster les couleurs du graphique en modifiant la palette coolwarm dans la fonction sns.barplot.
Contributeur
Hajar Elhassak - Étudiante en Data Science
Pour toute question, contactez-moi sur LinkedIn.
