# Playwright Python Bootcamp Framework

A small test automation framework with a UI layer and an API layer. Built with Python, pytest, and Playwright. You will extend it with your own tests during the bootcamp.

The application under test is [Automation Exercise](https://automationexercise.com), a free e-commerce practice site made for testers. It has a web UI and a public REST API.

- UI: https://automationexercise.com
- API list and examples: https://automationexercise.com/api_list
- Suggested test cases: https://automationexercise.com/test_cases

The site needs no shared login. Tests create their own user through the API and delete it afterward.

## Setup

You need Python 3.10 or newer and Git.

```bash
git clone <your-repo-url>
cd playwright-python-bootcamp

python -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
pip install -r requirements.txt
playwright install chromium
```

Check your setup:

```bash
pytest -m smoke --headed
```

## Run tests

| Goal | Command |
| --- | --- |
| All tests | `pytest` |
| API tests only | `pytest -m api` |
| UI tests only | `pytest -m ui` |
| Smoke tests | `pytest -m smoke` |
| One numbered test case | `pytest -k tc06` |
| One file | `pytest tests/ui/test_login.py` |
| One test | `pytest -k test_wrong_password_shows_error` |
| Watch the browser | `pytest --headed --slowmo 500` |
| Another browser | `pytest --browser firefox` |
| Debug with inspector | `PWDEBUG=1 pytest -k <test name>` |

Reports and failure evidence:

- HTML report: `reports/report.html`
- Screenshots and traces for failed tests: `test-results/`
- Open a trace: `playwright show-trace test-results/<test folder>/trace.zip`

## Project layout

```
.github/workflows/tests.yml   CI: lint, API tests, UI tests, report on GitHub Pages
src/autoexercise/
  config.py                   URLs, overridable with env vars
  data.py                     Builds unique test users
  api/                        API client layer (one class per resource group)
  pages/                      Page objects (one class per page)
tests/
  conftest.py                 Fixtures shared by all tests
  ui/                         Browser tests and UI fixtures
  ui/test_cases/              The 26 numbered test cases from the site (tc01 to tc26)
  api/                        HTTP tests
  api/test_cases/             API versions of the test cases that have an endpoint
  exercises/                  Your exercises, skipped until you finish them
docs/                         Guides
```

Read [docs/FRAMEWORK_GUIDE.md](docs/FRAMEWORK_GUIDE.md) to see how the layers fit together.

## Add a test

1. Pick a layer. Browser behavior goes in `tests/ui/`. Service behavior goes in `tests/api/`.
2. Reuse a page object or client. If none fits, add one under `src/autoexercise/`.
3. Name the file `test_<feature>.py` and the function `test_<behavior>`.
4. Add a marker (`ui`, `api`, `smoke`, `regression`).
5. Run it locally. Then push and check the Actions tab.

Rules for every test:

- One behavior per test.
- Tests do not depend on each other. Use the `new_user` fixture for a fresh account.
- No `time.sleep`. Use `expect(...)` assertions, which wait for you.
- No locators or URLs inside test functions. Put them in page objects and clients.

## Two things to know about this site

1. The API reports its result in the JSON body (`responseCode`), not reliably in the HTTP status. Use the `code(response)` helper in assertions.
2. The site shows ads that can cover buttons. The UI fixtures in `tests/ui/conftest.py` block them. Keep using the `page` fixture and you get this for free.

## The 26 test cases

The site lists 26 test cases at https://automationexercise.com/test_cases. Each one is implemented here and named with its number, for example `test_tc14_place_order_register_while_checkout`. Step numbers appear as comments in the code.

```bash
pytest -k tc14               # one test case by number
pytest -m testcases          # all of them
pytest -m "testcases and api"
```

See [docs/TEST_CASES.md](docs/TEST_CASES.md) for the full table and which test cases have an API version.

## Exercises

Five starter exercises live in `tests/exercises/`. Each file explains the task. Finish one by replacing the `pytest.skip(...)` line with your test. When it passes, delete `pytest.mark.exercise` from `pytestmark` so CI runs it too.

## Continuous integration

Every push and pull request runs GitHub Actions:

1. Lint with ruff. Fix issues with `ruff check . --fix`.
2. API tests.
3. UI tests in Chromium.
4. On `main` only: the reports publish to GitHub Pages.

To turn on the Pages report, open your repository, go to Settings, then Pages, and set Source to "GitHub Actions". The report link appears in the `publish-report` job after the next push to `main`.

Open any run in the Actions tab. Download the report and traces from the Artifacts section at the bottom of the run page. See [docs/GIT_WORKFLOW.md](docs/GIT_WORKFLOW.md) for the branch and pull request routine.

## Help

See [docs/TROUBLESHOOTING.md](docs/TROUBLESHOOTING.md).
