import pandas as pd
import matplotlib.pyplot as plt


def make_autopct(values):
    def my_autopct(pct):
        total = sum(values)
        val = int(round(pct*total/100.0))
        return '{p:.1f}%  ({v:d})'.format(p=pct,v=val)
    return my_autopct


df = pd.read_excel(r'c:\Users\Nezhi\Desktop\Прога\Tinkoff\data_lesson_3.xls')

df = df.dropna()
df = df.reset_index(drop=True)

df['age'] = 0

for i in range(len(df)):
    df['age'][i] = 2019 - df['birth_dt'].dt.year[i]

age_values = {'Up to 25 years old' : 0, 'From 25 to 45 years old' : 0, 'From 45 to 65 years old' : 0, 'From 65 years old' : 0}
for i in range(len(df)):
    if df['age'][i] < 25:
        age_values['Up to 25 years old'] += 1
    elif df['age'][i] > 24 and df['age'][i] < 45:
        age_values['From 25 to 45 years old'] += 1
    elif df['age'][i] > 44 and df['age'][i] < 65:
        age_values['From 45 to 65 years old'] += 1
    else:
        age_values['From 65 years old'] += 1

fig, ax = plt.subplots(figsize=(20, 8))
colors = ['royalblue', 'orange', 'lightgreen', 'red']
plt.pie(age_values.values(), labels=age_values.keys(), colors=colors, autopct=make_autopct(age_values.values()), textprops={'fontsize': 14})
ax.set_title("Tinkoff Quest №2", fontsize=20, pad=60)
ax.set_xlabel("Conversion to disposal by age", fontsize=16, labelpad=50)
plt.axis('equal')
plt.show()
