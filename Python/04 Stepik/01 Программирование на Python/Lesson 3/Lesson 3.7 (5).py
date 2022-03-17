# Step 5
'''6	Вяххи	159
11	Федотов	172
7	Бондарев	158
6	Чайкина	153'''

# Solve 1 (my)
with open('dataset_3380_5.txt', 'r', encoding='UTF-8') as textfile:
    d={x:[0,0] for x in range(1,12)}
    for line in textfile.readlines():
       clss, name, height = line.strip().split('\t')
       d[int(clss)] = [d[int(clss)][0]+int(height),d[int(clss)][1]+1]
for k in d:
    print(k, float(d[k][0]/d[k][1])) if d[k][0] > 0 else print(k, '-')



# Solve 2 (from comments)
import pandas as pd

df = pd.read_table('dataset_3380_5.txt', header=None, sep=r'\s{1,}')
print(df.groupby(0).mean())

