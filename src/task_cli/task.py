"Module décrivant les opérations sur les tâches"

from task_cli.storage import load_tasks


def create_task(desc: str) -> list:
    """
    Crée une nouvelle tâche.

    :param desc: La description de la tâche
    :type desc: str
    :return: La tâche créée
    :rtype: Task
    """
    return []


def update_task(task) -> None:
    """
    Met à jour une tâche existante.

    :param task: La tâche à mettre à jour
    :type task: Task
    """


def delete_task(task) -> None:
    """
    Supprime une tâche existante.

    :param task: La tâche à supprimer
    :type task: Task
    """


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
