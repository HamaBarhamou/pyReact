#!/usr/bin/python3
import socket

# Créons un socket TCP/IP
serveur_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Liaison du socket à une adresse précise
serveur_socket.bind(('localhost', 1234))

# Démarrage de l'écoute
serveur_socket.listen(1)

# Attente et traitement des connexions entrantes
while True:
    # Attente et traitement des connexions entrantes
    connexion, adresse = serveur_socket.accept()
    try:
        # Récupération des données
        data = connexion.recv(1024).decode('utf-8')
        # Traitement des données
        if data == "ping":
            # Envoi des données
            connexion.send("pong".encode('utf-8'))
    finally:
        # Fermeture de la connexion
        connexion.close()
