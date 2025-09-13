.\.venv\Scripts\Activate.ps1
ruff check .
if (Test-Path .\.venv\Scripts\pytest.exe) { .\.venv\Scripts\pytest.exe -q } else { pytest -q }
