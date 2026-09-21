# Task Tracker

Application en ligne de commande permettant de créer et gérer des tâches.

## Fonctionnalités

- Ajouter une ou plusieurs tâches
- Consulter les tâches enregistrées
- Attribuer un statut à chaque tâche
- Modifier la description et le statut d’une tâche
- Supprimer une tâche ou plusieurs tâches
- Sauvegarde persistante des données localement

## Statuts disponibles

- `todo`
- `in-progress`
- `done`

## Installation

### Installation de l’environnement de développement

Clonez le projet puis installez ses dépendances avec `uv` :

```bash
git clone <URL_DU_DEPOT>
cd task-tracker
uv sync
```

Pour activer l’environnement virtuel :

```bash
Sous Mac:

source .venv/bin/activate
```

```bash
Sous Windows:

source mon-env/Scripts/activate
```

### Installation autonome

Téléchargez le binaire puis l'installez localement:

```bash
pip install <BINAIRE_WHLS>
```

## Utilisation

Lancez l’application avec :

```bash
uv run python -m task_cli
```

```bash
uv run task_cli
```

### Exemple

```bash
task-cli add "Faire le ménage"
task-cli add "Faire à manger" "Faire la lessive" 
task-cli list
task-cli mark-in-progress 1
task-cli mark-done 1
task-cli update 2 "Faire les courses"
task-cli delete 3
```

## Structure du projet

```text
task-tracker/
├── src/
│   └── task_cli/
│       ├── cli.py
│       └── ...
├── README.md
├── pyproject.toml
└── uv.lock
```

## Modèle d’une tâche

Chaque tâche contient les informations suivantes :

- `id` : identifiant unique
- `description` : description de la tâche
- `status` : statut actuel
- `created_at` : date de création
- `updated_at` : date de dernière modification

## Tests

Pour lancer les tests :

```bash
uv run pytest
```

ou

```bash
pytest
```

## Remerciements

Ce projet fait partie de la liste de projets de la plateforme `Roadmap.sh` et accessible à l'adresse suivante : [https://roadmap.sh/projects/task-tracker](https://roadmap.sh/projects/task-tracker)
