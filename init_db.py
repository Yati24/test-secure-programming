import sqlite3

connection = sqlite3.connect('database.db')

with open('schema.sql') as f:
    connection.executescript(f.read())

print("Base de données initialisée avec succès !")
print("Utilisateur 'admin' créé (mdp: admin)")

connection.commit()
connection.close()  