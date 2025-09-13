#!/usr/bin/env bash
. .venv/bin/activate
ruff check .
pytest -q
