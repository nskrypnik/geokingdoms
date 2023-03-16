#!/bin/bash

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
PARENT_DIR="$(dirname "$SCRIPT_DIR")"
export PYTHONPATH="${PYTHONPATH}:${PARENT_DIR}/geoapp"

python -c "from api.utils.database import create_database; create_database()"
