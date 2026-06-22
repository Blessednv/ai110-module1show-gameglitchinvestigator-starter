# AI Interactions Log

> **Stretch features only.** Only fill in the sections that apply to stretch features you attempted. If you did not attempt a stretch feature, leave its section blank or delete it. This file is not required for the core project.

---

## Agent Workflow (SF8)

> Document your experience using an AI agent (e.g., Cursor Agent, Claude, Copilot) to make multi-step changes autonomously.

**What task did you give the agent?**

<!-- Describe the goal you asked the agent to accomplish -->

**What did the agent do?**

<!-- List the steps the agent took (files edited, commands run, etc.) -->

**What did you have to verify or fix manually?**

<!-- Describe anything the agent got wrong or that required human review -->

---

## Test Generation (SF7)

> Document how you used AI to help generate or improve tests.

**Prompt used to identify edge cases:**

> "Look at parse_guess and check_guess in logic_utils.py. Identify three potential edge-case inputs — such as negative numbers, decimals, or extremely large values — that a player might type and that could still break or produce unexpected behavior in the game. For each one, explain why it's a risk."

**Prompt used to generate the test suite:**

> "Now generate a suite of pytest cases for those three edge cases that verify the game handles each input gracefully (no crashes, defined outcome). Add them to tests/test_game_logic.py under a comment block labeled '# Challenge 1: Advanced Edge-Case Testing'."

| Edge Case | AI-Suggested Test | Did It Pass? | Why this edge case was chosen |
|-----------|-------------------|--------------|-------------------------------|
| **Negative number** (`"-5"`) | `parse_guess("-5")` returns `(True, -5, None)`; `check_guess(-5, 50)` returns `("Too Low", …"HIGHER"…)` | Yes | Negative integers are valid Python ints, so the parser accepts them even though the game range starts at 1 — could let a player input an impossible guess without feedback. |
| **Extremely large number** (`"9999999"`) | `parse_guess("9999999")` returns `(True, 9999999, None)`; `check_guess(9999999, 50)` returns `("Too High", …"LOWER"…)` | Yes | A number far outside any difficulty range (max 100) tests whether the comparison logic stays stable instead of overflowing or mis-routing the hint. |
| **No-leading-digit decimal** (`".5"`) | `parse_guess(".5")` returns `(True, 0, None)`; `check_guess(0, 50)` returns `("Too Low", …)` | Yes | `".5"` contains `"."` so it hits the float branch: `int(float(".5"))` = 0. Zero is outside the valid game range (1–N), yet the parser silently accepts it — a subtle boundary the basic tests missed. |

---

## Linting & Style (SF9)

> Document your use of AI for linting or code style improvements.

**Prompt used:**

```
<!-- Paste the prompt you gave the AI -->
```

**Linting output before:**

```
<!-- Paste relevant linter warnings/errors -->
```

**Changes applied:**

<!-- Describe what you changed based on the AI's suggestions -->

---

## Model Comparison (SF11)

> Compare two AI models on the same task.

**Task given to both models:**

<!-- Describe what you asked each model to do -->

| | Model A | Model B |
|-|---------|---------|
| **Model name** | | |
| **Response summary** | | |
| **More Pythonic?** | | |
| **Clearer explanation?** | | |

**Which did you prefer and why?**

<!-- Your conclusion -->
