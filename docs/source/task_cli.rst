Package task_cli
================

Le package ``task_cli`` centralise toute la logique métier de l'application en
ligne de commande. Il permet de créer, lister, modifier, filtrer et supprimer
les tâches tout en gardant une persistance locale simple via un fichier JSON.

Vue d'ensemble
--------------

Ce package est organisé selon une séparation claire des responsabilités :

- ``task_cli.cli`` : interaction avec l'utilisateur et parsing des commandes ;
- ``task_cli.model`` : définition du modèle de données et des statuts ;
- ``task_cli.storage`` : lecture et écriture des tâches sur le disque ;
- ``task_cli.task`` : logique métier pour manipuler les tâches.

Cette structure rend le code plus lisible, plus facile à tester et plus simple à
étendre.

Architecture du package
-----------------------

.. list-table:: Rôle des modules
   :header-rows: 1
   :widths: 20 80

   * - Module
     - Description
   * - ``task_cli.cli``
     - Gère les commandes de l'interface terminal et le point d'entrée principal.
   * - ``task_cli.model``
     - Déclare le modèle ``Task`` et l'énumération des statuts.
   * - ``task_cli.storage``
     - Lit et écrit les données de façon persistante dans le fichier JSON local.
   * - ``task_cli.task``
     - Implémente les opérations de création, modification, suppression et filtrage.

.. automodule:: task_cli
   :no-index:
   :undoc-members:
   :show-inheritance:

Sous-modules
------------


Module CLI
^^^^^^^^^^

Ce module gère le parsing des commandes de l'application et oriente chaque
appel vers la bonne logique métier.

.. automodule:: task_cli.cli
   :members:
   :undoc-members:
   :show-inheritance:


Module de modèle
^^^^^^^^^^^^^^^^

Ce module définit le modèle de données des tâches ainsi que les statuts pris en
charge par l'application.

.. automodule:: task_cli.model
   :members:
   :undoc-members:
   :show-inheritance:


Module de stockage
^^^^^^^^^^^^^^^^^^

Ce module s'occupe de la persistance locale des tâches dans le fichier JSON.

.. automodule:: task_cli.storage
   :members:
   :undoc-members:
   :show-inheritance:


Module métier
^^^^^^^^^^^^^

Ce module contient la logique principale pour manipuler les tâches : ajout,
mise à jour, suppression, listage et filtrage par statut.

.. automodule:: task_cli.task
   :members:
   :undoc-members:
   :show-inheritance:
