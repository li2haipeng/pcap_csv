import pandas as pd
import os
import sys
import csv
import collections
from pylab import *
import matplotlib.font_manager
import matplotlib
import selfUtils as su
# import matplotlib.pyplot as plt


def df_dict(df):

    dic = {}
    k = df.keys().values
    v = df.values
    for i in range(len(k)):
        dic[k[i]] = v[0][i]
    return dic


def bar_fig(x, y, y1, y2, n_g):

    n_groups = n_g

    # create plot
    fig, ax = plt.subplots(figsize = (5.75, 3.75))
    index = np.arange(n_groups)
    bar_width = 0.2
    opacity = 0.8

    rects1 = plt.bar(index, y, bar_width,
                     alpha=opacity,
                     color='r',label='0.05')

    rects2 = plt.bar(index + bar_width, y1, bar_width,
                     alpha=opacity,
                     color='g',
                     label='0.5')

    rects3 = plt.bar(index + 2* bar_width, y2, bar_width,
                     alpha=opacity,
                     color='black',
                     label='5.0')



    plt.xlabel('latency per packet (packet)', fontsize=16)
    plt.ylabel('pdf',fontsize=16)
    # plt.title('PDF of buffer cleaning latency')
    plt.xticks(index + bar_width, x)
    plt.legend()
    plt.tight_layout()
    savefig('real_packet_pdf.pdf', format='pdf')
    plt.show()
    exit(0)


def fig_order(x, y, y1, y2, y3): ## name, x, y, x_lim, y_lim, x_step, y_step, x_lable


    matplotlib.rcParams['ps.useafm'] = True
    matplotlib.rcParams['pdf.use14corefonts'] = True

    # matplotlib.rcParams['text.usetex'] = True
    # Set appropriate figure width/height

    fig = plt.figure(figsize=(5.75, 3.75))

    # Set appropriate margins, these values are normalized into the range [0, 1]

    subplots_adjust(left=0.20, bottom=0.20, right=0.90, top=0.90, wspace=0.1, hspace=0.1)


    # Plot lines in the figure

    ax = fig.add_subplot(111)
    ax.plot(x, y, marker ='^',  markersize = 12, markerfacecolor='none', linewidth=0.6, color='red',label='5.0')
    ax.plot(x, y1, marker ='o', markersize = 12, markerfacecolor='none', linewidth=0.6, color='green',label='0.5')
    ax.plot(x, y2, marker ='s', markersize = 12,  markerfacecolor='none', linewidth=0.6, color='black', label='0.05')
    ax.plot(x, y3, marker='*', markersize=12, markerfacecolor='none', linewidth=0.6, color='blue', label='0.005')


    prop = matplotlib.font_manager.FontProperties(size=12)

    leg = legend(loc='lower right', prop=prop)
    # set the fontsize of the legend
    for t in leg.get_texts():
       t.set_fontsize('16')

    # set ticker
    majorLocator_x = MultipleLocator(1)
    majorLocator_y = MultipleLocator(0.1)
    ax.xaxis.set_major_locator(majorLocator_x)
    ax.yaxis.set_major_locator(majorLocator_y)

    # Set labels for axes

    ax.tick_params(labelsize=16)
    ax.set_ylim(0.4, 1.05)

    # xlim(0, 15)
    xlabel('latency per packet (second)', fontsize=16)
    ax.set_ylabel('CDF', fontsize=16)

    # Save file as .eps

    savefig('time_cdf_1.pdf', format='pdf')
    show()
    exit(0)


