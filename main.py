import os

dossier = 'data'

mot = "nastyca"

for root, dirs, fichiers in os.walk(dossier):
    for fichier in fichiers:
        chemin = os.path.join(root, fichier)

        if os.path.isfile(chemin):
            with open(chemin, 'r', encoding='utf-8') as f:
                lignes = f.readlines()

            lignes_ = [ligne for ligne in lignes if mot not in ligne]

            with open(chemin, 'w', encoding='utf-8') as f:
                f.writelines(lignes_)

            print(f"Lignes contenant '{mot}' supprimées dans -> {chemin}")
