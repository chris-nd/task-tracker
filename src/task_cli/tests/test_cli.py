"Module de test pour le CLI"

import pytest

from task_cli.cli import create_parser


def test_create_parser():
    """
    Test la création d'un parser
    """
    parser = create_parser()

    assert parser is not None
    assert parser.prog == "task-cli"
    assert parser._subparsers is not None


def test_parser_command():
    """
    Test le parsing des commandes
    """
    parser = create_parser()

    # Test de la commande "add"
    args = parser.parse_args(["add", "Task 1"])
    assert args.command == "add"
    assert args.task == ["Task 1"]

    # Test de la commande "update"
    args = parser.parse_args(["update", "1", "Updated Task 1"])
    assert args.command == "update"
    assert args.id == [1]
    assert args.description == "Updated Task 1"

    # Test de la commande "delete"
    args = parser.parse_args(["delete", "1"])
    assert args.command == "delete"
    assert args.id == [1]

    # Test de la commande "mark-in-progress"
    args = parser.parse_args(["mark-in-progress", "1"])
    assert args.command == "mark-in-progress"
    assert args.id == [1]

    # Test de la commande "mark-done"
    args = parser.parse_args(["mark-done", "1"])
    assert args.command == "mark-done"
    assert args.id == [1]

    # Test de la commande "list"
    args = parser.parse_args(["list"])
    assert args.command == "list"
