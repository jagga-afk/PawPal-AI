# PawPal+ Project Reflection

## 1. System Design

**a. Initial design**

My initial UML design centered on four core concepts: Owner, Pet, Task, and Scheduler. The Owner held availability and preferences, the Pet stored identity and care needs, the Task represented an action with duration and priority, and the Scheduler decided how tasks should be arranged into a daily plan.

**b. Design changes**

The implementation stayed close to that structure, but I simplified it by making the relationship more direct: each Pet owns its own tasks, and the Owner aggregates the tasks from all pets. I also added recurring-task behavior directly to the Task class and made the Scheduler responsible for time sorting, filtering, and conflict warnings. That kept the design easier to explain and easier to test.

---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

The scheduler currently considers task duration, priority, and assigned time. It also respects the owner's available minutes when building the daily plan. I treated priority and time as the most important factors because they most directly affect whether a task is scheduled and when it appears in the day.

**b. Tradeoffs**

One tradeoff is that conflict detection only checks for exact time matches instead of overlapping durations. That is a reasonable simplification for this project because it keeps the logic lightweight, readable, and easy to explain to a pet owner. It also avoids overcomplicating the scheduler with interval math that is not required for the current demo.

---

## 3. AI Collaboration

**a. How you used AI**

I used AI to brainstorm the class structure, generate the initial implementation, refine the scheduler methods, draft tests, and improve the project documentation. The most helpful prompts asked for concrete code examples, test cases, and small refactoring suggestions that I could evaluate against the requirements.

**b. Judgment and verification**

One AI suggestion I did not accept as-is was a more compact conflict-checking implementation that used a dense one-liner. It was elegant, but it was harder for me to read and reason about. I kept a more explicit loop-based version and verified it by running the test suite and the demo script so the behavior was still correct.

---

## 4. Testing and Verification

**a. What you tested**

I tested sorting correctness, recurrence behavior, conflict detection, task completion, pet-task association, and the scheduler's day-planning logic. These tests were important because they cover the core behaviors that make the system feel intelligent rather than just static.

**b. Confidence**

I am moderately confident in the scheduler's correctness. The automated tests are passing, and the CLI demo shows the expected behavior. If I had more time, I would test edge cases such as overlapping durations, empty task lists, invalid time values, and tasks that exceed the owner's available time.

---

## 5. Reflection

**a. What went well**

I am most satisfied with how the core logic now works end to end: the app can sort tasks, filter them, detect conflicts, and create recurring follow-up tasks in a way that is easy to demonstrate.

**b. What you would improve**

If I had another iteration, I would improve the UI so it lets the user set times and recurrence more naturally, and I would make the conflict logic more sophisticated by handling overlapping time windows rather than only exact matches.

**c. Key takeaway**

A major lesson from this project was that AI is most useful when the human acts as the architect and reviewer. The AI can generate implementation quickly, but the human still needs to guide the structure, evaluate tradeoffs, and verify that the solution matches the real goals of the system.
