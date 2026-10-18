#!/bin/bash

# DevOps Lab - Filesystem Explorer

echo "=================================="
echo "      FILESYSTEM EXPLORER"
echo "=================================="
echo

echo "Current directory:"
pwd

echo
echo "Directory contents:"
ls -lah

echo
echo "File count:"
find . -maxdepth 1 -type f | wc -l

echo
echo "Directory count:"
find . -mindepth 1 -maxdepth 1 -type d | wc -l
