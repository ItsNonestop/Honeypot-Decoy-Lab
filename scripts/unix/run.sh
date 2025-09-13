#!/usr/bin/env bash
. .venv/bin/activate 2>/dev/null || true
python -m honeypot 2>/dev/null || python run.py
