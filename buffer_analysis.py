# from __future__ import division
import pandas as pd
import csv
import collections
from pylab import *
import math
import os


def proc_num(idx_dict, time_dict, dum_real, real_idx_dict, eps, folder):

    sum_idx = sum(i for i in idx_dict.values())
    sum_time = sum(i for i in time_dict.values())
    idx_dict = collections.OrderedDict(sorted(idx_dict.items()))

    with open('stats/buffer_info_' + eps + '/files/index_' + folder + '.csv', 'w') as _idx:
        writer = csv.DictWriter(_idx, idx_dict.keys())
        writer.writeheader()
        writer.writerow(idx_dict)

    with open('stats//buffer_info_' + eps + '/files/time_' + folder + '.csv', 'w') as _t:
        writer = csv.DictWriter(_t, time_dict.keys())
        writer.writeheader()
        writer.writerow(time_dict)

    # with open('stats//buffer_info_' + eps + '/files/dum_real_' + folder + '.csv', 'w') as _d:
    #     writer = csv.DictWriter(_d, dum_real.keys())
    #     writer.writeheader()
    #     writer.writerow(dum_real)

    with open('stats//buffer_info_' + eps + '/files/real_index_' + folder + '.csv', 'w') as _r:
        writer = csv.DictWriter(_r, real_idx_dict.keys())
        writer.writeheader()
        writer.writerow(real_idx_dict)



def main(argv):

    # path = '/home/lhp/PycharmProjects/2019_spring_data/buffer_info'
    p = '/home/lhp/PycharmProjects/2019_spring_data/optionB/'
    eps = argv[0]
    folder = argv[1]
    # eps = 0.3
    # folder = 1]
    path = p + eps + '/'+ folder
    # dst = argv[1]
    # folders = os.listdir(path)
    # folders.sort()
    idx_dict = {}
    real_idx_dict = {}
    positive_n = 0
    # time_dict = {0.000001: 0, 0.00001: 0, 0.0001: 0, 0.001: 0, 0.01: 0, 0.1: 0, 1: 0, 10: 0, 100: 0}
    time_dict = {0: 0,
                 0.001: 0,
                 0.01: 0,
                 0.1: 0,
                 1: 0,
                 10: 0,
                 100: 0}
    dum_real = {}
    idx_dif = 0
    time_dif = 0.0
    real_idx_dif = 0
    time_dif_sum = 0.0
    # for folder in folders:
    #     file_path = path + '/' + folder
    files = os.listdir(path)
    files.sort()
    for file in files:
        buffer_df = pd.read_csv(path + '/' + file)
        l = buffer_df.shape[0]
        buffered_t = buffer_df.iloc[:, 0]
        buffered_idx = buffer_df.iloc[:, 1]
        # real_idx = buffer_df.iloc[:, 3]
        cleaned_t = buffer_df.iloc[:, 3]
        cleaned_idx = buffer_df.iloc[:, 4]
        d_r = buffer_df.iloc[:, 5:7]

        for i in range(l):
            if not buffer_df.iloc[i].isnull().values.any():
                idx_dif = abs(buffered_idx[i] - cleaned_idx[i])
                # real_idx_dif = abs(real_idx[i] - buffered_idx[i])
                time_dif = abs(buffered_t[i] - cleaned_t[i])
                time_dif_sum += time_dif

                # print(time_dif)
                if idx_dif in idx_dict.keys():
                    idx_dict[idx_dif] += 1
                else:
                    idx_dict[idx_dif] = 1

                # if real_idx_dif in real_idx.keys():
                #     real_idx[real_idx_dif] += 1
                # else:
                #     real_idx[real_idx_dif] = 1

                for k in time_dict:
                    if time_dif <= k:
                        time_dict[k] +=1
                        break
                if idx_dif == 0:
                    real_idx_dif = d_r.values[i][1]
                if d_r.values[i][0] == 0:
                    real_idx_dif = idx_dif
                else:
                    real_idx_dif = idx_dif - d_r.values[i][0]

                if real_idx_dif in real_idx_dict.keys():
                    real_idx_dict[real_idx_dif] += 1
                else:
                    real_idx_dict[real_idx_dif] = 1

                dr_str = str(int(float(d_r.values[i][0]))) + '|' + str(int(float(d_r.values[i][1])))
                if dr_str in dum_real.keys():
                    dum_real[dr_str] += 1
                else:
                    dum_real[dr_str] = 1

            else:
                    positive_n = positive_n + buffer_df.iat[i, 0]

        # print(file + "is finished!!")

    idx_dict[-1111] = positive_n
    # time_dict[-1] = positive_n
    time_dict[-1] = time_dif_sum
    # dum_real[-1] = positive_n
    proc_num(idx_dict, time_dict, dum_real, real_idx_dict, eps, folder)
    print(folder + 'is finished')

if __name__ == '__main__':
    # argv = ['0.3', '1']
    main(sys.argv[1:])
    # main(argv)
