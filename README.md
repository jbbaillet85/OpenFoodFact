![texte alt][pancake.jpg]
# OpenFoodFact
Utilisez les données publiques de l'OpenFoodFact

## Tableau Trello:
https://trello.com/b/umDBQG3F/bienmanger

## Configuration Requise:
- Télécharger python: https://www.python.org/downloads/
- Télécharger mysql:https://dev.mysql.com/downloads/mysql/
- Télécharger git: https://git-scm.com/

## Comment installer le programme:
### Sur votre terminal:

1. Cloner le projet: *git clone https://github.com/jbbaillet85/OpenFoodFact.git*

2. Créer un environnement virtuel dans le dossier OpenFoodFact:
- windows: *py -3.8 -m venv env*
- mac/linux: *python3 -m venv env*

3. Activer l'environnement virtuel:
- windows: *source venv\Scripts\activate*
- mac/linux: *source/bin/activate*

4. Installer les dépendances à partir du fichier [requirements.txt](requirements.txt)
*pip3 install -r requirements.txt*

5. executer le serveur 
- linux: *sudo service mysql start*
- windows à partir du dossier mysql/bin: *./mysqld.exe --console*

6. executer client mysql
- linux: *sudo mysql -u root -p*
- windows: */mysql.exe -u root -p*

7. Créer une base de donnée avec le client mysql:
- *CREATE DATABASE __nombase__*

8. Remplacer les valeurs du fichier [config.py](config.py) par les tiennes

9. Lancer le fichier [install.py](install.py): "python install.py"

10. Lancer le fichier [main.py](main.py): windows: "python main.py" mac/linux: "python3 main.py"

11. Pour quitter le programme, tape le racourcis *ctrl* + *c*