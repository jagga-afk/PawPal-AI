from pawpal_system import Pet, Task


def test_task_completion_updates_status():
    task = Task("Walk", duration_minutes=15, priority=2)

    assert task.completed is False

    task.complete()

    assert task.completed is True


def test_add_task_increases_pet_task_count():
    pet = Pet("Biscuit", "dog", 3)
    task = Task("Feed", duration_minutes=10, priority=1)

    pet.add_task(task)

    assert len(pet.get_tasks()) == 1
