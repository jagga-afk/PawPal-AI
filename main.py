from pawpal_system import Owner, Pet, Scheduler, Task


def main() -> None:
    owner = Owner("Alex", availability_minutes=60)

    biscuit = Pet("Biscuit", "dog", 3)
    mochi = Pet("Mochi", "cat", 2)

    owner.add_pet(biscuit)
    owner.add_pet(mochi)

    biscuit.add_task(Task("Morning walk", duration_minutes=20, priority=3, frequency="daily"))
    biscuit.add_task(Task("Feed breakfast", duration_minutes=10, priority=2, frequency="daily"))
    mochi.add_task(Task("Litter check", duration_minutes=15, priority=4, frequency="daily"))

    scheduler = Scheduler()
    scheduled, skipped = scheduler.plan_day(owner, owner.availability_minutes)

    print("Today's Schedule")
    print("=" * 20)
    for task in scheduled:
        print(f"- {task.description} ({task.duration_minutes} min)")

    if skipped:
        print("\nSkipped:")
        for task in skipped:
            print(f"- {task.description} ({task.duration_minutes} min)")


if __name__ == "__main__":
    main()
