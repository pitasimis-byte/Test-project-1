# Usage

## Quick start

From the project root (Windows, PowerShell):

```powershell
python -m src.note_app --help
python -m src.note_app add "Buy milk"
python -m src.note_app list
```

## Commands

- `add "<note>"` — add a new note
- `list` — show current notes
- `remove <index>` — remove note by index
- `clear` — remove all notes

The CLI stores notes in `notes.json` in the project root. If you don't want this file tracked in Git, add it to `.gitignore` (already included in this repo by default).

**PR demo:** this line was added in `feature/pr-demo` to illustrate a small change for creating a pull request as a demo.
