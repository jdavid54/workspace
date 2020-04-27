import pandas as pd
import matplotlib.pyplot as plt

import os

path = './'

files = []
# r=root, d=directories, f = files
for r, d, f in os.walk(path):
    for file in f:
        if '.csv' in file:
            files.append(os.path.join(r, file))

for f in files:
    print(f)
    df = pd.read_csv(f,sep=',')
    try:
        df.plot()
        plt.title(f)
        plt.show()
    except:
        print('No data in',f)