# 👁️ TheOneEye — Sales Problems & AI Innovations Research Portal

An interactive intelligence portal and autonomous agent research framework designed to discover, track, validate, and curate **real-world B2B sales problems** and **post-2025 AI/ML sales innovations**.

---

## 📌 What is This Project?

**TheOneEye** is a dual-system intelligence portal:
1. **Interactive Web Portal (Flask + Modern Responsive UI)**: A full-featured web dashboard for browsing, filtering, reviewing, and annotating curated datasets of sales bottlenecks and AI solutions.
2. **Autonomous Research Agents**: Automated workflows (`problems_research.sh` & `innovations_research.sh`) powered by LLM agent protocols that continuously crawl the web, identify novel sales friction points or post-2025 AI/ML product breakthroughs, check for duplicates, and append verified findings to persistent JSONL datasets.

---

## ✨ Key Features

### 1. Dual Intelligence Trackers
* **Sales Problems Tracker (`/problems`)**: Curated database of validated pain points across SDR workflows, CRM hygiene, outbound prospecting, enterprise pipeline management, and forecasting. Includes evidence, impact metrics, and startup/automation opportunities.
* **AI/ML Innovations Tracker (`/innovations`)**: Curated database of modern AI/ML sales technologies (post-2025 releases, agentic workflows, MCP servers, autonomous SDRs, AI-driven CPQ, and pipeline intelligence) mapped directly to specific sales challenges.

### 2. Interactive Review & Workflow System
* **Status Tracking**: Categorize any finding as `Raw`, `To Do`, `In Review`, `Done`, or `Deleted`.
* **Custom Notes & Annotation**: Save persistent notes for every problem or innovation to capture team thoughts and follow-ups.
* **Modern UI & Theming**: Clean, responsive layout with dark mode, light mode, and system auto-detection.
* **Search & Fast Filtering**: Instant client-side search and filtering across titles, descriptions, evidence, tags, and status.

### 3. Autonomous AI Research Pipeline
* **Autonomous Agent Specifications**: Structured markdown instructions (`problems_research.md`, `innovations_research.md`) defining search heuristics, validation standards, deduplication logic, and citation requirements.
* **Persistent Research Memory**: Cross-session memory directories (`memory/problems/`, `memory/innovations/`) preventing repetitive research and ensuring continuity across agent runs.
* **Git-Backed Data Versioning**: Continuous commits of dataset expansions and research states.

---

## 📂 Project Structure

```text
TheOneEye-SalesProblem-Findings-Portal/
├── app.py                     # Flask web server & REST API endpoints
├── problems.jsonl             # Dataset of curated sales problems & opportunities
├── innovations.jsonl          # Dataset of post-2025 AI/ML sales innovations
├── user_data.json             # Persistent user annotations and status states
├── requirements.txt           # Python dependencies
│
├── problems_research.md       # Autonomous agent prompt & rules for sales problems
├── problems_research.sh       # Execution script for problems research agent
├── innovations_research.md    # Autonomous agent prompt & rules for AI innovations
├── innovations_research.sh    # Execution script for innovations research agent
│
├── memory/                    # Agent memory store for research sessions
│   ├── problems/              # Topic maps & research logs for sales problems
│   └── innovations/           # Topic maps & research logs for AI innovations
│
├── templates/                 # Jinja2 HTML templates
│   ├── base.html              # Base layout & theme scripts
│   ├── base_tracker.html      # Master tracker UI with sidebar, search & notes
│   ├── home.html              # Landing portal
│   ├── problems.html          # Problems view
│   └── innovations.html       # Innovations view
│
├── static/                    # CSS, JS, and brand assets
│   └── Logo.png               # Project branding
└── logs/                      # Execution and server logs
```

---

## 🚀 Getting Started

### Prerequisites
* Python 3.10+
* Git

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Roshan-yadav-evil-genius/TheOneEye-SalesProblem-Findings-Portal.git
   cd TheOneEye-SalesProblem-Findings-Portal
   ```

2. **Create and activate a virtual environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

---

## 🖥️ Running the Web Portal

Start the Flask application:

```bash
python app.py
```

Open your browser and navigate to:
* **Landing Page**: [http://localhost:5000/](http://localhost:5000/)
* **Sales Problems Tracker**: [http://localhost:5000/problems](http://localhost:5000/problems)
* **AI Innovations Tracker**: [http://localhost:5000/innovations](http://localhost:5000/innovations)

---

## 🤖 Running Autonomous Research Agents

To trigger autonomous research sweeps:

* **Discover new sales problems**:
  ```bash
  chmod +x problems_research.sh
  ./problems_research.sh
  ```

* **Discover new AI/ML sales innovations**:
  ```bash
  chmod +x innovations_research.sh
  ./innovations_research.sh
  ```

---

## 📡 REST API Reference

| Method | Endpoint | Description |
| :--- | :--- | :--- |
| `GET` | `/api/problems` | Returns all sales problems combined with user status and notes. |
| `GET` | `/api/innovations` | Returns all AI innovations combined with user status and notes. |
| `POST` | `/api/status` | Updates the status (`raw`, `done`, `review`, `todo`, `deleted`) for a slug. |
| `POST` | `/api/notes` | Updates the markdown/text notes for a slug. |

---

## 📄 Dataset Schemas

### `problems.jsonl`
```json
{
  "problem_title": "String",
  "problem_description": "String",
  "why_it_matters": "String",
  "example_evidence": "String",
  "proposed_slug": "String",
  "references": ["https://..."]
}
```

### `innovations.jsonl`
```json
{
  "challenge_addressed": "String",
  "ai_ml_solution": "String",
  "pros": "String or null",
  "cons": "String or null",
  "source_link": "https://..."
}
```

---

## 🛠️ Tech Stack

* **Backend**: Flask, Python 3
* **Frontend**: HTML5, Modern CSS (Custom Properties, Grid/Flexbox), Vanilla JavaScript
* **Data Layer**: JSON Lines (`.jsonl`) & JSON
* **Agents & Automation**: Autonomous LLM Agent Protocols & Persistent Memory Trees
