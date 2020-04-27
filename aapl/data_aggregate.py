import pandas as pd
import matplotlib.pyplot as plt

# all csv files created by datareader_pandas.py
df_aapl = pd.read_csv('aapl2.csv')
df_msft = pd.read_csv('msft.csv')
df_ge = pd.read_csv('ge.csv')
df_ual = pd.read_csv('ual.csv')
df_pep = pd.read_csv('pep.csv')
df_dal = pd.read_csv('dal.csv')
df_ibm = pd.read_csv('ibm.csv')
df_ko = pd.read_csv('ko.csv')

#close_px = pd.concat([pd.DataFrame(df_aapl[['Date','Close']]).rename(columns={'Close':'AAPL'}),pd.DataFrame(df_msft[['Date','Close']]).rename(columns={'Close':'MSFT'})], axis=1)  
#print(close_px)

# aggregate all stocks 'Close' column to one dataframe
# and rename column with Ticker
#merge AAPL and MSFT
close_px = pd.merge(pd.DataFrame(df_aapl[['Date','Close']]).rename(columns={'Close':'AAPL'}),
                    pd.DataFrame(df_msft[['Date','Close']]).rename(columns={'Close':'MSFT'}), how='outer')
#merge UAL and GE
temp_px = pd.merge(pd.DataFrame(df_ual[['Date','Close']]).rename(columns={'Close':'UAL'}),
                    pd.DataFrame(df_ge[['Date','Close']]).rename(columns={'Close':'GE'}), how='outer')
#print(temp_px)
close_px = pd.merge(close_px,temp_px, how='outer')
#print(close_px)
#merge PEP and DAL
temp_px = pd.merge(pd.DataFrame(df_pep[['Date','Close']]).rename(columns={'Close':'PEP'}),
                    pd.DataFrame(df_dal[['Date','Close']]).rename(columns={'Close':'DAL'}), how='outer')
#print(temp_px)
close_px = pd.merge(close_px,temp_px, how='outer')
#merge IBM and KO
temp_px = pd.merge(pd.DataFrame(df_ibm[['Date','Close']]).rename(columns={'Close':'IBM'}),
                    pd.DataFrame(df_ko[['Date','Close']]).rename(columns={'Close':'KO'}), how='outer')
#print(temp_px)
close_px = pd.merge(close_px,temp_px, how='outer')

close_px['Date'] = pd.to_datetime(close_px['Date'])
close_px.set_index(close_px['Date'],inplace=True)
close_px = close_px.drop(columns=['Date'])
print(close_px)

#save to file
#close_px.to_csv('close_px.csv')

#plot
close_px.plot()
plt.show()

#barplot volume for MSFT
df_msft['Date'] = pd.to_datetime(df_msft['Date'])
msft_volume = df_msft[['Date','Volume']]
msft_volume.set_index(msft_volume['Date'],inplace=True)
msft_volume = msft_volume.drop(columns=['Date'])

#plot the closing prices of AAPL
close_px['AAPL'].plot()
plt.show()
#plot the closing prices of MSFT
close_px['MSFT'].plot()
plt.show()
#plot MFST vs AAPL on the same chart
close_px[['MSFT','AAPL']].plot()
plt.show()

#plot the volume for MSFT
plt.bar(msft_volume.index,msft_volume['Volume'])  
plt.gcf().set_size_inches(15,8)
plt.show()

# multiplot
top = plt.subplot2grid((4,4), (0,0), rowspan=3, colspan=4)
top.plot(close_px['MSFT'].index, close_px['MSFT'], label='MSFT Close')
plt.title('MSFT Close Price 2012 - 2014')
plt.legend(loc=2)

bottom = plt.subplot2grid((4,4), (3,0), rowspan=1, colspan=4)
bottom.plot(msft_volume.index, msft_volume['Volume'])
plt.title('MSFT Trading Volume 2012 - 2014')
plt.subplots_adjust(hspace=0.75)
plt.gcf().set_size_inches(15,8)
plt.show()

#calculate daily percentage change
daily_pc = close_px / close_px.shift(1) - 1
#check the percentage on 2012-01-05
verif = close_px.loc['2012-01-05']['AAPL'] / close_px.loc['2012-01-04']['AAPL'] - 1
intable = daily_pc.loc['2012-01-05']['AAPL']
print(verif, intable)

#plot daily percentage change for AAPL
daily_pc['AAPL'].plot()
plt.title('Daily Percentage for AAPL')
plt.show()

#calculate daily cumulative return
daily_cr = (1 + daily_pc).cumprod()
print(daily_cr[:5])
#plot all the cumulative returns to get an idea
# of the relative performance of all the stocks
daily_cr.plot(figsize=(8,6))
plt.show()

#resample to end of month and forward fill values
monthly = close_px.asfreq('M').ffill()
print(monthly[:5])
#calculate the monthly percentage changes
monthly_pc = monthly / monthly.shift(1) - 1
print(monthly[:5])
#calculate monthly cumulative return
monthly_cr = (1 + monthly_pc).cumprod()
print(monthly[:5])
#plot monthly cumulative returns
monthly_cr.plot(figsize=(8,6))
plt.show()

#histogram of daily % change for AAPL
aapl = daily_pc['AAPL']
aapl.hist(bins=50);
plt.show()

#matrix of all stocks daily % changes histograms
daily_pc.hist(bins=50, figsize=(8,6));
plt.show()

# extract juts MSFT close
msft_close=close_px[['MSFT']]['MSFT']
#calculate the 30 and 90 day rolling means
ma_30 = msft_close.rolling(window=30).mean()
ma_90 = msft_close.rolling(window=90).mean()
#compose into a dataframe that can be plotted
result = pd.DataFrame({'Close': msft_close, '30_MA_Close': ma_30, '90_MA_Close': ma_90})
#plot all the series against each other
result.plot(title='MSFT Close Price')
plt.gcf().set_size_inches(12,8)
plt.show()

#plot the daily percentage change of MSFT vs AAPL
plt.scatter(daily_pc['MSFT'], daily_pc['AAPL'])
plt.xlabel('MSFT')
plt.ylabel('AAPL')
plt.show()

# calculate the correlation between all the stocks relative
# to daily precentage change
corrs = daily_pc.corr()
print(corrs)


#https://subscription.packtpub.com/book/big_data_and_business_intelligence/9781787123137/15/ch15lvl1sec134/determining-risk-relative-to-expected-returns
plt.scatter(daily_pc.mean(), daily_pc.std())
plt.xlabel('Expected returns')
plt.ylabel('Risk')

for label, x, y in zip(daily_pc.columns, daily_pc.mean(), daily_pc.std()):
    plt.annotate(
        label,
        xy = (x, y), xytext = (30, -30),
        textcoords = 'offset points', ha = 'right',
        va = 'bottom',
        bbox = dict(boxstyle = 'round, pad=0.5',
                    fc = 'yellow',
                    alpha = 0.5),
        arrowprops = dict(arrowstyle = '->',
                          connectionstyle = 'arc3, rad=0'))

plt.xlim(-0.001, 0.003)
plt.ylim(0.005, 0.0275)
plt.gcf().set_size_inches(8,8)
plt.show()