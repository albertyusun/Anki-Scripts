import pandas as pd


def convert(filename):
    pd.set_option("display.max_rows", None, "display.max_columns", None)
    df = pd.read_csv(filename)
    ret = pd.DataFrame()
    ret["write"] = "<p>{{c1::" + df['Chinese'] + "}}<br>" + \
                  "{{c2::" + df['Pinyin'] + "}}"
    ret["definition"] = "<p>"+ df['Chinese'] + "<br>"+ \
                       "{{c1::" + df['English Definition'] + "}}</p>"
    # ret["write"].append(ret["definition"])
    ret = pd.melt(ret)
    ret = ret.drop(columns=['variable'])
    ret = ret.dropna()
    ret.to_csv('new.csv')



if __name__ == "__main__":
    convert('week7.csv')