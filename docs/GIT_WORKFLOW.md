# Git Workflow

Use this routine for every change.

```bash
git checkout main
git pull
git checkout -b day3/<your-name>-login-tests

# write tests, run them locally
pytest tests/ui/test_login.py
ruff check . --fix

git add -A
git commit -m "Add login negative tests"
git push -u origin day3/<your-name>-login-tests
```

Then:

1. Open the repository on GitHub. Click "Compare and pull request".
2. Wait for the checks. The `lint`, `api`, and `ui` jobs must be green.
3. If a job fails, open it, read the error, download the artifact, fix the issue, and push again. The pull request updates itself.
4. Ask for a review. Merge when approved.
5. After the merge to `main`, the report publishes to GitHub Pages (if Pages is on).

## Commit messages

Start with a verb. Say what changed. Example: `Add API test for missing search term`.

## Do not commit

- `.venv/`, `reports/`, `test-results/`, `.env`. The `.gitignore` covers them.

## Reading a failed CI run

1. Open the Actions tab and select the failed run.
2. Select the red job. Expand the failing step.
3. Find the line starting with `FAILED`. The lines above it show the assertion.
4. Download the artifact (`ui-results`, for example). Open `reports/*.html` for the report. Open traces with `playwright show-trace`.
5. Reproduce locally: `pytest -k <test name>`.
