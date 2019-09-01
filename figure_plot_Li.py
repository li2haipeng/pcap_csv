import csv
from pathlib import Path
from pylab import *
import matplotlib.font_manager
import matplotlib
import pandas as pd
from scapy.all import *


def csv_numpy(packet_path):

    """

    Take the csv files, convert it to "list" structure or "ndarray" structure. Use either of the two

    structure for the future data analysis.

    :param packet_path: path of the csv file

    :return: return the traffic data in a data structure of "list" or "ndarray"

    """

    reader = csv.reader(open(packet_path + '.csv', "r"), delimiter=",")
    query_in_list = list(reader)
    query_in_list.pop(0)
    query_in_array = np.array(query_in_list).astype(float)
    query_in_list = query_in_array.tolist()

    # for p in query_in_list:
    #     p.remove(p[0])

    return query_in_list


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
    p_l=[]

    for i in range(0, num_packets):
        p_list = packets[burst_ranges[i][0]:burst_ranges[i][1]]
        init_time = p_list[0].time
        # print(init_time)

        echo_df = pd.DataFrame(columns=['time', 'size', 'direction'])
        p_list.reverse()
        for p in p_list:

            # 1 if echo is src, -1 if destination

            if p[IP].src == echo_ip:
                p[IP].src = 1
            else:
                p[IP].src = -1

            # Update the df with correct index

            echo_df.loc[-1] = [p.time - init_time, p.len, p[IP].src]
            echo_df.index = echo_df.index + 1

        # Sort, so list starts in non-reverse order, save to csv

        echo_df = echo_df.sort_index()
        echo_df.to_csv(csv_path + trace_name + "_" + str(i+1) + ".csv", index=False)
        p_l = echo_df.values.tolist()

    return p_l


def figure_gen(r_l):

    matplotlib.rcParams['ps.useafm'] = True

    matplotlib.rcParams['pdf.use14corefonts'] = True

    # matplotlib.rcParams['text.usetex'] = True

    # Set appropriate figure width/height

    fig = plt.figure(figsize=(5.75, 3.75))

    # Set appropriate margins, these values are normalized into the range [0, 1]

    subplots_adjust(left=0.20, bottom=0.20, right=0.90, top=0.90, wspace=0.1, hspace=0.1)

    # Set parameters in the figure

    x = [0]
    y = [0]

    for p in r_l:

        x.append(p[0])
        y.append(p[2]/1024.0)

    x.append(r_l[-1][0]+0.1)
    y.append(0)
    # Plot lines in the figure

    ax = fig.add_subplot(111)
    ax.plot(x, y, '-', linewidth=2, color='red')

    prop = matplotlib.font_manager.FontProperties(size=12)

    # leg = legend(loc='upper left', prop=prop)
    # set the fontsize of the legend
    # for t in leg.get_texts():
    #    t.set_fontsize('16')


    # set ticker
    majorLocator_x = MultipleLocator(1)
    majorLocator_y = MultipleLocator(100)
    ax.xaxis.set_major_locator(majorLocator_x)
    ax.yaxis.set_major_locator(majorLocator_y)

    # Set labels for axes

    ax.tick_params(labelsize=16)
    ax.set_ylim(0, 500)

    xlim(0, 3.5)
    xlabel('Time (second)', fontsize=16)
    ax.set_ylabel('Kb/second', fontsize=16)

    # Save file as .eps

    savefig('chirstms2.pdf', format='pdf')
    show()
    exit(0)


if __name__ == "__main__":

    path = '/home/lhp/Desktop/How_many_days_until_christmas?_??_Matt_114_.csv'
    # ip = '127.0.0.1'

    # r = burst_detector_short(path)
    # packets = rdpcap(path)
    # r = [(0,len(packets)-1)]
    # a = pcap_converter(path, ip, r)
    a = pd.read_csv(path)
    a = a.values.tolist()
    interval = 0.1
    b = a[-1][0]/interval
    b_s = 0
    b_e = b_s + interval
    amount = 0
    rates = 0
    rates_l = []

    ##convert packets per second to bytes persecond

    for n in range(int(round(b))):

        rates_l.append([round(b_e,2), 0, 0])
        b_e += interval

    for m in rates_l:

        for p in a:

            if p[0] < m[0] - interval:
                continue
            if p[0]<=m[0]:
                m[1] = m[1] + p[1]
            else:
                break
    for m in rates_l:
        m[2] = m[1]/interval
    figure_gen(rates_l)



