import pandas as pd
data = pd.read_csv("height_weight.csv")
print("Data Types:")
print(data.dtypes)
print("Variable Classification:")
for col in data.columns:
    dtype = data[col].dtype
    if dtype == 'object':
        print(col, ": Categorical")
    else:
        print(col, ": Continuous")
print("Dataset type:")
col=len(data.columns)
if col == 1:
    print("Univariate")
elif col == 2:
    print("Bivariate")
else:
    print("Multivariate")
    