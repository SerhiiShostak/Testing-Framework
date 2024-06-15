# Test framework

Test framework for educational purpose. I'm practicing creating automated tests using python and pytest.

Technologies used:
- `python 3.10`
- `pytest`
- `selenium`

Created tests for:
- `Rozetka.com.ua`
- `GitHub API`
- `Database testing (SQLite 3)`

## Launch tests
Clone the project

```bash
  git clone https://github.com/SerhiiShostak/Testing-Framework
```

Go to the project directory

```bash
  cd Testing-Framework
```

Run tests
```bash
  pytest -m [mark]
```

Available marks:
- `change`: Tests that modify name of a user
- `check`: Tests that check users name
- `http`: Test that check HTTP Protocol
- `api`: Test that check GitHub API
- `database`: Test that check DataBase
- `ui`: Test that check User Interface
- `rozetka`: Tests that check Rozetka.com.ua

## Project structure
- `config`: config file
- `modules`
  - `api\clients`: folder with clients for API testing
  - `common`: folder with DataBase operations
  - `ui\page_object`: folder with page object modules
- `tests`: folder with tests

## GitHub Actions
- `Test for GitHub Actions`: workflow with choices of test mark

For now, `rozetka` tests are not available for GitHub actions, but it still can be launched via `python -m rozetka`