import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style("darkgrid")

df = pd.read_csv("load_data.csv")

df_missions = df[df["ga:pagePathLevel1"].str.contains("/missions")]

df_missions["ga:pageLoadTime"] = df_missions["ga:pageLoadTime"]/1000

#df_missions.plot(style=".")

fig, ax = plt.subplots()

sns.distplot(df_missions["ga:pageLoadTime"], color="m", ax=ax, kde=False)

plt.ylabel("# of loads in a certain interval (bin)")
plt.xlabel("Load Time in Seconds")

ax.set_xlim(0, 150)

plt.title("GCconnex Career Marketplace load time distribution (n= "+ str(len(df_missions)) +")")

plt.show()