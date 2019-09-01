#!/bin/bash
# Replace file extensions with pcap

for f in raw_pcap/amazon_echo/*.pcapng;
    do mv $f `basename $f .pcapng`.pcap;
done;