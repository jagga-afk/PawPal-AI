from pawpal_system import Owner, Pet, Scheduler, Task


def test_task_completion_toggle():
    task = Task("Feed Biscuit", duration_minutes=10, priority=3, frequency="daily")

    assert task.completed is False

    task.complete()
    assert task.completed is True

    task.mark_incomplete()
    assert task.completed is False


def test_pet_tracks_tasks():
    pet = Pet("Biscuit", "dog", 3)
    task = Task("Walk", duration_minutes=15, priority=2)

    pet.add_task(task)
    assert pet.get_tasks() == [task]

    pet.remove_task(task)
    assert pet.get_tasks() == []


def test_owner_collects_tasks_from_all_pets():
    owner = Owner("Alex")
    pet_one = Pet("Biscuit", "dog", 3)
    pet_two = Pet("Mochi", "cat", 2)

    pet_one.add_task(Task("Feed", duration_minutes=10, priority=2))
    pet_two.add_task(Task("Groom", duration_minutes=20, priority=4))

    owner.add_pet(pet_one)
    owner.add_pet(pet_two)

    tasks = owner.get_all_tasks()
    assert len(tasks) == 2
    assert [task.description for task in tasks] == ["Feed", "Groom"]


def test_scheduler_prioritizes_and_schedules_tasks():
    owner = Owner("Alex")
    pet = Pet("Biscuit", "dog", 3)

    pet.add_task(Task("Walk", duration_minutes=15, priority=3))
    pet.add_task(Task("Feed", duration_minutes=10, priority=2))
    owner.add_pet(pet)

    scheduler = Scheduler()
    scheduled, skipped = scheduler.plan_day(owner, 25)

    assert [task.description for task in scheduled] == ["Walk", "Feed"]
    assert skipped == []
