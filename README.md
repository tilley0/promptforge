# 🔨 promptforge
**AI/ML Prompt Engineering & Agentic AI Development**

`promptforge` is a workspace for building **prompt libraries**, **agentic AI patterns**, and **LLM-integrated systems**. It emphasizes reproducibility, evaluation, and sane engineering practices (testing, linting, CI-friendly).

---

## 🚀 Goals
- Reusable **prompt patterns** (instruction, role-based, few-shot, eval-ready).
- **Agentic workflows**: planning, tool-use, memory, multi-agent handoffs.
- **Observability & evaluation**: runs, metrics, cost/latency, outcome scoring.
- Pluggable **providers** (OpenAI, Anthropic, or local via LiteLLM).

---

## 📂 Repository Layout
```plaintext
├── prompts/                 # Prompt templates, chains, archetypes
├── agents/                  # Agent configs, workflows, orchestration
├── data/                    # Context, small datasets, embeddings
├── experiments/             # Experiment runs, eval results, benchmarks
├── notebooks/               # Jupyter/Colab exploration
├── scripts/                 # CLI & utilities (run agents, eval, export)
│   └── run_agent.py
├── configs/                 # YAML/TOML configs for agents & eval
│   └── example_agent.yaml
├── tests/                   # Unit/integration tests (pytest)
├── docs/                    # Guides, design notes, diagrams
├── .env.example             # Env var template (copy to .env)
├── pyproject.toml           # Poetry project (deps, formatters, linters)
├── requirements.txt         # Pip alternative to Poetry
├── .gitignore
└── README.md
```

---

## 🧰 Getting Started

### 1) Clone and choose your Python workflow
```bash
git clone https://github.com/tilley0/promptforge.git
cd promptforge
# Recommended: Python 3.10–3.12
python -m venv .venv && source .venv/bin/activate  # Windows: .venv\Scripts\activate
```

**Option A: Poetry**
```bash
pip install --upgrade pip
pip install poetry
poetry install
```

**Option B: Pip**
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 2) Configure credentials
Copy the template and set your keys:
```bash
cp .env.example .env
# edit .env: set OPENAI_API_KEY or ANTHROPIC_API_KEY, pick a default model
```

Minimal `.env` example:
```
# One of these (or both)
OPENAI_API_KEY=sk-...
ANTHROPIC_API_KEY=...
# Optional defaults
PROVIDER=openai
OPENAI_MODEL=gpt-4o-mini
ANTHROPIC_MODEL=claude-3-5-sonnet-latest
```

### 3) Run a quick smoke test
```bash
python scripts/run_agent.py --config configs/example_agent.yaml --message "Say hello and list three capabilities."
```

### 4) Dev quality of life
Format, lint, type-check, and test:
```bash
# If using Poetry:
poetry run ruff check .
poetry run ruff format .
poetry run mypy .
poetry run pytest -q

# If using pip:
ruff check . && ruff format . && mypy . && pytest -q
```

---

## 📖 Documentation
- **Prompt Patterns** → `docs/prompts.md`
- **Agent Architectures** → `docs/agents.md`
- **Evaluation** → `docs/evaluation.md`

> Don’t see these yet? They’re stubs—open PRs are welcome.

---

## 🧪 Roadmap
- [ ] Baseline prompt library with eval sets
- [ ] Tool-augmented agent framework (search, RAG, function-calling)
- [ ] Repro **evaluation harness** (win-rate, rubric scoring, cost/latency)
- [ ] **Telemetry** (tokens, traces, decision logs)
- [ ] Multi-agent collaboration patterns

---

## 🤝 Contributing
1. Fork the repo  
2. Create a feature branch  
3. Include tests and update docs  
4. Open a PR with a crisp description

---

## 🔒 Security & Ethics
- Build responsibly; avoid harmful, deceptive, and noncompliant uses.
- Keep keys and datasets out of version control.
- If you handle regulated data, wire policies and data guards into your agents.

---

## 📜 License
MIT – see [LICENSE](LICENSE)
