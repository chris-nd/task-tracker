"Module de point d'entrée de l'application"

import argparse
import sys

from task_cli.task import (
    create_tasks,
    delete_tasks,
    list_tasks,
    mark_done,
    mark_in_progress,
    update_task,
    filter_list_tasks
)


# Création un parser de ligne de commande
def create_parser() -> argparse.ArgumentParser:
    """
    Crée un parser de ligne de commande.

    :returns: Un objet parser configuré.
    :rtype: argparse.ArgumentParser
    """

    # Parser pour la commande principale
    parser = argparse.ArgumentParser(
        prog="task-cli",
        usage="task-cli <command> [argument]",
        description="Un outil en ligne de commande pour gérer le suivi des tâches",
        epilog="Pour plus d'informations, utilisez l'option -h ou --help",
        add_help=False,
    )

    # Flags d'options du parseur
    parser.add_argument("-h", "--help", action="help", help="Afficher l'aide")

    # Sous-parseurs pour regrouper les parsers des sous commandes
    subparsers = parser.add_subparsers(dest="command", required=True)

    # Parser pour la commande "add"
    add_parser = subparsers.add_parser(
        "add",
        usage="task-cli add <task>",
        description="Ajouter une tâche",
        prog="task-cli add",
        epilog="Pour plus d'informations, utilisez l'option -h ou --help",
        add_help=False,
    )

    add_parser.add_argument("task", nargs="+", help="La description de la tâche")
    add_parser.add_argument("-h", "--help", action="help", help="Afficher l'aide")

    # Parser pour la commande "update"
    update_parser = subparsers.add_parser(
        "update",
        prog="task-cli update",
        usage="task-cli update <id> <description>",
        description="Mettre à jour une tâche",
        epilog="Pour plus d'informations, utilisez l'option -h ou --help",
        add_help=False,
    )

    update_parser.add_argument(
        "id", type=int, nargs=1, help="Numéro de la tâche à mettre à jour"
    )
    update_parser.add_argument(
        "description", help="La nouvelle description de la tâche"
    )
    update_parser.add_argument("-h", "--help", action="help", help="Afficher l'aide")

    # Parser pour la commande delete
    delete_parser = subparsers.add_parser(
        "delete",
        prog="task-cli delete",
        usage="task-cli delete <id>",
        description="Supprimer une tâche",
        epilog="Pour plus d'informations, utilisez l'option -h ou --help",
        add_help=False,
    )

    delete_parser.add_argument(
        "id", type=int, nargs="+", help="Numéro de la tâche à supprimer"
    )
    delete_parser.add_argument("-h", "--help", action="help", help="Afficher l'aide")

    # Parser ppour la command mark-in-progress
    mark_in_progress_parser = subparsers.add_parser(
        "mark-in-progress",
        prog="task-cli mark-in-progress",
        usage="task-cli mark-in-progress <id>",
        description="Marquer une tâche comme en cours",
        epilog="Pour plus d'informations, utilisez l'option -h ou --help",
        add_help=False,
    )

    mark_in_progress_parser.add_argument(
        "id", type=int, nargs=1, help="Numéro de la tâche à marquer comme en cours"
    )
    mark_in_progress_parser.add_argument(
        "-h", "--help", action="help", help="Afficher l'aide"
    )

    # Parser pour la commande mark-done
    mark_done_parser = subparsers.add_parser(
        "mark-done",
        prog="task-cli mark-done",
        usage="task-cli mark-done <id>",
        description="Marquer une tâche comme terminée",
        epilog="Pour plus d'informations, utilisez l'option -h ou --help",
        add_help=False,
    )

    mark_done_parser.add_argument(
        "id", type=int, nargs=1, help="Numéro de la tâche à marquer comme terminée"
    )
    mark_done_parser.add_argument(
        "-h", "--help", action="help", help="Afficher l'aide"
    )

    # Parser pour la commande "list"
    list_parser = subparsers.add_parser(
        "list",
        usage="task-cli list [status]",
        description="Lister les tâches",
        prog="task-cli list",
        epilog="Pour plus d'informations, utilisez l'option -h ou --help",
        add_help=False,
    )

    list_parser.add_argument(
        "status",
        nargs="?",
        help="Afficher les tâches par statut",
        choices=["todo", "in-progress", "done"],
    )

    list_parser.add_argument("-h", "--help", action="help", help="Afficher l'aide")

    return parser


def main():
    "Fonction de lancement du programme."

    parser = create_parser()
    args = parser.parse_args()

    sys.stdout.write("\n")

    if args.command == "add":
        create_tasks(args.task)
    elif args.command == "update":
        update_task(args.id[0], args.description)
    elif args.command == "delete":
        delete_tasks(args.id)
    elif args.command == "mark-in-progress":
        mark_in_progress(args.id[0])
    elif args.command == "mark-done":
        mark_done(args.id[0])
    elif args.command == "list":
        if args.status == "todo":
            filter_list_tasks("todo")
        elif args.status == "in-progress":
            filter_list_tasks("in-progress")
        elif args.status == "done":
            filter_list_tasks("done")
        else:
            list_tasks()

    sys.stdout.write("\n")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
