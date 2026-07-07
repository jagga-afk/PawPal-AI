from __future__ import annotations

from typing import List


class Task:
    def __init__(
        self,
        description: str,
        duration_minutes: int = 10,
        priority: int = 1,
        frequency: str = "once",
        completed: bool = False,
    ) -> None:
        """Create a single pet-care task with timing and priority details."""
        self.description = description
        self.duration_minutes = duration_minutes
        self.priority = priority
        self.frequency = frequency
        self.completed = completed

    def complete(self) -> None:
        """Mark the task as completed."""
        self.completed = True

    def mark_incomplete(self) -> None:
        """Mark the task as not completed."""
        self.completed = False

    def update(self, **kwargs: object) -> None:
        """Update task attributes using keyword arguments."""
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)


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
        self._tasks: List[Task] = []

    def add_task(self, task: Task) -> None:
        """Attach a new task to this pet."""
        self._tasks.append(task)

    def remove_task(self, task: Task) -> None:
        """Remove a task from this pet if it exists."""
        if task in self._tasks:
            self._tasks.remove(task)

    def get_tasks(self) -> List[Task]:
        """Return a copy of this pet's current tasks."""
        return list(self._tasks)


class Owner:
    def __init__(
        self,
        name: str,
        availability_minutes: int = 120,
        preferences: List[str] | None = None,
    ) -> None:
        self.name = name
        self.availability_minutes = availability_minutes
        self.preferences = preferences if preferences is not None else []
        self.pets: List[Pet] = []

    def add_preference(self, preference: str) -> None:
        """Store a new owner preference if it is not already present."""
        if preference and preference not in self.preferences:
            self.preferences.append(preference)

    def update_availability(self, minutes: int) -> None:
        """Adjust how many minutes the owner has available for tasks."""
        self.availability_minutes = max(0, minutes)

    def add_pet(self, pet: Pet) -> None:
        """Register a pet with this owner."""
        if pet not in self.pets:
            self.pets.append(pet)

    def get_all_tasks(self) -> List[Task]:
        """Collect every task belonging to the owner's pets."""
        tasks: List[Task] = []
        for pet in self.pets:
            tasks.extend(pet.get_tasks())
        return tasks


class Scheduler:
    def plan_day(self, owner: Owner, available_minutes: int) -> tuple[list[Task], list[Task]]:
        """Build a simple daily plan using task priority and available time."""
        tasks = sorted(owner.get_all_tasks(), key=lambda task: (-task.priority, task.duration_minutes))
        scheduled: list[Task] = []
        skipped: list[Task] = []
        remaining = available_minutes

        for task in tasks:
            if task.completed:
                continue
            if task.duration_minutes <= remaining:
                scheduled.append(task)
                remaining -= task.duration_minutes
            else:
                skipped.append(task)

        return scheduled, skipped
