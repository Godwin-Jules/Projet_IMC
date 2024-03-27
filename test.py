import json

ROOT_PATH = "try_python_tuto_youtube/Projet_IMC/"

sante = [
    {"id": 0, "diag": "Sous poids", "raison": "Sous alimentation", "conseil": "Plus d'alimentation"},
    {"id": 1, "diag": "Poids normal", "raison": "Vous prenez soin de notre ligne", "conseil": "Contunez comme cela"},
    {"id": 2, "diag": "Surpoids", "raison": "Mauvaise alimentation", "conseil": "Consommer moins gras, Faites un peu de sport, Pratiquer le jeûne intermittant"},
    {"id": 3, "diag": "Obésité", "raison": "Mauvaise alimentation, Manque d'activité physique", "conseil": "Consommer moins gras, Faites un peu de sport, Pratiquer le jeûne intermittant"},
    {"id": 4, "diag": "Obésité sévère", "raison": "Mauvaise alimentation, Manque d'activité physique", "conseil": "Consommer moins gras, Faites un peu de sport, Pratiquer le jeûne intermittant, Demander un suivi par un Nutritioniste"},
    {"id": 5, "diag": "Obésité morbide", "raison": "Mauvaise alimentation, Manque d'activité physique", "conseil": "Consommer moins gras, Faites un peu de sport, Pratiquer le jeûne intermittant, Songer à une intervention bariatrique"}
]

with open(f"{ROOT_PATH}database/sante.json", "w") as save:
    json.dump(sante, save)