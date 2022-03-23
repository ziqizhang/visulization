
import matplotlib.pyplot as plt
import numpy as np
import sys
import pandas as pd
import seaborn as sns
from matplotlib import rcParams

labelsize = 3
rcParams['xtick.labelsize'] = labelsize
rcParams['ytick.labelsize'] = labelsize

def plot(in_file, out_file, rotate_y=0, rotate_x=0):
    df = pd.read_csv(in_file, header=0)
    row_header=df.columns.values[1:]
    df=df.values
    col_header=df[:,0]
    df=df[:, 1:]
    df = df.astype(np.float)

    ax = sns.heatmap(df, annot=True, fmt='.2f', linewidth=0.5,cmap='RdYlGn',
                     annot_kws={"size": 5})
    y_labels=list(col_header)
    x_labels = list(row_header)
    ax.set_yticklabels(y_labels)
    ax.set_xticklabels(x_labels)
    plt.yticks(rotation=rotate_y)
    plt.xticks(rotation=rotate_x)
    plt.subplots_adjust(left=0.4)
    plt.subplots_adjust(bottom=0.2)
    plt.savefig(out_file, format='png', dpi=300)
    plt.clf()
    print("done")


if __name__ == "__main__":
    # infile = "/home/zz/Work/data/amazon/labelled/stats/stats_dist_rating.csv"
    # outfile = "/home/zz/Work/data/amazon/labelled/stats/heatmap_rating.png"
    # plot(infile, outfile,0,0)
    #
    # infile = "/home/zz/Work/data/amazon/labelled/stats/stats_dist_words.csv"
    # outfile = "/home/zz/Work/data/amazon/labelled/stats/heatmap_length.png"
    # plot(infile, outfile,0,90)

    infile = "/home/zz/Work/data/amazon/labelled/stats/stats_dist_rating_real.csv"
    outfile = "/home/zz/Work/data/amazon/labelled/stats/heatmap_rating_real.png"
    plot(infile, outfile, 0, 0)

    infile = "/home/zz/Work/data/amazon/labelled/stats/stats_dist_rating_fake.csv"
    outfile = "/home/zz/Work/data/amazon/labelled/stats/heatmap_rating_fake.png"
    plot(infile, outfile, 0, 0)

    infile = "/home/zz/Work/data/amazon/labelled/stats/stats_dist_words_real.csv"
    outfile = "/home/zz/Work/data/amazon/labelled/stats/heatmap_length_real.png"
    plot(infile, outfile, 0, 90)

    infile = "/home/zz/Work/data/amazon/labelled/stats/stats_dist_words_fake.csv"
    outfile = "/home/zz/Work/data/amazon/labelled/stats/heatmap_length_fake.png"
    plot(infile, outfile, 0, 90)