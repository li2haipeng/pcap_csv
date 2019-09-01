import csv
import sys
import argparse
from pathlib import Path
import pandas as pd
import selfUtils as su


def filter_ack(p_list):
    echo_packets = []
    for p in p_list:
        # if p[4] == 6.0 and p[2] < 60: #filter ACk packets
        if p[1] < 60:
            continue
        else:
            echo_packets.append(p)
    return echo_packets


def max_interval(packets):
    _max = 0
    _i = 0
    _m = 0
    for i,p in enumerate(packets):
        if i == len(packets) - 1:
            continue
        if abs(packets[i + 1][0] - p[0]) > _max:
            _max = abs(packets[i + 1][0] - p[0])
            # _i = i
    return (_max)


def min_interval(packets):
    _min = 1000
    for i,p in enumerate(packets):
        if i == len(packets) - 1:
            continue
        if abs(packets[i + 1][0] - p[0]) < _min:
            _min = abs(packets[i + 1][0] - p[0])
            _i = i
    return (_min)


def ave_interval(packets):
    total = 0
    l = len(packets)
    for i,p in enumerate(packets):
        if i == len(packets) - 1:
            continue
        total = packets[i+1][0] - p[0] + total

    ave = total/l

    return ave


def max_outgoing(packets):
    _max = 0
    for i, p in enumerate(packets):
        if i == len(packets) - 1:
            continue
        if abs(packets[i + 1][0] - p[0]) > _max:
            _max = abs(packets[i + 1][0] - p[0])
            # _i = i
    return (_max)


def half_duplex(p_list, trace_name):
    outgoing = []
    incoming = []
    # duplex_csv = pd.Dataframe(columns=['trace_name', 'max_interval'])
    for p in p_list:
        if p[2] == -1:
            incoming.append(p)
        else:
            outgoing.append(p)

    total_outgoing = 0
    total_incoming = 0
    for p in outgoing:
        total_outgoing = p[1] + total_outgoing
    for p in incoming:
        total_incoming = p[1] + total_incoming

    out_num = int(total_outgoing/1500)
    out_remainder = total_outgoing%1500
    in_num = int(total_incoming/1500)
    in_remainder = total_incoming%1500

    ################# Distribution stats###################
    ave = ave_interval(outgoing)
    (_min) = min_interval(outgoing)
    original_incoming = len(incoming)
    (M) = max_interval(outgoing)
    original_outgoing = len(outgoing)


    with open('stats/stats.csv','a') as stat_in:
        writer = csv.writer(stat_in)
        writer.writerow([trace_name, original_outgoing, original_incoming, out_num, out_remainder, in_num, in_remainder, M, _min, ave])
    ###################Distribution Stats#####################################

    duplex_list = outgoing + incoming
    return duplex_list


def main(opts):
    # csv_path = "/home/lhp/PycharmProjects/pcap_csv/csv/Announce_Happy_Valentines_Day_1__0218.csv"
    # half_duplex_path = "/home/lhp/PycharmProjects/pcap_csv/half_duplex/"
    csv_path = opts.csvPath
    half_duplex_path = opts.duplexPath
    pf = Path(csv_path)
    trace_name = pf.name[0:-3]

    packet_list = su.csv_numpy(csv_path)

    duplex_list = half_duplex(packet_list, trace_name)

    duplex_df = pd.DataFrame(duplex_list, columns=['time', 'size', 'direction'])
    duplex_df.to_csv(half_duplex_path + trace_name + "_HD.csv", index= False)
    print("Half_duplex of " + trace_name + " is finished")


def parseOpts(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument('-pc','--csvPath', help='path to read csv files')
    parser.add_argument('-pd', '--duplexPath',help='path to write half duplex files')
    opts = parser.parse_args()
    return opts


if __name__ == "__main__":
    opts = parseOpts(sys.argv)
    main(opts)
    # main()