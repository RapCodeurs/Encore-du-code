import os.path

"""f = open("nom_fichier.txt", "w")

for i in range(1, 11):
    # print(i)
    f.write(str(i) + "\n")
    # f.write("\n")

f.close()"""

"""fi = open("text_ficher.txt", "w")
fi.write("je serai de bon humeur aujourd'hui.\n")
fi.write("A quoi tu penses ?")
fi.close()"""

name_file = os.path.join("sous rep", "nom_fichier.txt")
print("Fichier: " + name_file)

if os.path.exists(name_file):
    print("Le fichier existe")
    f = open(name_file, "r")
    text = f.read()
    print(text)
    f.close()
else:
    print("Le fichier n'exite pas")


"""
try:
    f = open("nom_fichier555.txt", "r")
except FileNotFoundError:
    print("Le fichier n'a pas été trouvé")
else:
    text = f.read()
    print(text)
    for i in f:
        print(i, end="")
    f.close()"""


