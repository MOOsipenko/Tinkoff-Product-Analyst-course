import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.dates import DateFormatter
import datetime as dt

df = pd.read_excel(r'c:\Users\Nezhi\Desktop\Прога\Tinkoff\data_lesson_3.xls')
df = df.sort_values(by=['reg_dttm'])

print(df)

new_df = df.iloc[:, 1:3]
new_df['reg_dttm'] = pd.to_datetime(new_df['reg_dttm']).dt.date
new_df['birth_year'] = pd.DatetimeIndex(df['birth_dt']).year

new_df['reg_dttm'] = new_df['reg_dttm'].apply(lambda x: dt.datetime.strftime(x, '%y-%m-%d'))
new_df['birth_dt'] = new_df['birth_dt'].apply(lambda x: dt.datetime.strftime(x, '%y-%m-%d'))
type(new_df['reg_dttm'])

new_df['birth_year'] = new_df.groupby(['reg_dttm']).transform('mean')

df['birth_year'] = new_df['birth_year'].round()

fig, ax = plt.subplots(figsize=(20, 8))

ax.scatter(df['reg_dttm'], df['birth_dt'].dt.year, color='orange', label="Distribution of birth years")
ax.plot(df['reg_dttm'], df['birth_year'], marker='o', markersize=4, label="Mean values of the birth years every registration date")

ax.set_title("Tinkoff Quest №1", fontsize=20, pad=60)
ax.set_xlabel("Registration Date", fontsize=14, labelpad=30)
ax.set_ylabel("Brith Date", fontsize=14, labelpad=30)

date_form_x = DateFormatter("%d-%m-%y")
ax.xaxis.set_major_formatter(date_form_x)
ax.xaxis.set_major_locator(mdates.WeekdayLocator(interval=1))
ax.set_yticks(np.arange(1950, 2005, 5))

ax.legend()
plt.show()
