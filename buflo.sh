#!/bin/bash
# apply BuFLO on original data
# input: path, size(d), frequency(f), time(T)

for f in csv/*.csv; do
  python3 buflo_v2.py "$f" 1500 50 10
done