"Module de test pour les fonctions de stockage."

import json
import sys
from pathlib import Path

import pytest

from task_cli.storage import load_data, remove_data, save_data, update_data
from task_cli.tests.test_temp_file import mock_data_fixture


def read_temp_file(tmp_path, mock_data) -> Path:
    """
    Lit le fichier temporaire.

    :param tmp_path: Le chemin vers le dossier temporaire.
    :param mock_data: Les données de tâche fictives.
    :return: Le chemin vers le fichier temporaire.
    """

    d = tmp_path / "src/task_cli/data"
    d.mkdir(parents=True, exist_ok=True)
    p = d / "tasks.json"
    p.write_text(json.dumps(mock_data), encoding="utf-8")
    return p


def access_temp_file(tmp_path) -> Path:
    """
    Accède au fichier temporaire.

    :param tmp_path: Le chemin vers le dossier temporaire.
    :return: Le chemin vers le fichier temporaire.
    """

    d = tmp_path / "src/task_cli/data"
    d.mkdir(parents=True, exist_ok=True)
    p = d / "tasks.json"
    return p


def list_tasks_id(tmp_path, mock_data):
    """
    Liste les identifiants des tâches.

    :param tmp_path: Le chemin vers le dossier temporaire.
    :param mock_data: Les données de tâche fictives.
    :return: Une liste des identifiants des tâches.
    """
    p = read_temp_file(tmp_path, mock_data)
    tasks = load_data(p)
    return [task["id"] for task in tasks]


def test_load_data(tmp_path, mock_data):
    """
    Test la lecture des données depuis le stockage.

    :param tmp_path: Le chemin vers le dossier temporaire.
    :param mock_data: Les données de tâche fictives.
    """

    p = read_temp_file(tmp_path, mock_data)

    assert load_data(p) == mock_data
    assert load_data() == []

    if not p.read_text(encoding="utf-8").strip():
        assert load_data(p) == []

    if not isinstance(load_data(p), list):
        assert (
            sys.stderr.read()
            == "Erreur : le fichier tasks.json ne contient pas une liste de tâches."
        )
        assert load_data(p) == []


def test_save_data(tmp_path, mock_data):
    """
    Test l'enregistrement des données dans le stockage.
    """
    p = access_temp_file(tmp_path)

    assert save_data(mock_data, p) == 0

    if not mock_data:
        assert save_data(mock_data, p) == 1


@pytest.mark.parametrize(
    "data",
    [
        (
            [
                {
                    "id": 1,
                    "description": "Task 1",
                    "status": "done",
                    "created_at": "2026-09-01 to 00:00",
                    "updated_at": "2026-09-01 to 00:00",
                }
            ]
        )
    ],
)
def test_update_data(tmp_path, mock_data, data):
    """
    Test la mise à jour des données dans le stockage.

    :param tmp_path: Le chemin vers le dossier temporaire.
    :param mock_data: Les données de tâche fictives.
    :param data: Les données à mettre à jour.
    """

    p = access_temp_file(tmp_path)

    assert update_data(mock_data + data, p) == 0


def test_remove_data(tmp_path, mock_data):
    """
    Test la suppression des données depuis le stockage.
    """

    tasks_id = list_tasks_id(tmp_path, mock_data)
    p = access_temp_file(tmp_path)

    assert remove_data(tasks_id, p) == 0

    if not tasks_id:
        assert remove_data(tasks_id, p) == 1
