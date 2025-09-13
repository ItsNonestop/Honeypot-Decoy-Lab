#!/usr/bin/env bash
python3 -m venv .venv
. .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements-dev.txt
[ -f requirements.txt ] && pip install -r requirements.txt
pip install -e .
