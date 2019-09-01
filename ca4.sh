#!/bin/bash
# Edit to switch IP address and correct pcap path
#


#for i in {81..85}
#do
#  for f in /home/lhp/PycharmProjects/pcap_csv/raw_pcap/amazon_echo/a/$i/*.pcap
#  do
#    python3 autocollection_pcap2csv.py "$f" 10.63.1.24 '2nd/17'
#  done
#done
#
#for i in {86..90}
#do
#  for f in /home/lhp/PycharmProjects/pcap_csv/raw_pcap/amazon_echo/a/$i/*.pcap
#  do
#    python3 autocollection_pcap2csv.py "$f" 10.63.1.24 '2nd/18'
#  done
#done
#
#for i in {91..95}
#do
#  for f in /home/lhp/PycharmProjects/pcap_csv/raw_pcap/amazon_echo/a/$i/*.pcap
#  do
#    python3 autocollection_pcap2csv.py "$f" 10.63.1.24 '2nd/19'
#  done
#done

for i in 99
do
  for f in /home/lhp/PycharmProjects/pcap_csv/raw_pcap/amazon_echo/a/$i/*.pcap
  do
    python3 autocollection_pcap2csv.py "$f" 10.63.1.24 '2nd/20'
  done
done


#for i in {81..85}
#do
#  python3 autocollection_pcap2csv.py "$i" 10.63.1.144 '3nd/17' 'b/'
#done
#
#for i in {86..90}
#do
#  python3 autocollection_pcap2csv.py "$i" 10.63.1.144 '3nd/18' 'b/'
#done
#
#for i in {91..95}
#do
#  python3 autocollection_pcap2csv.py "$i" 10.63.1.144 '3nd/19' 'b/'
#done
#
#for i in {96..98}
#do
#  python3 autocollection_pcap2csv.py "$i" 10.63.1.144 '3nd/20' 'b/'
#done




#

