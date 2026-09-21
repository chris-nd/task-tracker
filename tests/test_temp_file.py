"Module de test pour les fichiers temporaires."

import json

import pytest


@pytest.fixture(name="mock_data")
def mock_data_fixture():
    """
    Fixture pour fournir des données de tâche fictives.
    """
    return [
        {
            "id": 1,
            "description": "Task 1",
            "status": "done",
            "created_at": "2026-09-01 to 00:00",
            "updated_at": "2026-09-01 to 00:00"
        },
        {
            "id": 2,
            "description": "Task 2",
            "status": "in-progress",
            "created_at": "2026-09-01 to 00:00",
            "updated_at": "2026-09-01 to 00:00"
        },
        {
            "id": 3,
            "description": "Task 3",
            "status": "todo",
            "created_at": "2026-09-01 to 00:00",
            "updated_at": "2026-09-01 to 00:00"
        }
    ]


def test_create_temp_file(tmp_path, mock_data):
    """
    Test la création d'un fichier temporaire.

    :param tmp_path: Le chemin vers le dossier temporaire.
    :param mock_data: Les données de tâche fictives.
    """
    d = tmp_path / "src/task_cli/data"
    d.mkdir(parents=True, exist_ok=True)
    p = d / "tasks.json"
    p.write_text(json.dumps(mock_data), encoding="utf-8")
    assert p.read_text(encoding="utf-8") == json.dumps(mock_data)
    assert len(list(tmp_path.iterdir())) == 1
