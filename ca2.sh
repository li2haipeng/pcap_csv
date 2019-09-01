#!/bin/bash
# Edit to switch IP address and correct pcap path
#
#


for i in {41..45}
do
  for f in /home/lhp/PycharmProjects/pcap_csv/raw_pcap/amazon_echo/a/$i/*.pcap
  do
    python3 autocollection_pcap2csv.py "$f" 10.63.1.88 '2nd/9'
  done
done

for i in {46..50}
do
  for f in /home/lhp/PycharmProjects/pcap_csv/raw_pcap/amazon_echo/a/$i/*.pcap
  do
    python3 autocollection_pcap2csv.py "$f" 10.63.1.88 '2nd/10'
  done
done

for i in {51..55}
do
  for f in /home/lhp/PycharmProjects/pcap_csv/raw_pcap/amazon_echo/a/$i/*.pcap
  do
    python3 autocollection_pcap2csv.py "$f" 10.63.1.88 '2nd/11'
  done
done

for i in {56..60}
do
  for f in /home/lhp/PycharmProjects/pcap_csv/raw_pcap/amazon_echo/a/$i/*.pcap
  do
    python3 autocollection_pcap2csv.py "$f" 10.63.1.88 '2nd/12'
  done
done
#
#
#
#for i in {41..45}
#do
#  python3 autocollection_pcap2csv.py "$i" 10.63.1.144 '3nd/9' 'b/'
#done
#
#for i in {46..50}
#do
#  python3 autocollection_pcap2csv.py "$i" 10.63.1.144 '3nd/10' 'b/'
#done
#
#for i in {51..55}
#do
#  python3 autocollection_pcap2csv.py "$i" 10.63.1.144 '3nd/11' 'b/'
#done

#for i in {56..60}
#do
#  python3 autocollection_pcap2csv.py "$i" 10.63.1.144 '3nd/12' 'b/'
#done





#

