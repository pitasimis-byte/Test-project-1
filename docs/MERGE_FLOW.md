# Merge workflow (MERGE_FLOW)

This diagram shows the typical branch → PR → merge flow used in this project.

```mermaid
flowchart LR
  A[Local: main] --> B(Create feature branch)
  B --> C(Work and commit locally)
  C --> D(Push feature branch to origin)
  D --> E(Open Pull Request)
  E --> F[CI runs on PR (tests)]
  F --> G[Review & Approve]
  G --> H(Merge PR into main)
  H --> I[CI runs on main (tests)]
  I --> J(Deploy / Release or Sync local main)
  J --> K(Delete feature branch)

  click D "https://docs.github.com/en/get-started/using-git/pushing-commits-to-a-remote-repository" "Push branch docs"
  click E "https://docs.github.com/en/pull-requests" "Open a PR"
  click G "https://docs.github.com/en/code-review/" "Code review"

  style F fill:#f9f,stroke:#333,stroke-width:1px
  style I fill:#efe,stroke:#333,stroke-width:1px
```

> Note: The CI steps correspond to the GitHub Actions workflow in `.github/workflows/python-tests.yml` that runs unit tests on PR and on merge to `main`.
