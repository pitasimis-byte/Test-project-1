# Contributing

Thanks for trying this mini project! Follow these simple steps to contribute.

- Keep changes small and focused.
- Add or update unit tests for any new behavior.
- Run tests locally with:

```powershell
python -m unittest discover -v -s tests
```

- Use clear commit messages, e.g.:

```powershell
git commit -m "Add search feature to NotesManager"
```

Suggested workflow

```powershell
# create a branch for your work
git checkout -b feature/your-feature

# make changes and run tests
python -m unittest discover -v -s tests

# stage and commit changes
git add .
git commit -m "Add feature: short description"
```

Open a pull request if you push to a remote repository. For this learning repo, you can also practice by making small commits and using the VS Code Source Control view to inspect diffs.
