import os
import shutil

# Dossiers à nettoyer
folders_to_clean = [
    os.getenv('TEMP'),  # Dossier temporaire
    os.path.join(os.getenv('USERPROFILE'), 'AppData', 'Local', 'Temp'),  # Dossier %temp%
]

# Fonction pour supprimer un fichier ou un dossier
def delete_item(path):
    try:
        if os.path.isfile(path) or os.path.islink(path):
            os.remove(path)
            print(f"Fichier supprimé: {path}")
        elif os.path.isdir(path):
            shutil.rmtree(path)
            print(f"Dossier supprimé: {path}")
    except Exception as e:
        print(f"Erreur en supprimant {path}: {e}")

# Parcourir les dossiers et supprimer les fichiers
def clean_folders(folders):
    for folder in folders:
        if os.path.exists(folder):
            for root, dirs, files in os.walk(folder):
                for file in files:
                    file_path = os.path.join(root, file)
                    delete_item(file_path)
                for dir in dirs:
                    dir_path = os.path.join(root, dir)
                    delete_item(dir_path)
        else:
            print(f"Dossier non trouvé: {folder}")

if __name__ == "__main__":
    print("Nettoyage des dossiers temporaires...")
    clean_folders(folders_to_clean)
    print("Nettoyage terminé.")
