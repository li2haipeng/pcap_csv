import os
import sys
import shutil

import pandas as pd


def delay_per_trace(eps):

    buffer_path = '/home/lhp/PycharmProjects/2019_spring_data/optionB/'
    csv_path = '/home/lhp/PycharmProjects/pcap_csv/csv/gamma/'
    positive_num = 0
    total_time = 0
    file_num = 0

    for folder in range(1, 21):
        csv_files_p = csv_path + str(folder)
        buffer_files_p = buffer_path + eps + '/' + str(folder)
        buffer_files = os.listdir(buffer_files_p)
        buffer_files.sort()
        for f in buffer_files:
            try:
                o_f = f[0:-10] + '.csv'
                o_packets = pd.read_csv(csv_files_p + '/' + o_f)
                b_packets = pd.read_csv(buffer_files_p + '/' + f)
                b = b_packets.iloc[-2, 3]
                a = o_packets.iloc[-1, 0]
                time_diff = max(b - a, 0)
                file_num += 1
                total_time += time_diff
                if time_diff > 0:
                    positive_num += 1
            except:
                continue
        print(folder)
    ave = total_time / file_num
    print(eps, ave, file_num, positive_num)


def filter(eps, folder):
    folder_p = '/home/lhp/PycharmProjects/pcap_csv/obf_data/lap_list/' + eps + '/' + folder
    files = os.listdir(folder_p)
    files.sort()
    for f in files:
        file_p = folder_p + '/' + f
        packets = pd.read_csv(file_p)
        for p in packets:
            dir = p[2]
            if dir != 1.0 and dir != -1.0:
                print(file_p)
                break

        shutil.move(file_p, '/home/lhp/PycharmProjects/pcap_csv/unqualified_csv')

def total_packets():
    p = 'csv/gamma/'
    folders = os.listdir(p)
    folders.sort()
    n = 0
    for folder in folders:
        f_p = p + folder
        files = os.listdir(f_p)
        files.sort()
        for f in files:
            ff_p = f_p + '/' + f
            try:
                packets = pd.read_csv(ff_p)
            except:
                continue
            n += len(packets)
        print(folder,n)

def main():
    delay_per_trace('0.005')
    delay_per_trace('0.05')
    # count('5.0')
    # eps = argv[0]
    # folder = argv[1]
    # filter(eps,folder)
    # total_packets()



if __name__ == '__main__':
    main()
