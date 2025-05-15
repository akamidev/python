# 🧹 Nettoyage Automatique des Fichiers Temporaires

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python)
![Windows](https://img.shields.io/badge/OS-Windows-0078D6?logo=windows)
![License](https://img.shields.io/badge/License-MIT-yellow)
![Status](https://img.shields.io/badge/Automatisé-Planificateur_de_tâches-green)

## Description 📄

Ce projet propose un script Python qui permet de **supprimer automatiquement les fichiers temporaires** accumulés dans les dossiers de cache système, tels que `%TEMP%` sous Windows. Ce script est idéal pour maintenir ton système propre et éviter l'encombrement du disque dû aux fichiers inutiles laissés par divers programmes.

> **Pourquoi ce projet ?**  
> Les fichiers temporaires peuvent rapidement consommer beaucoup d'espace disque et affecter la performance du système. Ce projet est conçu pour automatiser la suppression de ces fichiers, simplifiant ainsi l'entretien du système.

## Fonctionnalités 🔧

- ✅ Supprime automatiquement les fichiers temporaires dans les chemins prédéfinis.
- ✅ Facile à personnaliser pour ajouter d'autres répertoires à nettoyer.
- ✅ Peut être exécuté manuellement ou automatisé avec le **Planificateur de tâches** Windows.
- ✅ Journaux en console pour afficher les fichiers et dossiers supprimés.
- ✅ Réduit la charge sur le disque et améliore les performances du système.

## Installation 📥

### Prérequis

Assure-toi d'avoir Python installé sur ton système.

1. **Télécharger Python** : [Installer Python](https://www.python.org/downloads/)

2.  **Vérifier l'installation de Python** :
   
   - Ouvre une invite de commande et tape :
     
   ```bash
   python --version
   ```
     Cela doit afficher la version de Python.

### Étapes d'installation

1. **Cloner ce repository** sur ton système :
   
   ```bash
   git clone https://github.com/tonutilisateur/nettoyage-temp-python.git

### Naviguer dans le répertoire du projet :

   ```bash
   cd nettoyage-temp-python
   ```
### Exécuter le script :

   ```bash
   python nettoyage_temp.py
   ```
   
### Personnalisation ⚙️

Par défaut, le script nettoie les fichiers dans les répertoires temporaires de Windows. Cependant, tu peux personnaliser les dossiers à nettoyer.

Dans le fichier **nettoyage_temp.py** modifie la variable **folders_to_clean** pour ajouter d'autres chemins à nettoyer :

   ```bash
   folders_to_clean = [
    os.getenv('TEMP'),  # Dossier temporaire principal
    os.path.join(os.getenv('USERPROFILE'), 'AppData', 'Local', 'Temp'),  # %temp%
    # Tu peux ajouter d'autres chemins ici :
    # 'C:\\Chemin\\Vers\\Autre\\Dossier',
]
   ```

### Automatisation 🕒

Planifier l'exécution automatique du script avec le Planificateur de tâches Windows
Ouvrir le Planificateur de tâches :

Dans le menu démarrer de Windows, tape **"Planificateur de tâches"** et ouvre l'application.
Créer une nouvelle tâche :

Dans le menu à droite, clique sur Créer une tâche.
Donne un nom à ta tâche, par exemple Nettoyage Temporaire.
Coche Exécuter avec les autorisations maximales pour garantir que la tâche a les droits nécessaires.

### Configurer le déclencheur :

Va dans l'onglet Déclencheurs et clique sur Nouveau.
Choisis quand tu veux que la tâche se déclenche, par exemple tous les jours à une heure spécifique.
Clique sur OK.

## Ajouter une action :

Va dans l'onglet Actions et clique sur Nouveau.
Dans Programme/script, tape python.
Dans Ajouter des arguments, entre le chemin complet vers ton script Python, par exemple :

   ```bash
   C:\Scripts\nettoyage_temp.py
   ```
Clique sur OK.

### Finaliser la tâche :

Vérifie que tous les paramètres sont corrects.
Clique sur OK pour sauvegarder la tâche.

### Tester la tâche

Tu peux tester si la tâche fonctionne correctement en retournant dans le Planificateur de tâches, en faisant un clic droit sur la tâche nouvellement créée, et en sélectionnant Exécuter.

### Contribuer 🛠️

Les contributions sont les bienvenues ! Si tu souhaites améliorer le projet ou signaler un bug, n'hésite pas à ouvrir une issue ou à soumettre une pull request.

### Auteur 👨‍💻

Mehdi Akami :[Mon profil GitHub](https://github.com/akamidev) 

### Licence 📜

Ce projet est sous licence MIT. Consulte le fichier [LICENSE](https://github.com/akamidev/python/blob/main/LICENSE) pour plus d'informations.
