"Module de point d'entrée de l'application"

import argparse


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

    if args.command == "add":
        print(f'Tâche ajoutée : {args.task}')
    elif args.command == "list":
        print(f'Tâches affichées : {args.status}')


if __name__ == "__main__":
    main()
