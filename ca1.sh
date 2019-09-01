#!/bin/bash
# Edit to switch IP address and correct pcap path
#
#

for i in {21..25}
do
  for f in /home/lhp/PycharmProjects/pcap_csv/raw_pcap/amazon_echo/a/$i/*.pcap
  do
    python3 autocollection_pcap2csv.py "$f" 10.63.1.88 '2nd/5'
  done
done

for i in {26..30}
do
  for f in /home/lhp/PycharmProjects/pcap_csv/raw_pcap/amazon_echo/a/$i/*.pcap
  do
    python3 autocollection_pcap2csv.py "$f" 10.63.1.88 '2nd/6'
  done
done

for i in {31..35}
do
  for f in /home/lhp/PycharmProjects/pcap_csv/raw_pcap/amazon_echo/a/$i/*.pcap
  do
    python3 autocollection_pcap2csv.py "$f" 10.63.1.88 '2nd/7'
  done
done

for i in {36..40}
do
  for f in /home/lhp/PycharmProjects/pcap_csv/raw_pcap/amazon_echo/a/$i/*.pcap
  do
    python3 autocollection_pcap2csv.py "$f" 10.63.1.88 '2nd/8'
  done
done
#
#
#
#
#for i in {21..25}
#do
#  python3 autocollection_pcap2csv.py "$i" 10.63.1.144 '3nd/5' 'b/'
#done
#
#for i in {26..30}
#do
#  python3 autocollection_pcap2csv.py "$i" 10.63.1.144 '3nd/6' 'b/'
#done
#
#for i in {31..35}
#do
#  python3 autocollection_pcap2csv.py "$i" 10.63.1.144 '3nd/7' 'b/'
#done

#for i in {36..40}
#do
#  python3 autocollection_pcap2csv.py "$i" 10.63.1.144 '3nd/8' 'b/'
#done





#

