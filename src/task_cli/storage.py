"Modèle d'écriture et de lecture des données de tâches"

import json
import sys
from pathlib import Path


def load_tasks() -> list[dict]:
    """
    Charger les tâches depuis le fichier JSON.

    :return: Une liste de tâches.
    :rtype: list[dict]
    """

    path = Path("src/task_cli/data/tasks.json")

    if not path.exists():
        return []

    try:
        content = path.read_text(encoding="utf-8").strip()

        if not content:
            return []

        data = json.loads(content)

        if not isinstance(data, list):
            print(
                "Erreur : le fichier tasks.json ne contient pas une liste de tâches.", 
                file=sys.stderr
            )
            return []

        return data

    except json.JSONDecodeError:
        print("Erreur : le fichier tasks.json n'est pas un JSON valide.", file=sys.stderr)
        return []
    except OSError as exc:
        print(f"Erreur : impossible de lire le fichier tasks.json. {exc}", file=sys.stderr)
        return []


def save_tasks() -> None:
    """
    Sauvegarder les tâches dans le fichier JSON.
    """


def update_task() -> None:
    """
    Mettre à jour une tâche dans le fichier JSON.
    """
