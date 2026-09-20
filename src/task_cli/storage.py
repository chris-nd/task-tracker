"Modèle d'écriture et de lecture des données de tâches"

import json
import os
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


def save_tasks(tasks: list[dict]) -> None:
    """
    Sauvegarder les tâches dans le fichier JSON.

    :param tasks: Une liste de tâches à sauvegarder.
    :type tasks: list[dict]
    """

    if not tasks:
        return

    dir_path = Path("src/task_cli/data/")

    if not dir_path.exists():
        os.makedirs(dir_path)

    data = load_tasks() + tasks

    try:
        with open("src/task_cli/data/tasks.json", "w", encoding="utf-8") as f:
            json.dump(data, f)
    except OSError as exc:
        print(f"Erreur : impossible de sauvegarder les tâches. {exc}", file=sys.stderr)


def update_data(tasks: list[dict]) -> None:
    """
    Mettre à jour les tâches dans le fichier JSON.
    """

    # Gestion des erreurs
    if not tasks:
        print("Erreur : Aucune tâche à mettre à jour.")
        return

    if not isinstance(tasks, list):
        print("Erreur : Les tâches doivent être une liste pour être mises à jour.")
        return

    try:
        with open("src/task_cli/data/tasks.json", "w", encoding="utf-8") as f:
            json.dump(tasks, f)
    except OSError as exc:
        print(f"Erreur : impossible de mettre à jour les tâches. {exc}", file=sys.stderr)

def remove_tasks(tasks_id: list[int]) -> None:
    """
    Supprimer une ou plusieurs tâches du fichier JSON.
    """
    data = load_tasks()

    if not data:
        print("Aucune tâche enregistrée.")
        return

    task_to_delete = [task for task in data if task.get("id") in tasks_id]

    if not task_to_delete:
        print("Tâche non trouvée.")
        return

    try:
        with open("src/task_cli/data/tasks.json", "w", encoding="utf-8") as f:
            for task in task_to_delete:
                data.remove(task)
            json.dump(data, f)
    except OSError as exc:
        print(f"Erreur : impossible de supprimer les tâches. {exc}", file=sys.stderr)

    for task in task_to_delete:
        print(f"Tâche supprimée : [ID: {task.get('id')} - {task.get('description')}].")
