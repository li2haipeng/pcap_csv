import pandas as pd
import os
import sys
import csv
import collections
from pylab import *


def df_dict(df):

    dic = {}
    k = df.keys().values
    v = df.values
    for i in range(len(k)):
        dic[k[i]] = v[0][i]
    return dic


def update_dict(x, y):
    for k, v in y.items():
        if k in x:
            o = x[k]
            x[k] = o + v
        else:
            x[k] = v
    return x


def main(argv):
    eps = argv[0]
    # eps = '0.5'
    positive = 39305237
    # eps = '0.3'
    path = 'stats/buffer_info_' + eps + '/files'
    files = os.listdir(path)
    f_n = len(files)
    # dum_real = {}
    idx = {}
    time_dic = {}
    real_idx = {}
    for i in range(1, 21):
        # dr_p = path + '/dum_real_' + str(i) + '.csv'
        index_p = path + '/index_' + str(i) + '.csv'
        time_p = path + '/time_' + str(i) + '.csv'
        real_idx_p = path + '/real_index_' + str(i) + '.csv'

        # dum_real_df = pd.read_csv(dr_p)
        index_df = pd.read_csv(index_p)
        time_df = pd.read_csv(time_p)
        rd_df = pd.read_csv(real_idx_p)
        # dum_real_dic, index_dic, t_dic, real_dic = map(df_dict, [dum_real_df, index_df, time_df, rd_df])
        index_dic, t_dic, real_dic = map(df_dict, [index_df, time_df, rd_df])
        parent_dic = [idx, time_dic, real_idx]
        son_dic = [index_dic, t_dic, real_dic]
        idx, time_dic, real_idx = map(update_dict, parent_dic, son_dic)
        print(str(i))


    with open('stats/buffer_info_' + eps + '/index_' + eps +'.csv', 'w') as _idx:
        writer = csv.DictWriter(_idx, idx.keys())
        writer.writeheader()
        writer.writerow(idx)

    with open('stats/buffer_info_' + eps + '/time_' + eps +'.csv', 'w') as _t:
        writer = csv.DictWriter(_t, time_dic.keys())
        writer.writeheader()
        writer.writerow(time_dic)

    # with open('stats/buffer_info_' + eps + '/dum_real_' + eps +'.csv', 'w') as _t:
    #     writer = csv.DictWriter(_t, dum_real.keys())
    #     writer.writeheader()
    #     writer.writerow(dum_real)

    # real_idx['0.0'] += positive

    sum_idx = sum(i for i in idx.values())
    sum_time = sum(i for i in time_dic.values())
    sum_real = sum(i for i in real_idx.values())

    real_idx1 ={}
    for k, v in real_idx.items():
        real_idx1[float(k)] = v
    real_idx = collections.OrderedDict(sorted(real_idx1.items()))
    a = positive - sum_real
    real_idx[0] += a
    time_dic['0'] += a
    with open('stats/buffer_info_' + eps + '/real_index_' + eps +'.csv', 'w') as _t:
        writer = csv.DictWriter(_t, real_idx.keys())
        writer.writeheader()
        writer.writerow(real_idx)

    sum_idx = sum(i for i in idx.values())
    sum_time = sum(i for i in time_dic.values()) - time_dic['-1']
    sum_real = sum(i for i in real_idx.values())
    idx_pdf = {}
    time_pdf = {}
    real_pdf = {}

    idx_cdf = {}
    time_cdf = {}
    real_cdf = {}
    cdf_idx = 0
    cdf_time = 0
    cdf_real = 0
    for k, v in idx.items():
        r = (v / sum_idx)
        cdf_idx += r
        idx_pdf[k] = r
        idx_cdf[k] = cdf_idx

    for k, v in time_dic.items():
        r = (v / sum_time)
        cdf_time += r
        time_pdf[k] = r
        time_cdf[k] = cdf_time

    for k, v in real_idx.items():
        r = (v / sum_real)
        cdf_real += r
        real_pdf[k] = r
        real_cdf[k] = cdf_real

    with open('stats/buffer_info_' + eps + '/index_pdf_' + eps +'.csv', 'w') as _i_p:
        writer = csv.DictWriter(_i_p, idx_pdf.keys())
        writer.writeheader()
        writer.writerow(idx_pdf)

    with open('stats/buffer_info_' + eps + '/time_pdf_' + eps +'.csv', 'w') as _t_p:
        writer = csv.DictWriter(_t_p, time_pdf.keys())
        writer.writeheader()
        writer.writerow(time_pdf)

    with open('stats/buffer_info_' + eps + '/real_pdf_' + eps +'.csv', 'w') as _r_p:
        writer = csv.DictWriter(_r_p, real_pdf.keys())
        writer.writeheader()
        writer.writerow(real_pdf)

    with open('stats/buffer_info_' + eps + '/index_cdf_' + eps +'.csv', 'w') as _i_c:
        writer = csv.DictWriter(_i_c, idx_cdf.keys())
        writer.writeheader()
        writer.writerow(idx_cdf)

    with open('stats/buffer_info_' + eps + '/time_cdf_' + eps + '.csv', 'w') as _t_c:
        writer = csv.DictWriter(_t_c, time_cdf.keys())
        writer.writeheader()
        writer.writerow(time_cdf)

    with open('stats/buffer_info_' + eps + '/real_cdf_' + eps + '.csv', 'w') as _r_c:
        writer = csv.DictWriter(_r_c, real_cdf.keys())
        writer.writeheader()
        writer.writerow(real_cdf)


if __name__ == '__main__':
    main(sys.argv[1:])
    # main()


