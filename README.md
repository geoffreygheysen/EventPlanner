# 📦 Event Planner - Labo Flask

<details>
<summary>📌 Détails du projet</summary>

## 🎯 Contexte

Développement d'une API REST en Flask permettant de gérer les événements, les utilisateurs, les inscriptions et les rôles.

---

## 📚 Objectifs pédagogiques

- Appliquer Flask en architecture MVC complète
- Utiliser SQLAlchemy pour le mapping base de données
- Implémenter la validation via Marshmallow
- Sécuriser l’API avec JWT
- Mettre en place des rôles (utilisateur, participant, admin)
- Utiliser Thunder Client ou Postman pour tester l’API

---

## 🧩 Entités à modéliser

- ✅ User : id, email, password (hashé), nom, prénom, rôle (utilisateur/participant/admin), statut,
infos complémentaires (allergies, GSM...)
- ✅ Event : id, titre, date_debut, date_fin, lieu, statut (en attente, confirmé, passé)
- ✅ Theme : id, nom (lié à Event)
- ✅ Participation : id, id_user, id_event, confirmé
- ✅ Commentaire : id, contenu, id_user, id_event (autorisé uniquement si l'événement est passé)

---

## 🛡️ Gestion des rôles

- Utilisateur : inscription, demande de participation, commenter un événement passé
- Participant : compléter son profil, s’inscrire à un événement, voir ses événements
- Admin : créer événements et thèmes, valider les demandes, bannir un utilisateur

---

## 🚀 Fonctionnalités à implémenter

- 🔴 Inscription & connexion avec JWT
- 🔴 Consultation publique des événements par date/statut
- 🔴 Demande de rôle participant et validation par admin
- 🔴 Création/gestion des événements et thèmes par admin
- 🔴 Inscription à un événement par un participant
- 🔴 Ajout de commentaire sur un événement passé

---

</details>

<details>
<summary>📌 Architecture du projet</summary>

### 📁 Arborescence du projet `EventPlanner`

```
📦 EventPlanner/                             # Dossier racine du projet Flask
│
├── 📂 app/                                  # Dossier principal de l'application Flask
│   │
│   ├── 📂 controllers/                      # Contient la logique métier (contrôle les flux entre modèles et routes)
│   │   └── 📄 user_controller.py               # Contrôleur lié à la logique utilisateur
│   │
│   ├── 📂 models/                           # Contient les modèles de données et les schémas de validation
│   │   │
│   │   ├── 📂 db/                           # Modèles de base de données (SQLAlchemy ORM)
│   │   │   ├── 📄 __init__.py                  # Initialise le sous-package `db`, importe les modèles
│   │   │   ├── 📄 base_model.py                # Modèle de base (hérité par les autres modèles)
│   │   │   ├── 📄 user_model.py                # Modèle représentant les utilisateurs
│   │   │   ├── 📄 event_model.py               # Modèle représentant les événements
│   │   │   ├── 📄 theme_model.py               # Modèle représentant les thèmes d'événement
│   │   │   ├── 📄 participation_model.py       # Modèle représentant la participation des utilisateurs
│   │   │   └── 📄 comment_model.py             # Modèle représentant les commentaires
│   │   │
│   │   ├── 📂 dto/                          # Contient les schémas de validation (Marshmallow)
│   │   │   ├── 📂 user/                        # Schémas relatifs aux utilisateurs
│   │   │   │   └── 📄 user_schema.py           # Définition des schémas Marshmallow pour User
│   │   │   ├── 📂 event/                       # Schémas relatifs aux événements
│   │   │   ├── 📂 theme/                       # Schémas relatifs aux thèmes
│   │   │   ├── 📂 participation/               # Schémas relatifs aux participations
│   │   │   └── 📂 comment/                     # Schémas relatifs aux commentaires
│   │
│   ├── 📂 routes/                           # Définition des routes Flask (Blueprints)
│   │   └── 📄 user_routes.py                   # Routes liées aux utilisateurs
│   │
│   ├── 📂 tools/                            # Modules utilitaires / outils transversaux
│   │   └── 📄 session_scope.py                 # Context manager pour gérer la session SQLAlchemy proprement
│   │
│   ├── 📄 __init__.py                       # Initialise l'application Flask, les extensions, les Blueprints
│   └── 📄 config.py                         # Paramètres de configuration (dev, prod, base de données, etc.)
│
├── 📄 .gitignore                            # Spécifie les fichiers/dossiers à ignorer par Git
├── 📄 README.md                             # Documentation générale du projet (installation, usage, etc.)
├── 📄 requirements.txt                      # Liste des dépendances Python à installer avec pip
└── 📄 run.py                                # Point d'entrée de l'application Flask (lance le serveur)
```

</details>

<details>
<summary>📌 Récupération du projet depuis GitHub</summary>

### 📥 Récupération du projet via GitHub

Commande :

```bash
# récuperer le repository
git clone https://github.com/ton-user/ton-projet.git

# se positioner sur le projet
cd ton-projet
```

</details>

<details>
<summary>📌 Mise en place de l'environnement virtuel</summary>

### 💻 Création et connexion à l'environnemment virtuel

---

#### Sur macOS / Linux (terminal Bash / Zsh)

Commande :

```bash
# 1. Créer un environnement virtuel nommé ".venv"
python3 -m venv .venv

# 2. Activer l'environnement
source .venv/bin/activate

# 3. (Facultatif) Vérifier l'environnement actif
which python
```

---

#### Sur Windows (CMD ou PowerShell)

Commande :

```bash
# 1. Créer un environnement virtuel nommé ".venv"
python -m venv .venv

# 2. Activer l'environnement
.\.venv\Scripts\activate
```

---

#### 🔚 Pour désactiver l’environnement (Mac/linux ou Windows)

Commande :

```bash
# Désactiver l'environnement
deactivate
```

---

</details>

<details>
<summary>📌 Installation des packages Python</summary>

### 🧰 Installation des dépendances nécéssaires à l'application

---

A copier/coller dans votre fichier app/requirements.txt :

```txt
# This file is used to define the dependencies for the Flask application.
Flask==3.1.1                             # Framework principal

# Database dependencies
SQLAlchemy==2.0.41                       # ORM bas niveau
Flask-SQLAlchemy==3.1.1                  # Intégration SQLAlchemy + Flask
psycopg2==2.9.10                         # Connecteur PostgreSQL

# Authentication dependencies
Flask-Login==0.6.3                       # Gestion de sessions utilisateur

# API dependencies
marshmallow==4.0.0                       # Sérialisation/désérialisation d'objets
Flask-RESTful==0.3.10                    # Aide à créer des APIs RESTful
Flask-JWT-Extended==4.7.1                # Authentification via JSON Web Tokens
```

---

Commande pour tout installer une fois l'environnement virtuelle créer :

```bash
pip install -r requirements.txt
```

---

</details>

<details>
<summary>📌 Création et connexion à la Database</summary>

### 🔗 Configuration de la database PostgreSQL

Créer une base de données via pgAdmin 4 ou autre, puis renseignez les informations dans app/config.py :

La clé secrète est utilisée par Flask pour sécuriser les sessions, les cookies, etc. (ex de site: https://djecrety.ir/)

exemple pour PostgreSQL:

```python
# Clé secrète Flask (`SECRET_KEY`)
SECRET_KEY = 'votre clé secrète ici'

# Paramètres de connexion
scheme         = "postgresql+psycopg2"
username       = "votre_utilisateur"
password       = "votre_mot_de_passe"
hostname       = "localhost"
port           = "5432"
database_name  = "nom_de_votre_base"

# Construction de l'URL de connexion
URL_DB = f"{scheme}://{username}:{password}@{hostname}:{port}/{database_name}"

# Configuration SQLAlchemy
SQLALCHEMY_DATABASE_URI = URL_DB
```

</details>

---

## 🚀 Lancer l'application python

Commande :

```bash
python run.py
```

---