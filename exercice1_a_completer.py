# =============================================
# TP2 - Exercice 1 : Decision de fin d'annee
# Notions : if / elif / else, conditions combinees et imbriquees
# =============================================
SEUIL_ADMISSION = 10
SEUIL_RATTRAPAGE = 8
NOTE_ELIMINATOIRE = 6

nom = input("Nom de l'etudiant : ").strip().title()
cc = float(input("Note de CC (0-20) : "))
examen = float(input("Note d'examen (0-20) : "))
assiduite = input("Assiduite >= 80 % ? (o/n) : ").strip().lower()

# 1. Validation des deux notes (conditions combinees)
if 0 <= cc <= 20 and 0 <= examen <= 20 :  # Les DEUX notes valides
    moyenne = cc * 0.4 + examen * 0.6

    # 2. Mention (chaine de elif)
    if moyenne >= 16:
        mention = "Tres Bien"
    elif moyenne >= 14:  # Sinon, si...
        mention = "Bien"
    elif moyenne >= 10:  # Seuil de "Assez Bien"
        mention = "Assez Bien"
    elif moyenne >= SEUIL_ADMISSION:
        mention = "Passable"
    else :
        mention = "Aucune"

    # 3. Decision (conditions imbriquees)
    # Admis : moyenne suffisante ET examen non eliminatoire
    if moyenne >= SEUIL_ADMISSION and examen and NOTE_ELIMINATOIRE:
        decision = "Admis"
    elif moyenne >= 10:  # Seuil du rattrapage
        if assiduite == "o":  # Comparaison d'egalite
            decision = "Rattrapage"
        else:
            decision = "Ajourne (assiduite insuffisante)"
    else:
        decision = "Aucune"  # Aucune condition satisfaite

    # 4. Affichage du resultat
    print("-" * 40)
    print(f"Etudiant : {nom}")
    print(f"Moyenne  : {moyenne:2f}")  # 2 decimales
    print(f"Mention  : {mention}")
    print(f"Decision : {decision}")
    print("-" * 40)
if 0 >= cc >= 20 and 0 >= examen >= 20 :
    print("Erreur : les notes doivent etre comprises entre 0 et 20.")

print("hello world")
