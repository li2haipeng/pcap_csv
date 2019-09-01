from __future__ import division
import os
import selfUtils as su
import sys
import csv
import shutil
import numpy as np
import pandas as pd
import argparse
from sklearn.preprocessing import LabelBinarizer
from sklearn.feature_selection import chi2, SelectKBest
from sklearn.feature_extraction.text import CountVectorizer


class query:
    def __init__(self, f, total_time, total_num, total_bytes, burst_num,
                in_burst_num, in_burst_ratio,
                out_burst_num, out_burst_ratio,
                in_burst_bandwidth, out_burst_bandwidth,
                max_in_bandwidth, max_out_bandwidth,
                incoming_num, in_num_ratio,
                outgoing_num, out_num_ratio,
                incoming_bytes, in_bytes_ratio,
                outgoing_bytes, out_bytes_ratio):
        self.name = f
        self.total_time = total_time
        self.total_num = total_num
        self.total_bytes = total_bytes
        self. burst_num = burst_num
        self.in_burst_num = in_burst_num
        self.in_burst_ratio = in_burst_ratio
        self.out_burst_num = out_burst_num
        self.out_burst_ratio = out_burst_ratio
        self.in_burst_bandwidth = in_burst_bandwidth
        self.out_burst_bandwidth = out_burst_bandwidth

        self.max_in_bandwidth = max_in_bandwidth
        self.max_out_bandwidth = max_out_bandwidth
        self.incoming_num = incoming_num
        self.in_num_ratio = in_num_ratio
        self.outgoing_num = outgoing_num
        self.out_num_ratio = out_num_ratio
        self.incoming_bytes = incoming_bytes
        self.out_burst_ratio = out_burst_ratio
        self.in_bytes_ratio = in_bytes_ratio
        self.outgoing_bytes = outgoing_bytes

        self.out_bytes_ratio = out_bytes_ratio


def burst_analysis(f, packets):
    in_busrt_list = []
    out_burst_list = []
    size = 0
    bw = 0
    t = 0
    for i, p in enumerate(packets):
        if i == len(packets) - 1:
            continue

        size += p[1]
        if p[2] + packets[i+1][2] == 0:
            duration = abs(p[0] - t)
            if i == 0:
                continue
            if duration == 0:
                continue
            bw = size / duration
            if bw < 0:
                print()

            direction = p[2]
            burst = [size, direction, bw]
            if direction == 1:
                out_burst_list.append(burst)
            else:
                in_busrt_list.append(burst)
            size = 0
            bw = 0
            t = p[0]

    in_burst_num = len(in_busrt_list)
    out_burst_num = len(out_burst_list)
    burst_num = in_burst_num + out_burst_num
    if in_burst_num == 0 or out_burst_num == 0:
        print(f)
        shutil.move('csv/April/' + f, "unqualified_csv/")
        return 0,0,0,0,0,0,0,0,0
    in_burst_ratio = in_burst_num/burst_num
    out_burst_ratio = out_burst_num/burst_num
    max_in_bandwidth = max_out_bandwidth = 0
    total_in = total_out = 0
    for p in in_busrt_list:
        if p[2] > max_in_bandwidth:
            max_in_bandwidth = p[2]
        total_in += p[2]

    for p in out_burst_list:
        if p[2] > max_out_bandwidth:
            max_out_bandwidth = p[2]
        total_out += p[2]
    in_burst_bandwidth = total_in/in_burst_num
    out_burst_bandwidth = total_out/out_burst_num
    if in_burst_bandwidth < 0 or out_burst_bandwidth < 0:
        print()
    return (burst_num, in_burst_num, out_burst_num, in_burst_ratio, out_burst_ratio, in_burst_bandwidth, out_burst_bandwidth, max_in_bandwidth, max_out_bandwidth)