def latency_plot():

    eps = '5.0'
    idx_pdf_csv = pd.read_csv('stats/buffer_info_' + eps + '/index_pdf_' + eps + '.csv')
    idx_cdf_csv = pd.read_csv('stats/buffer_info_' + eps + '/index_cdf_' + eps + '.csv')
    time_pdf_csv = pd.read_csv('stats/buffer_info_' + eps + '/time_pdf_' + eps + '.csv')
    time_cdf_csv = pd.read_csv('stats/buffer_info_' + eps + '/time_cdf_' + eps + '.csv')
    # dum_real_csv = pd.read_csv('stats/buffer_info_' + eps + '/dr_' + eps + '.csv')
    real_pdf_csv = pd.read_csv('stats/buffer_info_' + eps + '/real_pdf_' + eps + '.csv')
    real_cdf_csv = pd.read_csv('stats/buffer_info_' + eps + '/real_cdf_' + eps + '.csv')
    eps = '0.5'
    idx_pdf_csv1 = pd.read_csv('stats/buffer_info_' + eps + '/index_pdf_' + eps + '.csv')
    idx_cdf_csv1 = pd.read_csv('stats/buffer_info_' + eps + '/index_cdf_' + eps + '.csv')
    time_pdf_csv1 = pd.read_csv('stats/buffer_info_' + eps + '/time_pdf_' + eps + '.csv')
    time_cdf_csv1 = pd.read_csv('stats/buffer_info_' + eps + '/time_cdf_' + eps + '.csv')
    # dum_real_csv1 = pd.read_csv('stats/buffer_info_' + eps + '/dr_' + eps + '.csv')
    real_pdf_csv1 = pd.read_csv('stats/buffer_info_' + eps + '/real_pdf_' + eps + '.csv')
    real_cdf_csv1 = pd.read_csv('stats/buffer_info_' + eps + '/real_cdf_' + eps + '.csv')
    #
    eps = '0.05'
    idx_pdf_csv2 = pd.read_csv('stats/buffer_info_' + eps + '/index_pdf_' + eps + '.csv')
    idx_cdf_csv2 = pd.read_csv('stats/buffer_info_' + eps + '/index_cdf_' + eps + '.csv')
    time_pdf_csv2 = pd.read_csv('stats/buffer_info_' + eps + '/time_pdf_' + eps + '.csv')
    time_cdf_csv2 = pd.read_csv('stats/buffer_info_' + eps + '/time_cdf_' + eps + '.csv')
    # dum_real_csv2 = pd.read_csv('stats/buffer_info_' + eps + '/dr_' + eps + '.csv')
    real_pdf_csv2 = pd.read_csv('stats/buffer_info_' + eps + '/real_pdf_' + eps + '.csv')
    real_cdf_csv2 = pd.read_csv('stats/buffer_info_' + eps + '/real_cdf_' + eps + '.csv')

    eps = '0.005'
    idx_pdf_csv3 = pd.read_csv('stats/buffer_info_' + eps + '/index_pdf_' + eps + '.csv')
    idx_cdf_csv3 = pd.read_csv('stats/buffer_info_' + eps + '/index_cdf_' + eps + '.csv')
    time_pdf_csv3 = pd.read_csv('stats/buffer_info_' + eps + '/time_pdf_' + eps + '.csv')
    time_cdf_csv3 = pd.read_csv('stats/buffer_info_' + eps + '/time_cdf_' + eps + '.csv')
    # dum_real_csv3 = pd.read_csv('stats/buffer_info_' + eps + '/dr_' + eps + '.csv')
    real_pdf_csv3 = pd.read_csv('stats/buffer_info_' + eps + '/real_pdf_' + eps + '.csv')
    real_cdf_csv3 = pd.read_csv('stats/buffer_info_' + eps + '/real_cdf_' + eps + '.csv')

    idx_pdf, idx_cdf, time_pdf, time_cdf = map(df_dict, [idx_pdf_csv, idx_cdf_csv, time_pdf_csv, time_cdf_csv])
    idx_pdf1, idx_cdf1, time_pdf1, time_cdf1 = map(df_dict, [idx_pdf_csv1, idx_cdf_csv1, time_pdf_csv1, time_cdf_csv1])
    idx_pdf2, idx_cdf2, time_pdf2, time_cdf2 = map(df_dict, [idx_pdf_csv2, idx_cdf_csv2, time_pdf_csv2, time_cdf_csv2])
    idx_pdf3, idx_cdf3, time_pdf3, time_cdf3 = map(df_dict, [idx_pdf_csv3, idx_cdf_csv3, time_pdf_csv3, time_cdf_csv3])

    real_pdf, real_cdf = map(df_dict, [real_pdf_csv, real_cdf_csv])
    real_pdf1, real_cdf1 = map(df_dict, [real_pdf_csv1, real_cdf_csv1])
    real_pdf2, real_cdf2 = map(df_dict, [real_pdf_csv2, real_cdf_csv2])
    real_pdf3, real_cdf3 = map(df_dict, [real_pdf_csv3, real_cdf_csv3])

    # x = list(real_cdf.keys())[0:7]
    # xx = list(int(float(i)) for i in x)
    # y = list(real_cdf.values())[0:7]
    # y1 = list(real_cdf1.values())[0:7]
    # y2 = list(real_cdf2.values())[0:7]

    xx = list(time_cdf.keys())[0:5]
    y = list(time_cdf.values())[0:5]
    y1 = list(time_cdf1.values())[0:5]
    y2 = list(time_cdf2.values())[0:5]
    y3 = list(time_cdf3.values())[0:5]

    fig_order(xx, y, y1, y2, y3)
    # bar_fig(x, y,y1,y2,7)


def main():

    # latency_plot()

######################################################Distirbution Figure Generator#############################################################################################

    in_interval = pd.read_csv('stats/distribution_gamma/adapt_in_distribution_interval.csv')
    in_size = pd.read_csv('stats/distribution_gamma/adapt_in_distribution_size.csv')
    out_interval = pd.read_csv('stats/distribution_gamma/adapt_out_distribution_interval.csv')
    out_size = pd.read_csv('stats/distribution_gamma/adapt_out_distribution_size.csv')

    # in_interval_l, in_size_l, out_interval_l, out_size_l = map(lambda l: l.values.tolist(), [in_interval, in_size, out_interval, out_size])

    in_interval_l, in_size_l, out_interval_l, out_size_l = map(su.csv_numpy,
                                                               ['stats/distribution_gamma/in_interval_r.csv', 'stats/distribution_gamma/in_size_r.csv',
                                                                'stats/distribution_gamma/out_interval_r.csv', 'stats/distribution_gamma/out_size_r.csv'])

    # x = [str(p[0]) for p in out_interval_l]
    x=[]
    for p in in_size_l:
        if p[0] < 1:
            x.append(str(p[0]))
        else:
            x.append(str(int(p[0])))
    y = [p[1] for p in in_size_l][0:10]



    # create plot
    fig, ax = plt.subplots(figsize=(7.75, 3.75))
    index = np.arange(10)
    bar_width = 0.5
    opacity = 0.8

    rects1 = plt.bar(index + bar_width, y, bar_width,
                     alpha=opacity,
                     color='blue')


    # plt.xlabel('Packet inter-arrival time (ms)', fontsize=16)
    plt.xlabel('Packet size (byte)', fontsize=16)
    plt.ylabel('PDF', fontsize=16)
    # plt.title('PDF of buffer cleaning latency')
    plt.xticks(index + bar_width, x[0:10])
    ax.tick_params(labelsize = 16)


    majorLocator_y = MultipleLocator(0.1)
    ax.yaxis.set_major_locator(majorLocator_y)

    # Set labels for axes

    ax.tick_params(labelsize=16)
    ax.set_ylim(0, 0.7)

    plt.tight_layout()
    savefig('in_size.pdf', format='pdf')
    plt.show()
    exit(0)


if __name__ == '__main__':
    main()
