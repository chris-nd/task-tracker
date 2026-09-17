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

    return parser


def main():
    "Fonction de lancement du programme."

    parser = create_parser()
    args = parser.parse_args()


if __name__ == "__main__":
    main()
