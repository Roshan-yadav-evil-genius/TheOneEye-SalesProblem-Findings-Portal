Your goal is to **search the web for AI/ML advancements in sales** (the sales field broadly: processes, tools, and go-to-market execution) that are **from 2025 onward**—i.e. **after the start of 2025**, with **no upper year limit** (include 2026, 2027, and later as they appear). Record **concrete applications or systems** with **practical business impact** (e.g., lead generation, conversion, CRM, outreach, sales productivity).

**Constraints:**

* Focus only on practical sales impact—not generic AI descriptions. Each entry must be a **specific** application or system tied to a **specific** sales challenge.
* Prefer **credible** sources (vendor docs, analyst reports, reputable press, academic/industry summaries). Where possible, favor material that clearly reflects **post‑2025** releases, forecasts, or evidence (stated dates, product/version timelines, report publication dates).

---

### Workflow

1. **Load `innovations.jsonl`** if it exists. If it does not exist yet, create it on first append.
2. **Research on the internet** for AI/ML innovations in sales (SDR workflows, lead gen, CRM, pipeline, outreach, forecasting, productivity, etc.).
3. **Before appending**, check whether a **similar innovation** already exists in `innovations.jsonl` (same product/system and same challenge). If it does, do not duplicate.

---

### Duplicate Handling

If a similar innovation already exists:

* **Do NOT add it to `innovations.jsonl`.**
* **Continue exploring related but different areas** such as:

  * A different tool, model, or deployment pattern
  * An adjacent step in the sales workflow
  * A different buyer stage or use case
  * Another credible source describing a distinct improvement

Continue researching until you find a **distinct new improvement**.

---

### When a New Improvement Is Found

Append one JSON object per line to **`innovations.jsonl`** (JSONL only—**not** a JSON array).

**Output rules for the dataset lines:**

* Each line must be a single valid JSON object with exactly these fields: `challenge_addressed`, `ai_ml_solution`, `pros`, `cons`, `source_link`.
* **`source_link`**: one credible URL string for that entry.
* For **`pros` and `cons`**: use the batch rule below. For entries where pros/cons do not apply, set both to JSON `null` (not empty strings).

**Pros/cons batch rule:** In each append operation (one session’s batch of new lines), only the **third** JSON object in **that batch** must include non-null `pros` and `cons` (each a concise factual string). All other lines in the same batch must have `"pros": null, "cons": null`. If the batch has fewer than three lines, **all** lines in that batch must have `pros` and `cons` set to `null`.

**Example shape** (illustrative—use real research and URLs):

```json
{"challenge_addressed": "Specific sales challenge", "ai_ml_solution": "How AI/ML solves it (concrete system or application)", "pros": null, "cons": null, "source_link": "https://example.com/credible-article"}
```

When producing the **lines to append** to `innovations.jsonl`, **do not include explanations outside those JSONL lines** (no markdown, no preamble or commentary mixed into the file content).

---

### Memory

Use **`memory/innovations/`** only (not `memory/problems/`). Record thoughts, notes, and research progress there so future runs can continue from past work.
Runtime memory resets after execution, so it is mandatory to keep track of your progress by organizing and updating files under **`memory/innovations/`** in whatever way helps you recall and move forward effectively.

---

### Committing Progress

After each research session, **commit your changes using git** so progress is preserved for future runs.

* Stage and commit **`innovations.jsonl`**, **`memory/innovations/`**, and any other modified files (including this doc if edited).
* Write a clear, descriptive commit message summarizing what was added or changed.
* **Do NOT push** unless explicitly asked — just commit locally.
* This ensures that even if runtime memory resets, the git history serves as a reliable record of all research progress.

---

### Objective

Continuously build a **dataset of unique, validated AI/ML sales innovations** (**post‑2025**, ongoing) with **clear challenges, solutions, and sources**, suitable for downstream product or research use.
