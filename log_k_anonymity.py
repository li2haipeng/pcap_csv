import selfUtils as su
import sys
import argparse
from pathlib import Path
import pandas as pd


def divide_list(packets):
    for i,p in enumerate(packets):
        if (float(p[2]) + float(packets[i+1][2]) == 0):
            return i


def add_dummy(packets):
    max_num = int(packets[-1][0])
    for p in packets:
        if int(p[0]) < max_num:
            dummy_num = max_num - int(p[0])
            p.append(dummy_num)

    return packets


def incoming_process(trace_name, incoming_list, interval, size, start_time):
    distribution = su.csv_numpy("stats/logk_distribution.csv")
    stats = su.csv_numpy("stats/filter_stats.csv")

    log_in_num = 0
    remainder = 0
    duplex_in_num = 0
    time = 0

    for p in stats:
        if p[0] == trace_name:
            duplex_in_num = p[5]
            remainder = p[6]
            break
    for p in distribution:
        if su.same_name(p[0],trace_name):
            if p[-1] == '':
                added_num = 0
            else:
                added_num = int(float(p[-1]))
            log_in_num = added_num + p[-3]

            break
    # original_end = packets[-1][1]
    incoming = []
    added_num = log_in_num - duplex_in_num - 1
    index = 0
    for i in range(int(duplex_in_num) + 1):
        time = start_time + interval*(i+1)
        # index = start_index + i + 1
        direction = -1
        original_packet = [time, size, direction, 0, 'original']
        if i == duplex_in_num:
            original_packet = [time, size, direction, size-remainder, 'padded']
        incoming.append(original_packet)
    for i in range(int(added_num)):
        time = time + interval
        # index = index + i + 1
        direction = -1
        dummy_packet = [time, size, direction, size, 'dummy']
        incoming.append(dummy_packet)
    return incoming


def outgoing_process(trace_name, interval):
    outgoing_stats = su.csv_numpy("stats/filter_stats.csv")
    outgoing_stats.sort(key=su.sort_by_fourth)
    out_num = outgoing_stats[-1][3]
    size = 1500
    original_num = 0
    remainder = 0
    time = 0
    for p in outgoing_stats:
        if p[0] == trace_name:
            original_num = p[3]
            remainder = p[4]
            break
    out_list = []
    for i in range(int(original_num) + 1):
        time = i*interval
        packet = [time, size, 1, 0, 'original']
        if i == original_num:
            packet = [time, size, 1, 1500-remainder, 'padded']
        out_list.append(packet)
    for i in range(int(out_num-original_num-1)):
        time = time + (i+1)* interval
        packet = [time, size, 1, size, 'dummy']
        out_list.append(packet)

    return out_list


def main(opts):
    # duplex_path = "half_duplex/Announce_Happy_Valentines_Day_29__0218._HD.csv"
    # out_interval = 0.5
    # in_interval = 1
    # size = 1500

    duplex_path = opts.hdPath
    size = float(opts.size)
    out_interval = float(opts.oInterval)
    in_interval = float(opts.iInterval)

    pf = Path(duplex_path)

    trace_name = pf.name[0:-7]
    duplex_list = su.csv_numpy(duplex_path)
    index = divide_list(duplex_list)
    outgoing_list = duplex_list[0:index+1]
    # same_outgoing = outgoing_process_buflo_method(outgoing_list, 1500, out_interval, size)

    same_outgoing = outgoing_process(trace_name, out_interval)
    outgoing_end = same_outgoing[-1][0]

    incoming_list = duplex_list[index+1: len(duplex_list)]
    logk_incoming = incoming_process(trace_name, incoming_list, in_interval, size, outgoing_end)
    logk_list = same_outgoing + logk_incoming

    logk_df = pd.DataFrame(logk_list,columns=['time', 'size', 'direction', 'overhead', 'type'])
    logk_df.to_csv("logk_list/" + trace_name + '_logk_.csv',index=False)

    print('logk of ' + trace_name + "is finished")


def parseOpts(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument('-ph', '--hdPath', help='path of half duplex files')
    parser.add_argument('-s', '--size', help='size of outgoing packets')
    parser.add_argument('-o', '--oInterval', help='interval of outgoing packets')
    parser.add_argument('-i', '--iInterval', help='interval of incoming packets')
    opts = parser.parse_args()
    return opts


if __name__ == '__main__':
    opts = parseOpts(sys.argv)
    main(opts)
