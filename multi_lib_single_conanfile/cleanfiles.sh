#!/bin/bash
TEMPORARY_FILE="\
    build \
    CMakeUserPresets.json \
    test_package/build \
    test_package/CMakeUserPresets.json"

echo "Deleting $TEMPORARY_FILE"
rm -rf $TEMPORARY_FILE
