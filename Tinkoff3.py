import numpy as np
import pandas as pd
import matplotlib.pyplot as plt



df = pd.read_excel(r'c:\Users\Nezhi\Desktop\Прога\Tinkoff\data_lesson_3.xls')
df = df.dropna()
df = df.reset_index(drop=True)

df['conv_vel'] = (df['purchase_dt']-df['reg_dttm']).dt.days + 1
df['mean_purchase_amt'] = df.groupby(['conv_vel'])['purchase_amt'].transform('mean').round()
df = df.sort_values('conv_vel')

fig, ax = plt.subplots(figsize=(20, 8))

ax.scatter(df['conv_vel'], df['purchase_amt'], color='orange', label="Distribution of purchase amount over the conversion velocity")
ax.plot(df['conv_vel'], df['mean_purchase_amt'], marker='o', markersize=4, label="Mean values of the distribution of purchase amount over the conversion velocity")

ax.set_title("Tinkoff Quest №3", fontsize=20, pad=60)
ax.set_xlabel("Conversion velocity", fontsize=14, labelpad=30)
ax.set_ylabel("Purchase amount", fontsize=14, labelpad=30)

ax.set_xticks(np.arange(0, 100, 5))
ax.set_yticks(np.arange(0, 7500, 500))

ax.legend()
plt.show()
