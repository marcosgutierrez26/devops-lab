# Testing

Unit tests for the Flask API (`app/app.py`) with pytest.

## Setup

    python3 -m venv .venv
    source .venv/bin/activate
    pip install -r app/requirements.txt -r app/requirements-dev.txt

## Run

    pytest app/ -v

## Tests (`app/test_app.py`)

| Test | Checks |
|---|---|
| `test_home_returns_ok` | `/` returns 200 and `status: ok` |
| `test_disk_returns_expected_fields` | `/disk` returns `total_gb`, `used_gb`, `usage_percent` and `level` |
| `test_clasificar_levels` | `clasificar()` returns `normal`, `WARNING` and `CRITICAL`, including the exact limits 80 and 90 |

Flask's `test_client()` sends requests to the API without starting the server.

## Verification

Changing `uso >= 80` to `uso > 80` in `clasificar()` made `test_clasificar_levels` fail
(`assert 'normal' == 'WARNING'`). After reverting the change, all 3 tests pass and pytest exits with `0`.
