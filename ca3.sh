#!/bin/bash
# Edit to switch IP address and correct pcap path
#

#for i in {61..65}
#do
#  for f in /home/lhp/PycharmProjects/pcap_csv/raw_pcap/amazon_echo/a/$i/*.pcap
#  do
#    python3 autocollection_pcap2csv.py "$f" 10.63.1.88 '2nd/13'
#  done
#done
#
#for i in {66..70}
#do
#  for f in /home/lhp/PycharmProjects/pcap_csv/raw_pcap/amazon_echo/a/$i/*.pcap
#  do
#    python3 autocollection_pcap2csv.py "$f" 10.63.1.88 '2nd/14'
#  done
#done
#
#for i in {71..73}
#do
#  for f in /home/lhp/PycharmProjects/pcap_csv/raw_pcap/amazon_echo/a/$i/*.pcap
#  do
#    python3 autocollection_pcap2csv.py "$f" 10.63.1.88 '2nd/15'
#  done
#done
#
#for i in {74..75}
#do
#  for f in /home/lhp/PycharmProjects/pcap_csv/raw_pcap/amazon_echo/a/$i/*.pcap
#  do
#    python3 autocollection_pcap2csv.py "$f" 10.63.1.24 '2nd/15'
#  done
#done
#
#for i in {76..80}
#do
#  for f in /home/lhp/PycharmProjects/pcap_csv/raw_pcap/amazon_echo/a/$i/*.pcap
#  do
#    python3 autocollection_pcap2csv.py "$f" 10.63.1.24 '2nd/16'
#  done
#done

for i in 100
do
  for f in /home/lhp/PycharmProjects/pcap_csv/raw_pcap/amazon_echo/a/$i/*.pcap
  do
    python3 autocollection_pcap2csv.py "$f" 10.63.1.24 '2nd/20'
  done
done


#for i in {61..65}
#do
#  python3 autocollection_pcap2csv.py "$i" 10.63.1.144 '3nd/13' 'b/'
#done
#
#for i in {66..70}
#do
#  python3 autocollection_pcap2csv.py "$i" 10.63.1.144 '3nd/14' 'b/'
#done
#
#for i in {71..75}
#do
#  python3 autocollection_pcap2csv.py "$i" 10.63.1.144 '3nd/15' 'b/'
#done
#
#for i in {76..80}
#do
#  python3 autocollection_pcap2csv.py "$i" 10.63.1.144 '3nd/16' 'b/'
#done





#

