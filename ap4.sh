#!/usr/bin/env bash

for i in 17 18 19 20
do
    for f in csv/gamma/"$i"/*.csv; do
        python3 adapt_padding.py -pc "$f" -f "$i" -eps 0.005
    done
done
#
for i in 17 18 19 20
do
    for f in csv/gamma/"$i"/*.csv; do
        python3 adapt_padding.py -pc "$f" -f "$i" -eps 0.05
    done
done

#for i in 17 18 19 20
#do
#    for f in csv/gamma/"$i"/*.csv; do
#        python3 adapt_padding.py -pc "$f" -f "$i" -eps 0.5
#    done
#done
#
#for i in 17 18 19 20
#do
#    for f in csv/gamma/"$i"/*.csv; do
#        python3 adapt_padding.py -pc "$f" -f "$i" -eps 5.0
#    done
#done


