from datetime import datetime, timedelta

from pawpal_system import Owner, Pet, Scheduler, Task


def test_sort_by_time_uses_time_values():
    scheduler = Scheduler()
    tasks = [
        Task("Later", duration_minutes=15, priority=1, time="10:30"),
        Task("Earlier", duration_minutes=10, priority=1, time="08:00"),
    ]

    sorted_tasks = scheduler.sort_by_time(tasks)

    assert [task.description for task in sorted_tasks] == ["Earlier", "Later"]


def test_filter_tasks_by_pet_and_completion_status():
    pet = Pet("Biscuit", "dog", 3)
    done_task = Task("Feed", duration_minutes=10, priority=2, time="09:00")
    pending_task = Task("Walk", duration_minutes=20, priority=3, time="10:00")
    done_task.complete()
    pet.add_task(done_task)
    pet.add_task(pending_task)

    scheduler = Scheduler()
    filtered = scheduler.filter_tasks([done_task, pending_task], pet_name="Biscuit", completed_only=True)

    assert [task.description for task in filtered] == ["Feed"]


def test_recurring_task_creates_next_instance_after_completion():
    task = Task("Medicine", duration_minutes=5, priority=4, frequency="daily", time="08:00")
    next_task = task.mark_complete_and_schedule_next()

    assert task.completed is True
    assert next_task is not None
    assert next_task.frequency == "daily"
    assert next_task.time == (datetime.now().date() + timedelta(days=1)).strftime("%Y-%m-%d")


def test_conflict_detection_reports_overlap():
    scheduler = Scheduler()
    pet = Pet("Biscuit", "dog", 3)
    task_a = Task("Feed", duration_minutes=20, priority=2, time="09:00")
    task_b = Task("Walk", duration_minutes=20, priority=3, time="09:00")
    pet.add_task(task_a)
    pet.add_task(task_b)

    warnings = scheduler.detect_conflicts([task_a, task_b])

    assert warnings
    assert "conflict" in warnings[0].lower()
