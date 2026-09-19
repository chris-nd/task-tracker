"Module décrivant les opérations sur les tâches"

from datetime import datetime

from task_cli.storage import load_tasks, save_tasks


def create_tasks(descriptions: list[str]) -> None:
    """
    Crée une nouvelle tâche.

    :param descriptions: Les descriptions des tâches
    :type descriptions: list[str]
    """

    # Gestion des erreurs
    if not descriptions:
        print("Erreur : La description de la tâche est vide.")
        return

    tasks = []
    task_id = len(load_tasks()) + 1
    for desc in descriptions:
        task = {
            "id": task_id,
            "description": desc,
            "status": "todo",
            "created_at": datetime.now().strftime("%Y-%m-%d to %H:%M"),
            "updated_at": datetime.now().strftime("%Y-%m-%d to %H:%M")
        }
        tasks.append(task)
        task_id += 1

    save_tasks(tasks)


def update_task(task) -> None:
    """
    Met à jour une tâche existante.

    :param task: La tâche à mettre à jour
    :type task: Task
    """


def delete_task(task_id: int) -> None:
    """
    Supprime une tâche existante.

    :param task_id: L'identifiant de la tâche à supprimer
    :type task_id: int
    """

    data = load_tasks()

    # Gestion d'erreur
    if not data:
        print("Aucune tâche enregistrée.")
        return

    # Recherche de la tâche à supprimer
    task_to_delete = None
    for task in data:
        if task.get("id") == task_id:
            task_to_delete = task
            break

    if not task_to_delete:
        print("Tâche non trouvée.")
        return

    # Suppression de la tâche
    data.remove(task_to_delete)
    print(f"Tâche supprimée : [ID: {task_id} - {task_to_delete.get('description')}].")
    save_tasks(data)


# Lister les tâches
def list_tasks() -> None:
    """
    Liste toutes les tâches.

    :return: Une liste de tâches.
    """

    tasks = load_tasks()

    # # Gestion des erreurs
    if not tasks:
        print("Aucune tâche trouvée.")
        return

    for index, task in enumerate(tasks, start=1):
        description = task.get("description", "")
        task_status = task.get("status", "todo")
        print(f"{index:>2}- {description:<30} [{task_status.upper():^11}] ")
