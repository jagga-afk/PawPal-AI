from pawpal_system import Owner, Pet, Scheduler, Task


def main() -> None:
    owner = Owner("Alex", availability_minutes=60)

    biscuit = Pet("Biscuit", "dog", 3)
    mochi = Pet("Mochi", "cat", 2)

    owner.add_pet(biscuit)
    owner.add_pet(mochi)

    morning_walk = Task("Morning walk", duration_minutes=20, priority=3, frequency="daily", time="08:00")
    feed_breakfast = Task("Feed breakfast", duration_minutes=10, priority=2, frequency="daily", time="07:30")
    litter_check = Task("Litter check", duration_minutes=15, priority=4, frequency="daily", time="08:00")
    biscuit.add_task(morning_walk)
    biscuit.add_task(feed_breakfast)
    mochi.add_task(litter_check)

    scheduler = Scheduler()
    all_tasks = owner.get_all_tasks()
    sorted_tasks = scheduler.sort_by_time(all_tasks)
    filtered_tasks = scheduler.filter_tasks(all_tasks, pet_name="Biscuit", completed_only=False)
    conflicts = scheduler.detect_conflicts(sorted_tasks)

    scheduled, skipped = scheduler.plan_day(owner, owner.availability_minutes)

    print("Today's Schedule")
    print("=" * 20)
    for task in scheduled:
        print(f"- {task.description} ({task.duration_minutes} min)")

    if skipped:
        print("\nSkipped:")
        for task in skipped:
            print(f"- {task.description} ({task.duration_minutes} min)")

    print("\nSorted tasks:")
    for task in sorted_tasks:
        print(f"- {task.description} at {task.time or 'unscheduled'}")

    print("\nBiscuit tasks:")
    for task in filtered_tasks:
        print(f"- {task.description}")

    if conflicts:
        print("\nWarnings:")
        for warning in conflicts:
            print(f"- {warning}")


if __name__ == "__main__":
    main()
