#!/usr/bin/env bash

for i in {5..8}
do
    python3 buffer_analysis.py 0.005 "$i"
done
#
#for i in {5..8}
#do
#    python3 buffer_analysis.py 5.0 "$i"
#done

#for i in {5..8}
#do
#    python3 buffer_analysis.py 0.5 "$i"
#done

for i in {5..8}
do
    python3 buffer_analysis.py 0.05 "$i"
done
#
