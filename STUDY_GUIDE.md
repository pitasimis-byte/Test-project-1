git add .
# Study Guide — Mini Python Notes CLI

This study guide walks through the exact steps we performed to create a tiny Python CLI notes app and test it. Use this to practice the VS Code + Python workflow.

Files and purpose
- `README.md` — quickstart and high-level overview
- `STUDY_GUIDE.md` — this detailed walkthrough
- `src/note_app.py` — the NotesManager CLI implementation
- `tests/test_note_app.py` — unit tests for core logic

High-level steps we followed

1) Scaffold the project
- Created `src/`, `tests/`, `.vscode/`, and top-level files (`README.md`, `STUDY_GUIDE.md`, `requirements.txt`).

2) Implement core functionality
- `NotesManager` in `src/note_app.py` handles loading/saving a JSON file, and provides `add`, `list`, `remove`, and `clear` operations.

3) Add tests
- Unit tests in `tests/test_note_app.py` verify basic behaviour and persistence.

4) Configure the editor and run tests
- Added VS Code `launch.json` and `tasks.json` to run/debug the app and run unit tests from the editor.

5) Initialize Git and commit
- A local git repo was initialized and an initial commit created; local git identity was configured for this repo.

Commands we used (PowerShell)

```powershell
cd C:\project
# create venv
python -m venv .venv
# activate venv
.\.venv\Scripts\Activate.ps1
# run tests
python -m unittest discover -v -s tests
# run the app (module)
python -m src.note_app --help
```

How to iterate safely
- Edit `src/note_app.py` and add tests in `tests/` before changing behaviour.
- Run `python -m unittest discover -v -s tests` after changes.
- Use small commits with clear messages:

```powershell
git add src/note_app.py tests/test_note_app.py
git commit -m "Add remove-by-index and tests"
```

Suggested next exercises (pick one)
- Add search/filter by substring and tests
- Add tags to notes and filter by tag
- Add created timestamps to notes and sort/display them
- Build a tiny `tkinter` GUI to add/list notes

If you want, I can implement one exercise now, update tests, and walk you through staging/committing the changes in VS Code.
