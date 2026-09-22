Guide d'utilisation
===================

Présentation
------------

Task Tracker CLI est une application en ligne de commande conçue pour suivre
les tâches quotidiennes, prioriser le travail et garder un historique simple de
l'état d'avancement.

Chaque tâche est enregistrée dans un fichier JSON local et contient :

- un identifiant unique ;
- une description ;
- un statut (`todo`, `in-progress` ou `done`) ;
- une date de création ;
- une date de mise à jour.

Installation
------------

Prérequis
^^^^^^^^^

Assurez-vous d'avoir Python 3.14 ou une version compatible ainsi que l'outil
``uv`` installé sur votre machine.

Installation du projet
^^^^^^^^^^^^^^^^^^^^^^

Depuis le dossier du projet :

.. code-block:: bash

   git clone <url-du-depot>
   cd task-tracker
   uv sync

Pour activer l'environnement virtuel :

.. code-block:: bash

   source .venv/bin/activate

Utilisation
-----------

L'application peut être lancée de deux manières :

.. code-block:: bash

   uv run python -m task_cli

ou directement via le point d'entrée :

.. code-block:: bash

   uv run task_cli

Commandes disponibles
---------------------

Ajouter une ou plusieurs tâches
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

   task-cli add "Faire le ménage"
   task-cli add "Faire la cuisine" "Faire la lessive"

Cette commande enregistre une ou plusieurs tâches avec le statut initial
``todo``.

Lister les tâches
^^^^^^^^^^^^^^^^^

.. code-block:: bash

   task-cli list

Affiche toutes les tâches enregistrées.

Pour filtrer par statut :

.. code-block:: bash

   task-cli list todo
   task-cli list in-progress
   task-cli list done

Mettre à jour une tâche
^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

   task-cli update 1 "Faire les courses"

La description de la tâche ayant l'identifiant 1 est remplacée.

Marquer une tâche comme en cours
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

   task-cli mark-in-progress 1

Marquer une tâche comme terminée
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

   task-cli mark-done 1

Supprimer une ou plusieurs tâches
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

   task-cli delete 1
   task-cli delete 2 3 4

Statuts disponibles
-------------------

Le programme utilise trois statuts :

- ``todo`` : tâche à faire ;
- ``in-progress`` : tâche actuellement en cours ;
- ``done`` : tâche terminée.

Structure du projet
-------------------

.. code-block:: text

   task-tracker/
   ├── src/
   │   └── task_cli/
   │       ├── __init__.py
   │       ├── cli.py
   │       ├── model.py
   │       ├── storage.py
   │       └── task.py
   ├── tests/
   │   ├── test_cli.py
   │   ├── test_storage.py
   │   ├── test_task.py
   │   └── test_temp_file.py
   ├── docs/
   │   └── source/
   │       ├── conf.py
   │       ├── index.rst
   │       ├── guide.rst
   │       ├── modules.rst
   │       └── task_cli.rst
   ├── README.md
   ├── pyproject.toml
   └── CHANGELOG.md

Rôles des modules
-----------------

``task_cli.cli``
    Contient la logique de parsing de ligne de commande et le point d'entrée
    principal de l'application.

``task_cli.task``
    Gère les opérations métiers liées aux tâches : création, mise à jour,
    suppression, filtrage et affichage.

``task_cli.storage``
    Lit et écrit les données dans le fichier JSON de stockage local.

``task_cli.model``
    Définit le modèle de données de la tâche à l'aide d'une dataclass et d'une
    énumération de statuts.

Exemples de workflow
--------------------

Voici un exemple complet d'utilisation :

.. code-block:: bash

   task-cli add "Préparer la réunion" "Relire le rapport"
   task-cli list
   task-cli mark-in-progress 1
   task-cli update 2 "Finaliser la documentation"
   task-cli mark-done 1
   task-cli list done

Ce type de séquence permet de gérer simplement un backlog de tâches tout en
maintenant une vue claire de l'avancement.
