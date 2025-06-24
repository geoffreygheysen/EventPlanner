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

- ✅ Inscription & connexion avec JWT
- ✅ Consultation publique des événements par date/statut
- 🔴 Demande de rôle participant et validation par admin
- 🔴 Création/gestion des événements et thèmes par admin
- 🔴 Inscription à un événement par un participant
- ✅ Ajout de commentaire sur un événement passé

---

</details>

<details>
<summary>📌 Architecture du projet</summary>

### 📁 Arborescence du projet `EventPlanner`

```
📦 EventPlanner/                             # Dossier racine du projet Flask
│
├── 📂 app/                                  # Contient l'ensemble de l'application Flask
│   │
│   ├── 📂 controllers/                      # Contient la logique métier (gère l'interaction entre modèles et routes)
│   │   ├── 📄 auth_controller.py
│   │   ├── 📄 comment_controller.py
│   │   ├── 📄 event_controller.py
│   │   ├── 📄 participation_controller.py
│   │   ├── 📄 theme_controller.py
│   │   └── 📄 user_controller.py
│   │
│   ├── 📂 models/                           # Définit les modèles de données et les schémas de validation
│   │   │
│   │   ├── 📂 db/                           # Modèles de base de données (via SQLAlchemy ORM)
│   │   │   ├── 📄 __init__.py
│   │   │   ├── 📄 base_model.py
│   │   │   ├── 📄 user_model.py
│   │   │   ├── 📄 event_model.py
│   │   │   ├── 📄 theme_model.py
│   │   │   ├── 📄 participation_model.py
│   │   │   └── 📄 comment_model.py
│   │   │
│   │   ├── 📂 dto/                          # Schémas de validation des données (via Marshmallow)
│   │   │   ├── 📂 user/
│   │   │   │   ├── 📄 user_schema.py
│   │   │   │   └── 📄 user_update_schema.py
│   │   │   ├── 📂 event/
│   │   │   │   ├── 📄 event_schema.py
│   │   │   │   └── 📄 event_update_schema.py
│   │   │   ├── 📂 theme/
│   │   │   │   ├── 📄 theme_schema.py
│   │   │   │   └── 📄 theme_update_schema.py
│   │   │   ├── 📂 participation/
│   │   │   │   ├── 📄 participation_schema.py
│   │   │   │   └── 📄 participation_update_schema.py
│   │   │   └── 📂 comment/
│   │   │       ├── 📄 comment_schema.py
│   │   │       └── 📄 comment_update_schema.py
│   │
│   ├── 📂 routes/                           # Définition des routes Flask (via Blueprints)
│   │   ├── 📄 auth_routes.py
│   │   ├── 📄 comment_routes.py
│   │   ├── 📄 event_routes.py
│   │   ├── 📄 participation_routes.py
│   │   ├── 📄 theme_routes.py
│   │   └── 📄 user_routes.py
│   │
│   ├── 📂 tools/                            # Modules utilitaires et fonctions transversales
│   │   ├── 📄 jwt_manager.py
│   │   ├── 📄 role_required.py
│   │   └── 📄 session_scope.py
│   │
│   ├── 📄 __init__.py                       # Initialise l'application Flask, les extensions et les Blueprints
│   └── 📄 config.py                         # Paramètres de configuration (base de données, env dev/prod, etc.)
│
├── 📄 .gitignore                            # Liste des fichiers/dossiers ignorés par Git
├── 📄 README.md                             # Documentation du projet (installation, fonctionnement, etc.)
├── 📄 requirements.txt                      # Liste des dépendances Python du projet
└── 📄 run.py                                # Point d'entrée principal pour démarrer l'application Flask
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