python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements-dev.txt
if (Test-Path requirements.txt) { pip install -r requirements.txt }
pip install -e .
