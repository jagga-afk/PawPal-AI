import streamlit as st

from pawpal_system import Owner, Pet, Scheduler, Task

st.set_page_config(page_title="PawPal+", page_icon="🐾", layout="centered")

st.title("🐾 PawPal+")

st.markdown(
    """
Welcome to the PawPal+ starter app.

This file is intentionally thin. It gives you a working Streamlit app so you can start quickly,
but **it does not implement the project logic**. Your job is to design the system and build it.

Use this app as your interactive demo once your backend classes/functions exist.
"""
)

with st.expander("Scenario", expanded=True):
    st.markdown(
        """
**PawPal+** is a pet care planning assistant. It helps a pet owner plan care tasks
for their pet(s) based on constraints like time, priority, and preferences.

You will design and implement the scheduling logic and connect it to this Streamlit UI.
"""
    )

with st.expander("What you need to build", expanded=True):
    st.markdown(
        """
At minimum, your system should:
- Represent pet care tasks (what needs to happen, how long it takes, priority)
- Represent the pet and the owner (basic info and preferences)
- Build a plan/schedule for a day that chooses and orders tasks based on constraints
- Explain the plan (why each task was chosen and when it happens)
"""
    )

st.divider()

st.subheader("Quick Demo Inputs (UI only)")

if "owner" not in st.session_state:
    st.session_state.owner = Owner(name="Jordan")

owner_name = st.text_input("Owner name", value=st.session_state.owner.name)

with st.expander("Add a pet", expanded=False):
    with st.form("pet_form"):
        pet_name = st.text_input("Pet name", value="Mochi")
        species = st.selectbox("Species", ["dog", "cat", "other"])
        age = st.number_input("Age", min_value=0, max_value=30, value=1)
        submitted_pet = st.form_submit_button("Add pet")

        if submitted_pet:
            new_pet = Pet(name=pet_name, species=species, age=int(age))
            st.session_state.owner.add_pet(new_pet)
            st.success(f"Added {new_pet.name} to {st.session_state.owner.name}'s pets.")

st.markdown("### Tasks")
st.caption("Add a few tasks. These are stored on the selected pet and shown below.")

col1, col2, col3 = st.columns(3)
with col1:
    task_title = st.text_input("Task title", value="Morning walk")
with col2:
    duration = st.number_input("Duration (minutes)", min_value=1, max_value=240, value=20)
with col3:
    priority = st.selectbox("Priority", ["low", "medium", "high"], index=2)

if st.button("Add task"):
    if not st.session_state.owner.pets:
        default_pet = Pet(name="Mochi", species="dog", age=1)
        st.session_state.owner.add_pet(default_pet)

    target_pet = st.session_state.owner.pets[0]
    task_priority = 1 if priority == "low" else 2 if priority == "medium" else 3
    task = Task(description=task_title, duration_minutes=int(duration), priority=task_priority)
    target_pet.add_task(task)
    st.success(f"Added task to {target_pet.name}.")

if st.session_state.owner.pets:
    st.write("Current pets:")
    for pet in st.session_state.owner.pets:
        st.write(f"- {pet.name} ({pet.species}, age {pet.age})")
        if pet.get_tasks():
            for task in pet.get_tasks():
                st.write(f"  • {task.description} ({task.duration_minutes} min)")
        else:
            st.write("  • No tasks yet")
else:
    st.info("No pets yet. Add one above.")

st.divider()

st.subheader("Build Schedule")
st.caption("This button should call your scheduling logic once you implement it.")

if st.button("Generate schedule"):
    st.session_state.owner.name = owner_name
    if not st.session_state.owner.pets:
        default_pet = Pet(name="Mochi", species="dog", age=1)
        st.session_state.owner.add_pet(default_pet)

    scheduler = Scheduler()
    scheduled, skipped = scheduler.plan_day(st.session_state.owner, st.session_state.owner.availability_minutes)
    sorted_tasks = scheduler.sort_by_time(st.session_state.owner.get_all_tasks())
    pet_tasks = scheduler.filter_tasks(st.session_state.owner.get_all_tasks(), pet_name=st.session_state.owner.pets[0].name)
    conflicts = scheduler.detect_conflicts(sorted_tasks)

    st.success("Schedule generated")
    if scheduled:
        st.write("### Scheduled tasks")
        for task in scheduled:
            st.write(f"- {task.description} ({task.duration_minutes} min)")
    if skipped:
        st.write("### Skipped tasks")
        for task in skipped:
            st.write(f"- {task.description} ({task.duration_minutes} min)")

    if sorted_tasks:
        st.write("### Sorted tasks")
        for task in sorted_tasks:
            st.write(f"- {task.description} at {task.time or 'unscheduled'}")

    if pet_tasks:
        st.write("### Tasks for first pet")
        for task in pet_tasks:
            st.write(f"- {task.description}")

    if conflicts:
        st.warning("### Possible conflicts")
        for warning in conflicts:
            st.write(f"- {warning}")
