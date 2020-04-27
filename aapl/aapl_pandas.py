import pandas as pd
import matplotlib.pyplot as plt

aapl = pd.read_csv("aapl.csv")
aapl = aapl.reindex(aapl.index[::-1])
aapl = aapl.reset_index()
print(aapl)
aapl['Diff'] = aapl['Close'] - aapl['Open']

# plotting columns
aapl['Open'].head(100).plot()
aapl['Close'].head(100).plot()
plt.title('Open/Close')
plt.legend()
plt.show()

aapl['Volume'].head(100).plot()
plt.title('Volume')
plt.show()

aapl['Diff'].head(100).plot()
plt.show()

aapl['Pct_daily'] = aapl['Open']/aapl['Open'].shift(1)
