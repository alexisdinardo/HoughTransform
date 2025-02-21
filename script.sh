#!/bin/sh
python convert_A05.py

echo Test01: detect_circles 01
pytest Autograder_a05.py::test01

echo Test02: detect_circles 02
pytest Autograder_a05.py::test02

echo Test03: detect_circles 03
pytest Autograder_a05.py::test03

echo Test04: detect_circles 04
pytest Autograder_a05.py::test04
