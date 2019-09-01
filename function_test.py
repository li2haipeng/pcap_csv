import selfUtils as su
import math
from sklearn.feature_selection import chi2, SelectKBest
import pandas as pd
import os


def main():
    obs = su.csv_numpy('stats/feature.csv')

    y = []
    for i in range(0,29):
        y.append(i)

    kbest = SelectKBest(score_func=chi2, k=5).fit(obs,y)
    x_new = kbest.transform(obs)
    a = kbest.scores_

    b = pd.DataFrame(a)
    b.to_csv('stats/scores.csv')
    print(a)


def preprocess():
    pre_data = []
    path = 'csv/gamma'
    folder = os.listdir(path)
    folder.sort()
    for i,f in enumerate(folder):
        p = path + '/' + f
        file = os.listdir(p)
        file.sort()
        print(p)
        for i, m in enumerate(file):
            d = []
            d.append(m)
            a = p+ '/' + m
            data = su.csv_numpy(a)
            for pa in data:
                d.append(pa[1]*pa[2] + 3000)
                if len(d) >= 401:
                    break
            if len(d) < 401:
                d = (d + (401-len(d))*[0])[:401]

            pre_data.append(d)

    return pre_data


def main2(df,index):
    # X = pd.read_csv('/home/lhp/Downloads/Gamma_v2_with_class.csv',index_col=0)
    # data = X[['total_time', 'total_num', 'total_bytes', 'burst_num',
    #             'in_burst_num', 'in_burst_ratio',
    #             'out_burst_num', 'out_burst_ratio',
    #             'in_burst_bandwidth', 'out_burst_bandwidth',
    #             'max_in_bandwidth', 'max_out_bandwidth',
    #             'incoming_num', 'in_num_ratio',
    #             'outgoing_num', 'out_num_ratio',
    #             'incoming_bytes', 'in_bytes_ratio',
    #             'outgoing_bytes', 'out_bytes_ratio']]
    # data_l = data.values.tolist()
    # data.to_csv('stats/abc.csv')
    data = df[index[1:]]
    # data_l = data.values.tolist()
    # tri_list = []
    # for i in data_l:
    #     tri_row = []
    #     for j in i:
    #         tri_row.append(j+2)
    #     tri_list.append(tri_row)
    label = df[['class']]
    # label_l = label.values.tolist()
    kbest = SelectKBest(score_func=chi2, k = 5).fit(data, label)
    a = kbest.scores_
    b = pd.DataFrame(a)
    b.to_csv('stats/scores.csv')

def cal():
    t = 0
    path = '/home/lhp/PycharmProjects/pcap_csv/csv/gamma/'
    folders = os.listdir(path)
    for folder in folders:
        p = path + folder
        files = os.listdir(p)
        for f in files:
            f_p = p + '/' + f
            list = su.csv_numpy(f_p)
            t += len(list)
    print(t)

if __name__ == "__main__":
    # # data = preprocess()
    # index = ['class']
    # for i in range(400):
    #     index.append(str(i))
    #
    # # df = pd.DataFrame(data,columns=index)
    # # df.to_csv('stats/pre_data.csv')
    # # su.just_class('stats/pre_data.csv')
    # df = pd.read_csv('stats/Gamma_class.csv')
    #
    # main2(df,index)
    cal()


