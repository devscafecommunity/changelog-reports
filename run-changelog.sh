#!/bin/bash
# Ativa o ambiente virtual e executa o changelog-report
cd "$(dirname "$0")"
if [ -f .venv/bin/activate ]; then
    source .venv/bin/activate
fi
python .
