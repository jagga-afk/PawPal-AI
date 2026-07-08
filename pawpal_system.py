from __future__ import annotations

from datetime import datetime, timedelta
from typing import List


class Task:
    def __init__(
        self,
        description: str,
        duration_minutes: int = 10,
        priority: int = 1,
        frequency: str = "once",
        completed: bool = False,
        time: str = "",
        pet_name: str | None = None,
    ) -> None:
        """Create a single pet-care task with timing and priority details."""
        self.description = description
        self.duration_minutes = duration_minutes
        self.priority = priority
        self.frequency = frequency
        self.completed = completed
        self.time = time
        self.pet_name = pet_name

    def complete(self) -> None:
        """Mark the task as completed."""
        self.completed = True

    def mark_incomplete(self) -> None:
        """Mark the task as not completed."""
        self.completed = False

    def mark_complete_and_schedule_next(self) -> "Task | None":
        """Mark the task complete and create a recurring follow-up task."""
        self.complete()
        if self.frequency.lower() in {"daily", "weekly"}:
            delta_days = 1 if self.frequency.lower() == "daily" else 7
            next_time = datetime.now().date() + timedelta(days=delta_days)
            return Task(
                description=self.description,
                duration_minutes=self.duration_minutes,
                priority=self.priority,
                frequency=self.frequency,
                completed=False,
                time=next_time.strftime("%Y-%m-%d"),
            )
        return None

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
        task.pet_name = self.name
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

    def sort_by_time(self, tasks: List[Task]) -> List[Task]:
        """Sort tasks by their time value, treating missing values as the end."""
        return sorted(tasks, key=lambda task: task.time or "99:99")

    def filter_tasks(self, tasks: List[Task], pet_name: str | None = None, completed_only: bool = False) -> List[Task]:
        """Filter tasks by pet name and completion status."""
        filtered: List[Task] = []
        for task in tasks:
            matches_pet = not pet_name or task.pet_name == pet_name
            matches_status = not completed_only or task.completed
            if matches_pet and matches_status:
                filtered.append(task)
        return filtered

    def detect_conflicts(self, tasks: List[Task]) -> List[str]:
        """Return simple warning messages when tasks overlap in time."""
        warnings: List[str] = []
        for index, task in enumerate(tasks):
            for other in tasks[index + 1 :]:
                if task.time and other.time and task.time == other.time:
                    warnings.append(f"Conflict: {task.description} and {other.description} share time {task.time}.")
        return warnings
