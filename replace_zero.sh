#!/usr/bin/env bash

for f in csv/*.csv; do
  python3 correct_csv.py "$f"
done