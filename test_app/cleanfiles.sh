#!/bin/bash
TEMPORARY_FILE="\
    CMakeUserPresets.json \
    build"

echo "Deleting $TEMPORARY_FILE"
rm -rf $TEMPORARY_FILE
