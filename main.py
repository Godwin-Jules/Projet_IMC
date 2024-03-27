import json

ROOT_PATH = "try_python_tuto_youtube/Projet_IMC/"

def file_reader(file_path):
    """This function will return the content of the given file"""
    with open(f"{ROOT_PATH}{file_path}", "r") as file_reading:
        return json.load(file_reading)

def file_writer(writing_data, file_path):
    """This function will rewrite the content of the given file with the given data"""
    with open(f"{ROOT_PATH}{file_path}", "w") as file_writing:
        json.dump(writing_data, file_writing)

def compute_IMC(poids, taille):
    """This function will compute the IMC of a person with the given weight and height and return it"""
    return round(poids / taille ** 2, 2)

def modify_user(user_id, user_path, data_path):
    """This function will change the personal informations about a user saved with an ID in the database"""
    users = file_reader(user_path)
    datas = file_reader(data_path)

    user = [el for el in users if el["id"] == user_id][0]
    data = [el for el in datas if el["id"] == user_id][0]

    nom = input("Nouveau nom : ").upper()
    prenom = input("Nouveau prenom : ")
    sex = input("Nouveau sexe : ").upper()
    travail = input("Nouveau travail : ")
    age = input("Nouvel âge : ")
    poids = input("Nouveau poids (en Kg) : ")
    taille = input("Nouvelle taille (en cm) : ")

    if len(nom) != 0:
        user["nom"] = nom
    if len(prenom) != 0:
        user["prenom"] = prenom
    if len(sex) != 0:
        data["sex"] = sex
    if len(travail) != 0:
        data["travail"] = travail
    if len(age) != 0:
        data["age"] = int(age)
    if len(poids) != 0:
        data["poids"] = float(poids)
    if len(taille) != 0:
        data["taille"] = float(taille)/100

    imc = compute_IMC(data["poids"], data["taille"])
    data["IMC"] = imc
    data["classe_sante"] = get_sante_classe(imc)

    for index, el in enumerate(users):
        if el["id"] == user_id:
            users[index] = user
            break
    for index, el in enumerate(datas):
        if el["id"] == user_id:
            datas[index] = data
            break

    file_writer(users, user_path)
    file_writer(datas, data_path)

def get_sante_classe(imc):
    """This function will return the classe ID of someone according to his/her IMC"""
    if imc < 18.5:
        return 0
    elif 18.5 <= imc < 25:
        return 1
    elif 25 <= imc < 30:
        return 2
    elif 30 <= imc < 35:
        return 3
    elif 35 <= imc < 40:
        return 4
    else:
        return 5

def user_creator():
    """This function will create a user with the given details provided"""
    print("\nCréation d'un nouveau compte, veuillez remplir les informations nécessaires")
    users = file_reader("database/users.json")
    datas = file_reader("database/infos.json")
    user = {}
    data = {}
    id_increment = file_reader("database/id_increment.json")
    user_id = id_increment["id_increment"] + 1
    user_nom = input("Nom : ").upper()
    user_prenom = input("Prénom(s) : ")
    user_age = input("Âge : ")
    user_sex = input("Sexe : ").upper()
    user_travail = input("Travail : ")
    user_poids = input("Poids (en Kg) : ")
    user_taille = input("Taille (en cm) : ")

    user.update({"id": user_id})
    data.update({"id": user_id})

    if user_nom:
        user.update({"nom": user_nom})
    else:
        user.update({"nom": "Guest"})
    if user_prenom:
        user.update({"prenom": user_prenom})
    else:
        user.update({"prenom": f"Unknown {user_id}"})
    if user_age:
        data.update({"age": int(user_age)})
    else:
        data.update({"age": 18})
    if user_sex:
        data.update({"sex": user_sex})
    else:
        data.update({"sex": "M"})
    if user_travail:
        data.update({"travail": user_travail})
    else:
        data.update({"travail": "Etudiant"})
    if user_poids:
        data.update({"poids": float(user_poids)})
    else:
        data.update({"poids": 50})
    if user_taille:
        data.update({"taille": float(user_taille)})
    else:
        data.update({"taille": 1.5})
    
    user_imc = compute_IMC(data["poids"], data["taille"])
    user_sante = get_sante_classe(user_imc)

    data.update({"IMC":user_imc, "classe_sante": user_sante})
    id_increment["id_increment"] = user_id

    users.append(user)
    datas.append(data)
    file_writer(users, "database/users.json")
    file_writer(datas, "database/infos.json")
    file_writer(id_increment, "database/id_increment.json")


def main():
    """This is the main function of this mini program of health consulting"""
    print("\nBienvenu(e) !\nVeuillez vous connecter ou créer un compte\n")
    print("\t[1] - Se connecter\n\t[2] - Créer un compte\n")

    user_choice = input("Votre choix : ")
    try:
        user_choice = int(user_choice)
    except Exception as e:
        print(e)

    if user_choice == 1:
        """Se connecter à la plateforme de Health Consulting"""
        users = file_reader("database/users.json")
        print("\nListe des utilisateurs : \n")
        for index, user in enumerate(users):
            print(f"\t{index+1} - {user['nom']} {user['prenom']}")
        user_choice = input("\nVotre choix : ")
        try:
            user_choice = int(user_choice)
        except Exception as e:
            print(e)

        user_id = users[int(user_choice)-1]["id"]

        print("\nQue voulez-vous faire ?\n")
        print("\t[1] - Modifier mes données\n\t[2] - Consulter mon IMC\n\t[3] - Mon état de santé\n")

        user_choice = input("Votre choix : ")
        try:
            user_choice = int(user_choice)
        except Exception as e:
            print(e)
        
        if user_choice == 1:
            """Modifier les données personnelles"""
            modify_user(user_id, "database/users.json", "database/infos.json")
        elif user_choice == 2:
            """Consulter son IMC"""
            user_data = [el for el in file_reader("database/infos.json") if el["id"] == user_id][0]
            print(f"\nVotre IMC est : {user_data['IMC']}")
        elif user_choice == 3:
            """Consulter son état de santé"""
            user_data = [el for el in file_reader("database/infos.json") if el["id"] == user_id][0]
            user_sante = [el for el in file_reader("database/sante.json") if el["id"] == user_data["classe_sante"]][0]
            print(f"\nVotre état de santé est : ")
            print(f"\tDiagnostic : {user_sante["diag"]}")
            print(f"\tRaison(s) : {user_sante["raison"]}")
            print(f"\tConseil(s) : {user_sante["conseil"]}")
        
    elif user_choice == 2:
        """Créer un compte sur la plateforme de Health Consulting"""
        user_creator()

main()