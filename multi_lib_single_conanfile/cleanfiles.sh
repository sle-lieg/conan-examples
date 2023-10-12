#!/bin/bash
TEMPORARY_FILE="\
    generators/ \
    cmake-build-release/ \
    graph_info.json \
    conaninfo.txt \
    conanbuildinfo.txt \
    conan.lock \
    CMakeUserPresets.json \
    test_package/build \
    build"

echo "Deleting $TEMPORARY_FILE"
rm -rf $TEMPORARY_FILE
