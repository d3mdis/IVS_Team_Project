#! /usr/bin/bash

echo "Running mathlib_suite.py:"
cd ../../
python3 -m unittest src.tests.mathlib_suite
cd src/tests/
