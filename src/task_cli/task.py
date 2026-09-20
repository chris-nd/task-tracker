"Module décrivant les opérations sur les tâches"

from datetime import datetime

from task_cli.storage import load_tasks, remove_tasks, save_tasks, update_data


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


def delete_tasks(tasks_id: list[int]) -> None:
    """
    Supprime une tâche existante.

    :param tasks_id: Une liste d'identifiants de tâches à supprimer
    :type tasks_id: list[int]
    """

    remove_tasks(tasks_id)


# Marquer une tâche en cours
def mark_in_progress(task_id: int) -> None:
    """
    Marque une tâche comme en cours.

    :param task_id: L'identifiant de la tâche à marquer comme en cours
    :type task_id: int
    """

    # Gestion des erreurs
    if not task_id:
        print("Erreur : Aucun identifiant de tâche spécifié.")
        return

    if not isinstance(task_id, int):
        print("Erreur : L'identifiant de la tâche doit être un entier.")
        return

    data = load_tasks()

    if not data:
        print("Aucune tâche trouvée.")
        return

    for task in data:
        if task["id"] == task_id:
            task["status"] = "in-progress"
            task["updated_at"] = datetime.now().strftime("%Y-%m-%d to %H:%M")
            break
    else:
        print("Tâche non trouvée.")

    update_data(data)


# Marquer une tâche comme terminé
def mark_done(task_id: int) -> None:
    """
    Marque une tâche comme terminée.

    :param task_id: L'identifiant de la tâche à marquer comme terminée
    :type task_id: int
    """

    # Gestion des erreurs
    if not task_id:
        print("Erreur : Aucun identifiant de tâche spécifié.")
        return

    if not isinstance(task_id, int):
        print("Erreur : L'identifiant de la tâche doit être un entier.")
        return

    data = load_tasks()

    if not data:
        print("Aucune tâche trouvée.")
        return

    for task in data:
        if task["id"] == task_id:
            task["status"] = "done"
            task["updated_at"] = datetime.now().strftime("%Y-%m-%d to %H:%M")
            break
    else:
        print("Tâche non trouvée.")

    update_data(data)


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
