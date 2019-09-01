#!/bin/bash
# Edit to switch IP address and correct pcap path
#

for i in {1..5}
do
  for f in /home/lhp/PycharmProjects/pcap_csv/raw_pcap/amazon_echo/a/$i/*.pcap
  do
    python3 autocollection_pcap2csv.py "$f" 10.63.1.88 '2nd/1'
  done
done

for i in {6..10}
do
  for f in /home/lhp/PycharmProjects/pcap_csv/raw_pcap/amazon_echo/a/$i/*.pcap
  do
    python3 autocollection_pcap2csv.py "$f" 10.63.1.88 '2nd/2'
  done
done

for i in {11..15}
do
  for f in /home/lhp/PycharmProjects/pcap_csv/raw_pcap/amazon_echo/a/$i/*.pcap
  do
    python3 autocollection_pcap2csv.py "$f" 10.63.1.88 '2nd/3'
  done
done

for i in {16..20}
do
  for f in /home/lhp/PycharmProjects/pcap_csv/raw_pcap/amazon_echo/a/$i/*.pcap
  do
    python3 autocollection_pcap2csv.py "$f" 10.63.1.88 '2nd/4'
  done
done






#
#for i in {1..5}
#do
#  python3 autocollection_pcap2csv.py "$i" 10.63.1.144 '3nd/1' 'b/'
#done
#
#for i in {6..10}
#do
#  python3 autocollection_pcap2csv.py "$i" 10.63.1.144 '3nd/2' 'b/'
#done
#
#for i in {11..15}
#do
#  python3 autocollection_pcap2csv.py "$i" 10.63.1.144 '3nd/3' 'b/'
#done
#
#for i in {16..20}
#do
#  python3 autocollection_pcap2csv.py "$i" 10.63.1.144 '3nd/4' 'b/'
#done





#