def features_cal(f, packets):
    total_time = packets[-1][0]
    total_num = len(packets)

    total_bytes = 0
    incoming_bytes = outgoing_bytes = 0
    out_list = []
    in_list = []
    for p in packets:
        if p[2] == 1:
            out_list.append(p)
            outgoing_bytes += p[1]
        else:
            in_list.append(p)
            incoming_bytes += p[1]
        total_bytes += p[1]
    in_bytes_ratio = incoming_bytes/total_bytes
    out_bytes_ratio = outgoing_bytes/total_bytes

    incoming_num = len(in_list)
    outgoing_num = len(out_list)
    in_num_ratio = incoming_num/total_num
    out_num_ratio = outgoing_num/total_num
    # burst_analysis(f, packets)
    burst_num, in_burst_num, out_burst_num, in_burst_ratio, out_burst_ratio, in_burst_bandwidth, out_burst_bandwidth, max_in_bandwidth, max_out_bandwidth = burst_analysis(f, packets)

    # return (total_time, total_num, total_bytes, burst_num,
    #         in_burst_num, in_burst_ratio, out_burst_num, out_burst_ratio,
    #         in_burst_bandwidth, out_burst_bandwidth,
    #         max_in_bandwidth, max_out_bandwidth,
    #         incoming_num, in_num_ratio,
    #         outgoing_num, out_num_ratio,
    #         incoming_bytes, in_bytes_ratio,
    #         outgoing_bytes, out_bytes_ratio)

    features = [f,total_time, total_num, total_bytes, burst_num,
                in_burst_num, in_burst_ratio,
                out_burst_num, out_burst_ratio,
                in_burst_bandwidth, out_burst_bandwidth,
                max_in_bandwidth, max_out_bandwidth,
                incoming_num, in_num_ratio,
                outgoing_num, out_num_ratio,
                incoming_bytes, in_bytes_ratio,
                outgoing_bytes, out_bytes_ratio]
    with open('stats/feature2.csv', 'a') as title:
        writer = csv.writer(title)
        writer.writerow(features)


