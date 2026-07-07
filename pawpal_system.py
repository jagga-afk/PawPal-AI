from __future__ import annotations

from typing import List


class Owner:
    def __init__(self, name: str, availability_minutes: int = 120, preferences: List[str] | None = None) -> None:
        self.name = name
        self.availability_minutes = availability_minutes
        self.preferences = preferences if preferences is not None else []

    def add_preference(self, preference: str) -> None:
        pass

    def update_availability(self, minutes: int) -> None:
        pass


class Pet:
    def __init__(
        self,
        name: str,
        species: str,
        age: int,
        special_needs: List[str] | None = None,
        notes: str = "",
    ) -> None:
        self.name = name
        self.species = species
        self.age = age
        self.special_needs = special_needs if special_needs is not None else []
        self.notes = notes


class Task:
    def __init__(
        self,
        title: str,
        category: str,
        duration_minutes: int,
        priority: int = 1,
        preferred_time: str = "anytime",
        recurring: bool = False,
    ) -> None:
        self.title = title
        self.category = category
        self.duration_minutes = duration_minutes
        self.priority = priority
        self.preferred_time = preferred_time
        self.recurring = recurring

    def update_task(
        self,
        *,
        title: str | None = None,
        category: str | None = None,
        duration_minutes: int | None = None,
        priority: int | None = None,
        preferred_time: str | None = None,
        recurring: bool | None = None,
    ) -> None:
        pass


class TaskManager:
    def __init__(self, tasks: List[Task] | None = None) -> None:
        self.tasks = tasks if tasks is not None else []

    def add_task(self, task: Task) -> None:
        pass

    def edit_task(self, index: int, task: Task) -> None:
        pass

    def remove_task(self, index: int) -> None:
        pass

    def sort_tasks(self) -> List[Task]:
        return []


class DailyPlan:
    def __init__(self, date: str, scheduled_tasks: List[Task] | None = None, reasoning: List[str] | None = None) -> None:
        self.date = date
        self.scheduled_tasks = scheduled_tasks if scheduled_tasks is not None else []
        self.reasoning = reasoning if reasoning is not None else []

    def display_plan(self) -> str:
        return ""


class Scheduler:
    def generate_plan(self, owner: Owner, pet: Pet, task_manager: TaskManager) -> DailyPlan:
        return DailyPlan(date="today")

    def prioritize_tasks(self, tasks: List[Task]) -> List[Task]:
        return []

    def resolve_conflicts(self, tasks: List[Task]) -> List[Task]:
        return []

    def explain_reasoning(self, tasks: List[Task]) -> List[str]:
        return []
