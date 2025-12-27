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
python -m unittest discover -v
```

Next steps:
- Try editing `src/note_app.py` to add tags or search.
- Commit to git and open the VS Code Source Control view.
- Ask Copilot to help add features or refactor.
