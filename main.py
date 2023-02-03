#!/usr/bin/python3
"""
- Ecrire une base de code pour un framework python et open source nommé pyReact.
Tous comme react js elle permet d'ecrire des composant fronte-end pour une application web.
plus perfotmante et plus rapide que react js.
- Creer un serveur python qui renvoi les vues creer au navigateur
- Rediger un fichier readme.md expliquant les objectifs et comment contribuer
- Donner des sugestion en pour ameliorer le code existant
"""

def bonjour():
    print("Bonjour!")

bonjour()

import pyReact

class Composant(pyReact.Component):
    def __init__(self, props):
        super().__init__(props)
        self.state = {
            "data": props.data
        }
    
    def render(self):
        return React.createElement(
            "div", 
            {}, 
            React.createElement(
                "h2", 
                {}, 
                self.state.data
            )
        )

# Créer un composant
c = Composant({"data": "Hello World!"})

# Créer un élément à partir du composant
e = c.createElement()

# Afficher le composant
c.render(e)

# Créer un serveur
server = pyReact.Server(e)

# Démarrer le serveur
server.run()

# Suggestions pour améliorer le code existant
# 1. Utiliser des fonctions utiles fournies par pyReact pour gérer plus facilement le composant et le DOM.
# 2. Utiliser des bibliothèques tierces, telles que React Router, pour ajouter une couche d'abstraction à l'application. 
# 3. Utiliser des outils de développement comme React DevTools pour améliorer le développement et le débogage.
# 4. Utiliser des outils pour compiler et optimiser le code, comme Babel et Webpack.
# 5. Utiliser des bibliothèques pour rendre l'application plus robuste, telles que Redux et RxJS.