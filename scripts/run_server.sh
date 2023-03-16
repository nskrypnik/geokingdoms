#!/bin/bash

# This is for production and should receive GEOAPP_DB_CONNECTION
# from the environment variables

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
PARENT_DIR="$(dirname "$SCRIPT_DIR")"
export PYTHONPATH="${PYTHONPATH}:${PARENT_DIR}/geoapp"

uvicorn main:app --reload
