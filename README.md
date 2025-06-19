# 📦 Event Planner - Labo Flask

<details>
<summary>📌 Détails du projet</summary>

## 🎯 Contexte

Développement d'une API REST en Flask permettant de gérer les événements, les utilisateurs, les inscriptions et les rôles.

---

## Objectifs pédagogiques

- Appliquer Flask en architecture MVC complète
- Utiliser SQLAlchemy pour le mapping base de données
- Implémenter la validation via Marshmallow
- Sécuriser l’API avec JWT
- Mettre en place des rôles (utilisateur, participant, admin)
- Utiliser Thunder Client ou Postman pour tester l’API

---

## Entités à modéliser

- User : id, email, password (hashé), nom, prénom, rôle (utilisateur/participant/admin), statut,
infos complémentaires (allergies, GSM...)
- Event : id, titre, date_debut, date_fin, lieu, statut (en attente, confirmé, passé)
- Theme : id, nom (lié à Event)
- Participation : id, id_user, id_event, confirmé
- Commentaire : id, contenu, id_user, id_event (autorisé uniquement si l'événement est passé)

---

## Gestion des rôles

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