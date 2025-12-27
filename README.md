# Mini Python Notes CLI

A tiny project to learn VS Code + Python + pair-programming workflow with Copilot.
What you get:
- A small `NotesManager` CLI in `src/note_app.py`.
- Unit tests in `tests/test_note_app.py`.
Quick setup (Windows, PowerShell):

1. Open the folder in VS Code.
2. Create a virtual environment and activate it:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```
3. Run the app:

```powershell
python -m src.note_app --help
python -m src.note_app add "Buy milk"
python -m src.note_app list
```
4. Run tests (no external deps):

```powershell
python -m unittest discover -v
```
Next steps:
- Try editing `src/note_app.py` to add tags or search.
- Commit to git and open the VS Code Source Control view.
- Ask Copilot to help add features or refactor.
# Mini Python Notes CLI

This small project is a learning playground to get familiar with VS Code, Python, and pair-programming with Copilot.
Project location
- Path on this machine: `C:\project`

What's included
- `src/note_app.py`: the `NotesManager` CLI module (add, list, remove, clear)
- `tests/test_note_app.py`: unit tests covering core behaviour
- `.vscode/`: editor `launch.json` and `tasks.json` for running and testing from VS Code
- `STUDY_GUIDE.md`: step-by-step study notes

Quickstart (Windows, PowerShell)

1. Open the project in VS Code:

```powershell
code C:\project
```

2. Create and activate a virtual environment (from the project root):

```powershell
cd C:\project
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

3. Run the CLI help and try commands:

```powershell
python -m src.note_app --help
python -m src.note_app add "Buy milk"
python -m src.note_app list
```

4. Run tests (no external deps):

```powershell
python -m unittest discover -v -s tests
```

Run & debug from VS Code
- Use the Run view and select `Run Notes CLI (module)` to run the module.
- Use `Run Tests (unittest)` to run tests in the debugger.
- Use the Tasks panel to run the `Run Tests` or `Run Notes CLI (list)` tasks quickly.

Git and commits
- A local git repo was initialized and an initial commit created. To make further commits:

```powershell
cd C:\project
git status
git add <files>
git commit -m "Describe changes"
```

Study guide and next exercises
- See `STUDY_GUIDE.md` for a detailed walkthrough of what we built and why.
- Suggested exercises: add search, tags, timestamps, or a small GUI with `tkinter`.

Need help?
- Tell me which exercise you want next and I can implement it, add tests, and walk through the git workflow.
# Mini Python Notes CLI

A tiny project to learn VS Code + Python + pair-programming workflow with Copilot.

What you get:
- A small `NotesManager` CLI in `src/note_app.py`.
- Unit tests in `tests/test_note_app.py`.

Quick setup (Windows, PowerShell):

1. Open the folder in VS Code.
2. Create a virtual environment and activate it:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

3. Run the app (from project root):

```powershell
python -m src.note_app --help
python -m src.note_app add "Buy milk"
python -m src.note_app list
```

4. Run tests (no external deps):

```powershell
python -m unittest discover -v -s tests
```

Next steps:
- Try editing `src/note_app.py` to add tags or search.
- Commit to git and open the VS Code Source Control view.
- Ask Copilot to help add features or refactor.
