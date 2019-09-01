#!/usr/bin/env bash

for f in /home/lhp/PycharmProjects/pcap_csv/half_duplex/0218/*.csv; do
  python3 log_k_anonymity.py -ph "$f" -s 1500 -o 1 -i 0.5
done