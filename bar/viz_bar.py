
import matplotlib.pyplot as plt
import numpy as np
import sys
import pandas as pd
from matplotlib import rcParams

labelsize = 3
rcParams['xtick.labelsize'] = labelsize
rcParams['ytick.labelsize'] = labelsize

def plot(in_file, out_file):
    df = pd.read_csv(in_file, header=0)
    fig=df.plot(x='name', kind='barh', stacked=True,
            title='Stacked Bar Graph',mark_right = True).get_figure()
    fig.savefig(out_file, dpi=300)
    print("done")


if __name__ == "__main__":
    infile = "/home/zz/Work/data/amazon/labelled/stats/stats_dist_rating.csv"
    outfile = "/home/zz/Work/data/amazon/labelled/stats/stacked_bar_rating.png"
    plot(infile, outfile)

    infile = "/home/zz/Work/data/amazon/labelled/stats/stats_dist_words.csv"
    outfile = "/home/zz/Work/data/amazon/labelled/stats/stacked_bar_words.png"
    plot(infile, outfile)