def main(opts):
    # csv_path = 'csv/April/Announce_Happy_Valentines_Day_??_Google_0_.csv'
    # # csv_path = opts.csvPath
    # packets = su.csv_numpy(csv_path)
    # feature_chi(packets)

    features_title = ['name','total_time', 'total_num', 'total_bytes', 'burst_num',
                'in_burst_num', 'in_burst_ratio',
                'out_burst_num', 'out_burst_ratio',
                'in_burst_bandwidth', 'out_burst_bandwidth',
                'max_in_bandwidth', 'max_out_bandwidth',
                'incoming_num', 'in_num_ratio',
                'outgoing_num', 'out_num_ratio',
                'incoming_bytes', 'in_bytes_ratio',
                'outgoing_bytes', 'out_bytes_ratio']

    path = 'csv/April'

    with open('stats/feature2.csv', 'a') as title:
        writer = csv.writer(title)
        writer.writerow(features_title)
    m = 0
    files = os.listdir(path)
    query_dict = {}
    for f in files:

        m+=1
        src = path + '/' + f
        packets = su.csv_numpy(src)
        trace_name = su.extract_name(f)
        features_cal(trace_name, packets)
        # (total_time, total_num, total_bytes, burst_num,
        # in_burst_num, in_burst_ratio,
        # out_burst_num, out_burst_ratio,
        # in_burst_bandwidth, out_burst_bandwidth,
        # max_in_bandwidth, max_out_bandwidth,
        # incoming_num, in_num_ratio,
        # outgoing_num, out_num_ratio,
        # incoming_bytes, in_bytes_ratio,
        # outgoing_bytes, out_bytes_ratio) = features_cal(trace_name, packets)



        # if trace_name not in query_dict:
        #     q = query(f,total_time, total_num, total_bytes, burst_num,
        #         in_burst_num, in_burst_ratio,
        #         out_burst_num, out_burst_ratio,
        #         in_burst_bandwidth, out_burst_bandwidth,
        #         max_in_bandwidth, max_out_bandwidth,
        #         incoming_num, in_num_ratio,
        #         outgoing_num, out_num_ratio,
        #         incoming_bytes, in_bytes_ratio,
        #         outgoing_bytes, out_bytes_ratio)
        #
        #     new_query = {trace_name:q}
        #     query_dict.update(new_query)
        # else:
        #     query_dict[trace_name].total_time = (total_time + query_dict[trace_name].total_time)/2
        #     query_dict[trace_name].total_num = (total_num + query_dict[trace_name].total_num)/2
        #     query_dict[trace_name].total_bytes = (total_bytes + query_dict[trace_name].total_bytes) / 2
        #     query_dict[trace_name].burst_num = (burst_num + query_dict[trace_name].burst_num) / 2
        #     query_dict[trace_name].in_burst_num = (in_burst_num + query_dict[trace_name].in_burst_num) / 2
        #     query_dict[trace_name].in_burst_ratio = (in_burst_ratio + query_dict[trace_name].in_burst_ratio) / 2
        #     query_dict[trace_name].out_burst_num = (out_burst_num + query_dict[trace_name].out_burst_num) / 2
        #     query_dict[trace_name].out_burst_ratio = (out_burst_ratio + query_dict[trace_name].out_burst_ratio) / 2
        #     query_dict[trace_name].out_burst_bandwidth = (out_burst_bandwidth + query_dict[trace_name].out_burst_bandwidth) / 2
        #     query_dict[trace_name].in_burst_bandwidth = (in_burst_bandwidth + query_dict[trace_name].in_burst_bandwidth) / 2
        #     query_dict[trace_name].max_in_bandwidth = (max_in_bandwidth + query_dict[trace_name].max_in_bandwidth) / 2
        #     query_dict[trace_name].max_out_bandwidth = (max_out_bandwidth + query_dict[trace_name].max_out_bandwidth) / 2
        #     query_dict[trace_name].incoming_num = (incoming_num + query_dict[trace_name].incoming_num) / 2
        #
        #     query_dict[trace_name].in_num_ratio = (in_num_ratio + query_dict[trace_name].in_num_ratio) / 2
        #     query_dict[trace_name].outgoing_num = (outgoing_num + query_dict[trace_name].outgoing_num) / 2
        #     query_dict[trace_name].out_num_ratio = (out_num_ratio + query_dict[trace_name].out_num_ratio) / 2
        #     query_dict[trace_name].incoming_bytes = (incoming_bytes + query_dict[trace_name].incoming_bytes) / 2
        #     query_dict[trace_name].in_bytes_ratio = (in_bytes_ratio + query_dict[trace_name].in_bytes_ratio) / 2
        #     query_dict[trace_name].out_bytes_ratio = (out_bytes_ratio + query_dict[trace_name].out_bytes_ratio) / 2
        #     query_dict[trace_name].outgoing_bytes = (outgoing_bytes + query_dict[trace_name].outgoing_bytes) / 2

        if m%100 == 0:
            print(m)
    # for k, v in query_dict.items():
    #     with open('stats/feature.csv', 'a') as title:
    #         writer = csv.writer(title)
    #         writer.writerow([v.total_time, v.total_num, v.total_bytes, v.burst_num,
    #             v.in_burst_num, v.in_burst_ratio,
    #             v.out_burst_num, v.out_burst_ratio,
    #             v.in_burst_bandwidth, v.out_burst_bandwidth,
    #             v.max_in_bandwidth, v.max_out_bandwidth,
    #             v.incoming_num, v.in_num_ratio,
    #             v.outgoing_num, v.out_num_ratio,
    #             v.incoming_bytes, v.in_bytes_ratio,
    #             v.outgoing_bytes, v.out_bytes_ratio])
    # obs = su.csv_numpy('stats/feature.csv')

def parseOpts(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument('-pc','--csvPath', help='path to read csv files')
    opts = parser.parse_args()
    return opts


if __name__ == "__main__":
    opts = parseOpts(sys.argv)
    main(opts)
