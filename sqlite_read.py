import sqlite3


connexion = sqlite3.connect("albums2.db")
curseur = connexion.cursor() 

curseur.execute("SELECT * FROM artiste")
artistes = curseur.fetchall()
for art in artistes:
    print(art)

connexion.close()