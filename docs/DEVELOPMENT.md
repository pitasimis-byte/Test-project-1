# Development

## Setup

1. Create a virtual environment and activate it:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

2. Install dependencies (if any):

```powershell
pip install -r requirements.txt
```

## Run tests

```powershell
python -m unittest discover -v -s tests
```

## Contributing

- Create a branch for your change: `git checkout -b feature/your-feature`
- Run tests locally and add or update tests for new behavior
- Commit and push your branch, then open a pull request

Refer to `CONTRIBUTING.md` for more details.
