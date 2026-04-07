Your goal is to **discover real problems in sales** that could become opportunities for **automation tools or startups**.

---

### Workflow

1. **Load `problems.jsonl`** if it exists.
2. **Research sales-related problems on the internet** (SDR workflows, lead generation, CRM usage, pipeline management, outreach, forecasting, etc.).
3. **Before adding a problem**, check whether a **similar problem already exists** in `problems.jsonl`.

---

### Duplicate Handling

If a similar problem already exists:

* **Do NOT add it to `problems.jsonl`.**
* **Continue exploring related but different areas** such as:

  * Adjacent sales workflow problems
  * Upstream causes of the same friction
  * Downstream consequences of the problem
  * Other unexplored sales inefficiencies

Continue researching until you find a **distinct new problem**.

---

### When a New Problem is Found

Append a new line to **`problems.jsonl`** in this format:

```json
{"problem_title": "Problem Title", "problem_description": "Problem Description", "why_it_matters": "Why it Matters", "example_evidence": "Example Evidence", "proposed_slug": "Proposed Slug", "references": ["https://source-url-1", "https://source-url-2"]}
```

Each **line must represent one unique problem**.

---

### Memory

Use **`memory/problems/`** only (not `memory/innovations/`). Record thoughts, notes, and research progress there so future runs can continue from past work.
Runtime memory resets after execution, so it is mandatory to keep track of your progress by organizing and updating files under **`memory/problems/`** in whatever way helps you recall and move forward effectively.


---

### Committing Progress

After each research session, **commit your changes using git** so progress is preserved for future runs.

* Stage and commit **`problems.jsonl`**, **`memory/problems/`**, and any other modified files.
* Write a clear, descriptive commit message summarizing what was added or changed.
* **Do NOT push** unless explicitly asked — just commit locally.
* This ensures that even if runtime memory resets, the git history serves as a reliable record of all research progress.

---

### Objective

Continuously build a **dataset of unique, validated sales problems** that could lead to **automation tools or startup opportunities**.
