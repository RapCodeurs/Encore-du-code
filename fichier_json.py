import json

# Json
# Manipuler des données structurées

# Personne
#    nom : str
#    age : int
#    amis : [str]


# Paul 
# 25
# Sophie, Marie, Jean

# Pierre
# 34
# Andre, Philippe

"""
personne  = {"nom": "Paul",
            "age": 25,
            "amis": ["Sophie, Marie, Jean"]}

# Sérialiser DATA --> TXT "" (Json) on utilise la fonction dumps
# Désérialiser TXT (Json) --> DATA on utilise la fonction  loads


personne_json = json.dumps(personne)

f = open("fichier_json.txt", "w")
f.write(personne_json)
f.close()"""

f = open("fichier_json.txt", "r")
donnes_json = f.read()
f.close()

personne = json.loads(donnes_json)
print("Nom:" + personne["nom"])

