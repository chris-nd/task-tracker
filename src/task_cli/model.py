"Module décrivant le modèle de données pour les tâches"

from dataclasses import dataclass
from enum import Enum


class TaskStatus(Enum):
    "Enumération des statuts possibles pour une tâche."
    TODO = "todo"
    IN_PROGRESS = "in-progress"
    DONE = "done"


@dataclass
class Task:
    "Classe représentant une tâche."
    id: int
    description: str
    status: TaskStatus
    created_at: str
    updated_at: str
