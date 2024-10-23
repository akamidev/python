# Nettoyage Automatique des Fichiers Temporaires

[![Python Version](https://img.shields.io/badge/python-3.9%2B-blue)](https://www.python.org/downloads/)

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
2. **Vérifier l'installation de Python** :
   - Ouvre une invite de commande et tape :
     ```bash
     python --version
     ```
     Cela doit afficher la version de Python.

### Étapes d'installation

1. **Cloner ce repository** sur ton système :
   ```bash
   git clone https://github.com/tonutilisateur/nettoyage-temp-python.git
