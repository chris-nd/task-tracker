"Module de test pour les fonctions de stockage."

import json
import os
import sys

import pytest

from task_cli.storage import load_data, remove_data, save_data, update_data
from task_cli.tests.test_temp_file import mock_data_fixture, test_create_temp_file


def test_load_data(tmp_path, mock_data):
    """
    Test la lecture des données depuis le stockage.
    """
    d = tmp_path / "src/task_cli/data"
    d.mkdir(parents=True, exist_ok=True)
    p = d / "tasks.json"
    p.write_text(json.dumps(mock_data), encoding="utf-8")

    assert load_data(p) == mock_data
    assert load_data() == []

    if not p.read_text(encoding="utf-8").strip():
        assert load_data(p) == []

    if not isinstance(load_data(p), list):
        assert sys.stderr.read() == "Erreur : le fichier tasks.json ne contient pas une liste de tâches."
        assert load_data(p) == []


def test_save_data():
    """
    Test l'enregistrement des données dans le stockage.
    """



def test_update_data():
    """
    Test la mise à jour des données dans le stockage.
    """



def test_remove_data():
    """
    Test la suppression des données depuis le stockage.
    """
