# https://pandas.pydata.org/docs/getting_started/intro_tutorials/03_subset_data.html

import pandas as pd
titanic = pd.read_csv("titanic.csv")
print(titanic)

print(titanic.info())

ages = titanic["Age"]
print(ages)

above_35 = titanic[titanic["Age"] > 35]
print(above_35)

class_23 = titanic[titanic["Pclass"].isin([2, 3])]
print(class_23)
class_23 = titanic[(titanic["Pclass"] == 2) | (titanic["Pclass"] == 3)]
print(class_23)

age_no_na = titanic[titanic["Age"].notna()]
print(age_no_na)

adult_names = titanic.loc[titanic["Age"] > 35, "Name"]
print(adult_names)

some_slice = titanic.iloc[9:25, 2:5]
print(some_slice)

titanic.iloc[0:3, 3] = "anonymous"
print(titanic.head().iloc[:,0:5])

# https://pandas.pydata.org/docs/getting_started/intro_tutorials/06_calculate_statistics.html

print(titanic["Age"].mean())

print(titanic[["Age", "Fare"]].median())

print(titanic[["Age", "Fare"]].describe())

agg = titanic.agg({'Age': ['min', 'max', 'median', 'skew'],
              'Fare': ['min', 'max', 'median', 'mean']})
print(agg)

print(titanic[["Sex", "Age"]].groupby("Sex").mean())

print(titanic.groupby("Sex").mean())

print(titanic.groupby("Sex")["Age"].mean())

print(titanic.groupby(["Sex", "Pclass"])["Fare"].mean())

print(titanic["Pclass"].value_counts())

print(titanic.groupby("Pclass")["Pclass"].count())