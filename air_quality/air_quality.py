# https://pandas.pydata.org/docs/getting_started/intro_tutorials/04_plotting.html

import pandas as pd
import matplotlib.pyplot as plt

air_quality = pd.read_csv("air_quality_no2.csv", index_col=0, parse_dates=True)
print(air_quality)
'''
air_quality.plot()
plt.show()

air_quality["station_paris"].plot()
plt.show()


air_quality.plot.scatter(x="station_london", y="station_paris", alpha=0.5)
plt.show()

names = [method_name for method_name in dir(air_quality.plot) if not method_name.startswith("_")]
print(names)

air_quality.plot.box()
plt.show()

axs = air_quality.plot.area(figsize=(12, 4), subplots=True)
plt.show()

fig, axs = plt.subplots(figsize=(12, 4))        # Create an empty matplotlib Figure and Axes
air_quality.plot.area(ax=axs)                   # Use pandas to put the area plot on the prepared Figure/Axes
axs.set_ylabel("NO$_2$ concentration")          # Do any matplotlib customization you like
fig.savefig("no2_concentrations.png")           # Save the Figure/Axes using the existing matplotlib method.
plt.show()
'''
air_quality["london_mg_per_cubic"] = air_quality["station_london"] * 1.882
air_quality["ratio_paris_antwerp"] = \
        air_quality["station_paris"] / air_quality["station_antwerp"]

print(air_quality)
print(air_quality.info())

air_quality_renamed = air_quality.rename(
        columns={"station_antwerp": "BETR801",
                 "station_paris": "FR04014",
                 "station_london": "London Westminster"})

print(air_quality_renamed)
print(air_quality_renamed.info())

air_quality_renamed = air_quality_renamed.rename(columns=str.lower)
print(air_quality_renamed.info())