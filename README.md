# PawPal+ (Module 2 Project)

PawPal+ is a Streamlit-based pet-care planner that helps an owner organize daily tasks for one or more pets. The system combines a Python logic layer with a simple UI so a user can add pets, attach tasks, and generate a schedule based on priority, duration, and timing.

## Scenario

A busy pet owner needs help staying consistent with daily care. PawPal+ supports:

- Tracking pet-care tasks such as walks, feeding, and litter checks
- Using constraints like time availability, priority, and task timing
- Producing a daily plan that can sort, filter, and flag conflicts

## What the app does

- Lets a user enter owner and pet information
- Lets a user add tasks with duration, priority, and optional time values
- Generates a daily schedule based on available minutes
- Shows smarter behaviors such as time-based sorting, pet-based filtering, recurring tasks, and conflict warnings
- Includes automated tests for the scheduler logic

## Getting started

### Setup

```bash
python -m venv .venv
.venv\Scripts\activate  # Windows
pip install -r requirements.txt
```

### Run the demo

```bash
python main.py
```

## 🖥️ Sample Output

The terminal demo below shows the current scheduling output from the logic layer:

```text
Today's Schedule
====================
- Litter check (15 min)
- Morning walk (20 min)
- Feed breakfast (10 min)

Sorted tasks:
- Feed breakfast at 07:30
- Morning walk at 08:00
- Litter check at 08:00

Biscuit tasks:
- Morning walk
- Feed breakfast

Warnings:
- Conflict: Morning walk and Litter check share time 08:00.
```

## 🧪 Testing PawPal+

Run the full automated test suite with:

```bash
python -m pytest
```

Verified output:

```text
..........                                                               [100%]
10 passed in 0.03s
```

Confidence level: ★★★★★

## 📐 Smarter Scheduling

| Feature | Method | Description |
|---------|--------|-------------|
| Sorting by time | Scheduler.sort_by_time() | Orders tasks by their assigned time value so the schedule is easier to read. |
| Filtering by pet or completion | Scheduler.filter_tasks() | Returns tasks for a chosen pet and optionally only completed tasks. |
| Conflict detection | Scheduler.detect_conflicts() | Flags tasks that share the same time so the owner can adjust the schedule. |
| Recurring task logic | Task.mark_complete_and_schedule_next() | Marks a task complete and creates a follow-up task for the next day or week. |
| Daily planning | Scheduler.plan_day() | Chooses the highest-priority tasks that fit within the owner's available minutes. |

## 📸 Demo Walkthrough

1. Open the Streamlit app and enter an owner name.
2. Add one or more pets and attach tasks such as feeding, walks, or litter checks.
3. Click Generate schedule to create a daily plan based on priority and time availability.
4. Review the sorted task list, filtered pet tasks, and any conflict warnings that appear.
5. Complete a recurring task to see a follow-up task created automatically for the next day or week.

## 📁 Project Files

- [pawpal_system.py](pawpal_system.py) contains the core classes and scheduling logic.
- [app.py](app.py) provides the Streamlit interface.
- [main.py](main.py) runs a console demo of the scheduler.
- [tests/test_pawpal.py](tests/test_pawpal.py) and [tests/test_smart_scheduler.py](tests/test_smart_scheduler.py) contain the automated tests.
- [diagrams/uml.mmd](diagrams/uml.mmd) and [diagrams/uml_final.mmd](diagrams/uml_final.mmd) store the Mermaid UML diagrams.
