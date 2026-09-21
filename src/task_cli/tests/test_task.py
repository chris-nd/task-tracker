"Module de test pour les tâches"

import pytest

from task_cli.task import (
    create_tasks,
    delete_tasks,
    list_tasks,
    mark_done,
    mark_in_progress,
    update_task,
)


@pytest.mark.parametrize("task", ["Task 1", "Task 2"])
def test_create_tasks(task):
    """
    Test la création de tâches

    :param task: La tâche à créer
    """

    assert create_tasks(task) == 0
    assert create_tasks([]) == 1


@pytest.mark.parametrize("task_id", [1, 2])
@pytest.mark.parametrize("new_description", ["Updated Task 1", "Updated Task 2"])
def test_update_task(task_id, new_description):
    """
    Test la mise à jour d'une tâche

    :param task_id: L'ID de la tâche à mettre à jour
    :param new_description: La nouvelle description de la tâche
    """

    assert update_task(task_id, new_description) == 0


@pytest.mark.parametrize("task_ids", [[1], [2], [1, 2]])
def test_delete_tasks(task_ids):
    """
    Test la suppression de tâches

    :param task_ids: La liste des IDs des tâches à supprimer
    """

    assert delete_tasks(task_ids) == 0


@pytest.mark.parametrize("task_id", [1, 2])
def test_mark_done(task_id):
    """
    Test le marquage d'une tâche comme terminée

    :param task_id: L'ID de la tâche à marquer comme terminée
    """

    assert mark_done(task_id) == 0


@pytest.mark.parametrize("task_id", [1, 2])
def test_mark_in_progress(task_id):
    """
    Test le marquage d'une tâche comme en cours

    :param task_id: L'ID de la tâche à marquer comme en cours
    """

    assert mark_in_progress(task_id) == 0


def test_list_tasks():
    """
    Test la liste des tâches
    """

    assert list_tasks() == 0
