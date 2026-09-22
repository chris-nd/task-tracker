Package task_cli
================

Le package ``task_cli`` contient la logique métier et la couche d'interaction de
l'application en ligne de commande. Il regroupe les composants nécessaires pour
créer, consulter, modifier, filtrer et supprimer des tâches.

Aperçu
------

Le package ``task_cli`` centralise la logique de gestion des tâches pour
l'application en ligne de commande. Il regroupe les éléments nécessaires au
traitement des commandes utilisateur, à la validation des données, à la
persistance locale et à la représentation du modèle de tâche.

Le module principal expose le cœur de l'application et sert de point d'entrée
pour les opérations CRUD liées aux tâches : ajout, mise à jour, suppression,
listage et filtrage selon le statut.

Les classes et fonctions du package sont structurées de manière à séparer :

- la saisie utilisateur et le parsing des commandes dans ``task_cli.cli`` ;
- le modèle métier des tâches dans ``task_cli.model`` ;
- la persistance des données dans ``task_cli.storage`` ;
- les opérations de gestion des tâches dans ``task_cli.task``.

Cette organisation permet de garder le code maintenable, de tester chaque
composant indépendamment et de faciliter l'évolution de l'interface en ligne de
commande.

.. automodule:: task_cli
   :no-index:
   :undoc-members:
   :show-inheritance:

Sous-modules
------------

task_cli.cli
^^^^^^^^^^^^

Ce module gère le parsing des commandes et le point d'entrée principal de
l'application.

.. automodule:: task_cli.cli
   :members:
   :undoc-members:
   :show-inheritance:

task_cli.model
^^^^^^^^^^^^^^

Ce module définit le modèle de données des tâches et les statuts pris en charge.

.. automodule:: task_cli.model
   :members:
   :undoc-members:
   :show-inheritance:

task_cli.storage
^^^^^^^^^^^^^^^^

Ce module lit et écrit les tâches dans le fichier JSON local utilisé pour la
persistance des données.

.. automodule:: task_cli.storage
   :members:
   :undoc-members:
   :show-inheritance:

task_cli.task
^^^^^^^^^^^^^

Ce module contient les opérations de gestion des tâches : création, mise à jour,
validation du statut, filtrage et affichage.

.. automodule:: task_cli.task
   :members:
   :undoc-members:
   :show-inheritance:
