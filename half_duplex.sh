#!/usr/bin/env bash

pd1=half_duplex/open_world/

for f in csv/open_world/1/*.csv ; do
    python3 half_duplex.py -pc "$f" -pd "$pd1"
done

#pd1=half_duplex/gamma/1/
#
#for f in csv/gamma/1/*.csv ; do
#    python3 half_duplex.py -pc "$f" -pd "$pd1"
#done
#
#
#pd2=half_duplex/gamma/2/
#
#for f in csv/gamma/2/*.csv ; do
#    python3 half_duplex.py -pc "$f" -pd "$pd2"
#done
#
#
#pd3=half_duplex/gamma/3/
#
#for f in csv/gamma/3/*.csv ; do
#    python3 half_duplex.py -pc "$f" -pd "$pd3"
#done
#
#
#pd4=half_duplex/gamma/4/
#
#for f in csv/gamma/4/*.csv ; do
#    python3 half_duplex.py -pc "$f" -pd "$pd4"
#done
#
#
#pd5=half_duplex/gamma/5/
#
#for f in csv/gamma/5/*.csv ; do
#    python3 half_duplex.py -pc "$f" -pd "$pd5"
#done


