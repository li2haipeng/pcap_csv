#!/usr/bin/env python3
"""
@Author: Sean Kennedy (seankennedy@ieee.org)

"""

import ipaddress
import sys
from pathlib import Path

import pandas as pd
from scapy.all import *



def pcap_converter(pcap_path, echo_ip, burst_ranges):
    """
    Take the pcap files, convert to a list, break list into trace files based of number of queries,
    save sublists to csv files after extracting relevant packet information.
    :param pcap_path:
    :param echo_ip: IPv4 address of the Amazon Echo
    :param burst_ranges: list of tuples in the form (f_p, l_p) where f_p is the first packet in the burst and l_p is the
                         last
    :return: nothing. saves pandas dataframes in csv format
    """
    csv_path = 'csv/'
    pf = Path(pcap_path)
    trace_name = pf.name[0:-5]
    packets = rdpcap(pcap_path)
    num_packets = len(burst_ranges)
    for i in range(0, num_packets):
        p_list = packets[burst_ranges[i][0]:burst_ranges[i][1]]
        init_time = p_list[0].time
        # print(init_time)
        echo_df = pd.DataFrame(columns=['time', 'size', 'direction'])
        p_list.reverse()
        echo_packets = []
        for p in p_list:
            try:
                p[IP].src
            except:
                continue
            if p[IP].src.strip() == echo_ip.strip() or p[IP].dst.strip() == echo_ip.strip():
                echo_packets.append(p)
        p_list = echo_packets

        for p in p_list:
            # 1 if echo is src, -1 if destination
            if p[IP].src == echo_ip:
                p[IP].src = 1
            elif p[IP].dst == echo_ip:
                p[IP].src = -1
            else:
                p[IP].src = 0
            # Update the df with correct index
            echo_df.loc[-1] = [p.time - init_time, p.len, p[IP].src]
            echo_df.index = echo_df.index + 1

        # Sort, so list starts in non-reverse order, save to csv
        echo_df = echo_df.sort_index()
        echo_df.to_csv(csv_path + trace_name + "_" + str(i + 1) + ".csv")


def burst_detector_short(packet_path, echo_ip):
    """
    Detect Burst Patterns in pcap files, getting rid of need to manually enter first and last packet indices associated
    with queries
    Short version: For shorter packet burst detection
    :return:
    """
    start_burst_ranges = []
    end_burst_ranges = []
    interval = 1 # Amount of time between packets that constitutes a burst
    packets = rdpcap(packet_path)  # Read packet file
    c = 0  # Counter that stores number of packets in burst
    burst_in_progress = False
    echo_packets = []

    # only echo packets
    for p in packets:
        try:
            p[IP].src
        except:
            continue
        if p[IP].src.strip() == echo_ip.strip() or p[IP].dst.strip() == echo_ip.strip():
            echo_packets.append(p)

    packets = echo_packets

    for i, p in enumerate(packets):
        if i == 0:  # fist
            continue
        if i == len(packets) - 1:  # last
            continue
        prev_packet = packets[i - 1]
        next_packet = packets[i + 1]

        if (abs(p.time - prev_packet.time) > interval) and (abs(next_packet.time - p.time) > interval):
            # Not an echo packet
            c = 0
            continue

        if (abs(p.time - prev_packet.time) < interval) and (abs(next_packet.time - p.time) < interval):
            # Echo packet
            c += 1
            continue

        if (abs(p.time - prev_packet.time) > interval) and (abs(next_packet.time - p.time) < interval):
            # Start of new trace
            c = 0
            c += 1
            burst_in_progress = True
            start_burst_ranges.append(i + 1)

        if ((abs(p.time - prev_packet.time) < interval) and (abs(next_packet.time - p.time) > interval)
                and burst_in_progress == True):
            # End of the current trace
            c += 1
            end_burst_ranges.append((i + 1, c))

    # Make sure indices line up for start and end ranges
    if len(start_burst_ranges) != len(end_burst_ranges):
        end_burst_ranges.append((i + 1, c))

    # The maximum burst size in the pcap file
    max_c = max(end_burst_ranges, key=lambda x: x[1])[1]

    # Ensure lists are same size
    assert (len(start_burst_ranges) == len(end_burst_ranges)), "Start Ranges and End Ranges have different lengths"

    # Store the ranges of packet numbers for the bursts
    burst_ranges = []

    for idx, p in enumerate(end_burst_ranges):
        if p[1] > max_c - 200:
            burst_ranges.append((start_burst_ranges[idx], end_burst_ranges[idx][0]))

    return burst_ranges


def main(argv):
    if argv[0] == '--help' or argv[0] == '--h':
        print("This program takes a pcap file containing network traffic, and converts it to CSV files containing"
              " the traffic bursts.  The first argument is the pcap file path, and the second argument is the IPv4 "
              "address of the device.")
        sys.exit(0)
    if len(argv) != 2:
        raise IOError("Incorrect number of arguments, run 'python pcap_2_csv.py --help' for correct usage")
    else:
        pcap_path = argv[0]
        echo_ip = argv[1]
        try:
            ipaddress.ip_address(echo_ip)
        except ValueError:
            print("ValueError: You did not enter a valid IPv4 address")

        pf = Path(pcap_path)
        if not pf.is_file():
            raise FileNotFoundError("No file exists at specified path" + pcap_path)
        print('pcap file ' + pf.name + ' loaded.')
        print('Running burst detection...')

        ranges = burst_detector_short(pcap_path, echo_ip)
        print('Burst detection finished.')
        print('There are {} bursts with packet number ranges of {}'.format(len(ranges), ranges))
        print('Using ranges to convert pcap files to CSV trace files...')


        # ranges = [(9, 3229), (3324, 6525), (6554, 10117),(10140,13499),(13526,16935)]
        pcap_converter(pcap_path, echo_ip, ranges)
        print('CSV files generated.  Saved to csv/ directory.')


if __name__ == "__main__":
    path = '/home/lhp/PycharmProjects/pcap_csv/raw_pcap/amazon_echo/surprise_me_5_L.pcap'
    # path = '/home/lhp/PycharmProjects/pcap_csv/raw_pcap/amazon_echo/Announce_Happy_Valentines_Day_0_.pcap'
    # # path = 'sports_update_5_30s'
    ip = '10.63.1.105'
    # # # # Ranges for how_many_days_untill_christmas
    # # # first = [4, 598, 1087, 1563, 2071]
    # # # last = [581, 1082, 1557, 2066, 2592]
    # # # Ranges for  sports_update_5_30s
    # # first = [12, 2719, 5249, 7873, 10377]
    # # last = [2712, 5245, 7806, 10369, 12902]
    # # pcap_converter(path, ip, first, last)
    r = burst_detector_short(path,ip)
    ranges = [(11, 973), (1005, 2115), (2156, 3204), (3243, 5122), (5137, 6376)]
    # pcap_converter(path, ip, ranges)
    # print(r[1][0])
    # # print(len(s), len(e))
    # # for packet in e:
    # #     if packet[1] > 300:
    # #         print(packet[1])
    # print(r)

    # main(sys.argv[1:])


