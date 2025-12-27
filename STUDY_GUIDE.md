# Study Guide — Mini Python Notes CLI

This study guide walks through the exact steps we performed to create a tiny Python CLI notes app and test it. Use this to practice the VS Code + Python workflow.

Project files created
- `project/README.md` — brief quickstart
- `project/STUDY_GUIDE.md` — this study guide
- `project/src/note_app.py` — main NotesManager CLI
- `project/tests/test_note_app.py` — unit tests
- `project/.gitignore` — ignores `__pycache__`, `.venv`, `notes.json`

Step-by-step actions we did

1. Created a project scaffold
   - Added `src/` package, `tests/` folder, and project metadata files.

2. Implemented the notes CLI in `src/note_app.py`
   - `NotesManager` handles loading/saving `notes.json`, adding, listing, removing, clearing.
   - A `main()` function provides a small argparse-based CLI: `add`, `list`, `remove`, `clear`, and `--file` option.

3. Wrote unit tests in `tests/test_note_app.py`
   - Tests cover add/list, remove, and persistence between manager instances.

4. Configured Python environment (local venv) and ran tests
   - Created a venv and used the workspace Python environment configured by VS Code tools.
   - Ran tests with:

```powershell
cd /project
python -m unittest discover -v -s tests
```

5. Verified tests all pass (3 tests OK).

Commands to run and try

- Create and activate a venv (PowerShell):

```powershell
cd /project
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

- Run the CLI help

```powershell
python -m src.note_app --help
```

- Add a note

```powershell
python -m src.note_app add "Buy milk"
```

- List notes

```powershell
python -m src.note_app list
```

- Remove a note (0-based index)

```powershell
python -m src.note_app remove 0
```

- Run tests

```powershell
python -m unittest discover -v -s tests
```

Suggested next exercises (pick one)
- Add searching/filtering by substring.
- Add tags and filter by tag.
- Add timestamps and sort by date.
- Build a Tiny GUI with `tkinter` or a web UI with `Flask`.
- Initialize a Git repo and make incremental commits for each change.

Git quickstart (optional)

```powershell
cd /project
git init
git add .
git commit -m "Initial mini notes CLI scaffold"
```

Notes and tips
- Use the VS Code Source Control view to stage/commit changes.
- Use the Run/Debug panel to run `python -m src.note_app` with args for iterative debugging.
- Ask Copilot to suggest refactors, tests, or new features — treat it as a pair programmer.

If you want, I can now:
- Add a VS Code `launch.json` and task to run tests from the editor
- Initialize a Git repo and make the first commit
- Implement one of the suggested feature exercises

Tell me which of those you'd like next.
