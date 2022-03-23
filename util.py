import pandas as pd
import json

def join_boxplot_heatmap_data(infile_boxplot_stats, infile_heatmap_stats,
                              outfile):
    df_heatmap = pd.read_csv(infile_heatmap_stats, header=0)
    f = open(infile_boxplot_stats)
    json_data = json.load(f)
    f.close()

    header=["name", "mean","median","q1","q3","stdev","variance","max","min"]
    rows=[]
    rows.append(header)
    for item in json_data:
        k = next(iter(item))
        data=item[k]
        real = data['real']
        del real["label"]
        real=dict(sorted(real.items()))
        real=list(real.values())
        real.insert(0, k+" Real")

        fake = data['fake']
        del fake["label"]
        fake = dict(sorted(fake.items()))
        fake = list(fake.values())
        fake.insert(0, k+" Fake")

        rows.append(real)
        rows.append(fake)

    df_boxplot = pd.DataFrame(rows[1:], columns=rows[0])
    merged=pd.merge(df_heatmap, df_boxplot, on='name', how='outer')

    merged.to_csv(outfile, index=False)

if __name__ == "__main__":
    infile_heatmap = "/home/zz/Work/data/amazon/labelled/stats/stats_dist_rating.csv"
    infile_boxplot = "/home/zz/Work/data/amazon/labelled/stats/stats_descriptive_rating.json"
    outfile = "/home/zz/Work/data/amazon/labelled/stats/stats_joined_rating.csv"
    join_boxplot_heatmap_data(infile_boxplot,infile_heatmap, outfile)

    infile_heatmap = "/home/zz/Work/data/amazon/labelled/stats/stats_dist_words.csv"
    infile_boxplot = "/home/zz/Work/data/amazon/labelled/stats/stats_descriptive_words.json"
    outfile = "/home/zz/Work/data/amazon/labelled/stats/stats_joined_length.csv"
    join_boxplot_heatmap_data(infile_boxplot, infile_heatmap, outfile)



