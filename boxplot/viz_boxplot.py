import json

import matplotlib.pyplot as plt
from matplotlib import rcParams
import pandas as pd
import sys


labelsize = 16
rcParams['xtick.labelsize'] = labelsize
rcParams['ytick.labelsize'] = labelsize

def plot(in_file,outfolder):
    f = open(in_file)
    json_data=json.load(f)
    f.close()
    for item in json_data:
        k = next(iter(item))
        data=item[k]
        real = data['real']
        real['fliers']=[]
        fake = data['fake']
        fake['fliers'] = []
        stats = [real, fake]

        fs = 12  # fontsize

        fig, axes = plt.subplots(nrows=1, ncols=1, figsize=(4, 6), sharey=True)
        axes.bxp(stats, positions=[1,1.3])
        axes.set_title('Boxplot for {}'.format(k), fontsize=fs)
        plt.savefig(outfolder+"/"+k+".png", format='png', dpi=300)
        plt.clf()

if __name__ == "__main__":
    # infile="/home/zz/Work/data/amazon/labelled/stats/stats_descriptive_rating.json"
    # outfolder="/home/zz/Work/data/amazon/labelled/stats/boxplots_rating"
    # plot(infile, outfolder)

    infile = "/home/zz/Work/data/amazon/labelled/stats/stats_descriptive_words.json"
    outfolder = "/home/zz/Work/data/amazon/labelled/stats/boxplots_length"
    plot(infile, outfolder)