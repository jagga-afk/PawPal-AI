# AI Interactions Log

> **Stretch features only.** Only fill in the sections that apply to stretch features you attempted. If you did not attempt a stretch feature, leave its section blank or delete it. This file is not required for the core project.

---

## Agent Workflow (SF7)

> Document your experience using an AI agent (e.g., Cursor Agent, Claude, Copilot) to make multi-step changes autonomously.

**What task did you give the agent?**

I asked the AI coding assistant to help turn the initial PawPal+ prototype into a more intelligent scheduler by adding sorting, filtering, recurring-task behavior, conflict detection, tests, and updated documentation.

**What did the agent do?**

The assistant helped me:

- Extend the core classes in pawpal_system.py with new scheduling methods
- Add a terminal demo in main.py that shows the new behavior
- Update app.py so the Streamlit UI reflects the smarter logic
- Draft and refine tests in tests/test_smart_scheduler.py
- Improve README.md, reflection.md, and the Mermaid UML files
- Suggest small refactors for readability and performance

**What did you have to verify or fix manually?**

I had to review the generated code carefully to make sure the logic matched the project requirements. In particular, I verified the recurring-task behavior, checked that the filter logic actually used the pet name, and confirmed that the tests reflected real scheduler behavior rather than overly permissive implementations.

---

## Prompt Comparison (SF11)

> Compare two different prompts (or two different models) on the same task.

| | Option A | Option B |
|-|----------|----------|
| **Model / tool used** | GitHub Copilot in the editor | GitHub Copilot in a separate chat session |
| **Prompt** | “Add sorting, filtering, conflict detection, and recurring tasks to pawpal_system.py.” | “How could this algorithm be simplified for better readability or performance?” |
| **Response summary** | Produced a direct implementation plan and code changes quickly. | Produced a shorter refactoring suggestion with clarity-focused advice. |
| **What was useful** | Good for making concrete edits and wiring the logic into the project files. | Good for improving readability without changing behavior. |
| **Problems noticed** | Some suggestions were a bit too broad and needed human review. | The suggestion was elegant but needed adaptation to fit the existing class structure. |
| **Decision** | I used the first approach for implementation and the second approach for refinement. |

**Which approach did you use in your final implementation and why?**

I used the implementation-focused approach for the main build because it was faster and more practical for adding the new features. I used the refactoring-style prompt afterward to simplify and clarify the logic, because that helped keep the scheduler readable while still improving performance.
