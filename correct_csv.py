import csv
import numpy as np
import ipaddress
import sys
from pathlib import Path

import pandas as pd
from scapy.all import *


def corrct(packet_path):
    pf = Path(packet_path)
    csv_path = 'new_csv/'
    trace_name = pf.name[0:-4]

    reader = csv.reader(open(packet_path, "r"), delimiter=",")
    query_in_list = list(reader)
    query_in_list.pop(0)
    query_in_array = np.array(query_in_list).astype(float)
    query_in_list = query_in_array.tolist()

    for p in query_in_list:
        if p[3] == 0.0:
            p[3] = 1
        del p[0]

    echo_df2 = pd.DataFrame(query_in_list, columns=['time', 'size', 'direction'])
    echo_df2.to_csv(csv_path + trace_name + ".csv")


def main(argv):
    if argv[0] == '--help' or argv[0] == '--h':
        print("This program takes a csv file converted from pcap and applies BuFLO algorithm on the original traffic data"
              " The 1st argument is the csv file path, the 2nd argument is the target frequency of packet transmission,"
              " the 3rd argument is the time"
              " interval, the 4th argument is the minimum amount of time for the transmission")
        sys.exit(0)
    if len(argv) != 1:
        raise IOError("Incorrect number of arguments, run 'python buflo.py --help' for correct usage")
    else:
        csv_path = argv[0]
    corrct(csv_path)
    print('CSV files: ' + csv_path + ' generated. Saved to buflo/ directory.')


if __name__ == "__main__":
    # path = '/home/lhp/PycharmProjects/pcap_csv/csv/alexa_5_30s_L_1.csv'
    # corrct(path)
    main(sys.argv[1:])