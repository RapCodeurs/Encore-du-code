import sqlite3

connexion = sqlite3.connect("albums2.db")
curseur = connexion.cursor() 

# connexion.excute(sql_table_artise)

curseur.execute("""CREATE TABLE artiste (
    artiste_id INTEGER NOT NULL PRIMARY KEY, 
    nom VARCHAR);""")

curseur.execute("""CREATE TABLE album (
    album_id INTEGER NOT NULL PRIMARY KEY, 
    artiste_id INTEGER REFERENCES artiste,
    titre VARCHAR,
    annee_sortie INTEGER);""")

curseur.execute("""INSERT INTO artiste (nom) VALUES ("Michael Jackson");""")
curseur.execute("""INSERT INTO artiste (nom) VALUES ("Céline Dion");""")
curseur.execute("""INSERT INTO album (artiste_id, titre, annee_sortie) VALUES (1, "Thriller", 1983);""")
connexion.commit()
connexion.close()
