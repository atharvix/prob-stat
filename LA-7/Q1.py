import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv("ye.csv")
y = data["Year"]
v = data["Import"]
n = len(y)
m_y = sum(y) / n
m_v = sum(v) / n
cov = sum((y - m_y) * (v - m_v)) / n
std_y = (sum((y - m_y) ** 2) / n) ** 0.5
std_v = (sum((v - m_v) ** 2) / n) ** 0.5
corr_coeff = cov / (std_y * std_v)
print("Correlation Coefficient between Year and Import Volume: ", corr_coeff)
b1 = cov / (std_y ** 2)
b0 = m_v - b1 * m_y
print("Least Squares Line: ")
print("Import = {:.2f} + {:.2f} * Year".format(b0, b1))
years_pred = [2019, 2020, 2021, 2022]
err = {}
for year in years_pred:
    pred_val = b0 + b1 * year
    actual_val = data.loc[data["Year"] == year, "Import"].values
    if len(actual_val) > 0:
        error = actual_val[0] - pred_val
        err[year] = error
    else:
        err[year] = None
print("Errors in Predicted Values for 2019-2022: ", err)
years_future = [2023, 2024, 2025]
pred = {}
for year in years_future:
    pred_val = b0 + b1 * year
    pred[year] = pred_val
print("Predicted Import Values for 2023-2025: ", pred)
plt.scatter(y, v, color='blue', label='Actual Data')
reg_line = b0 + b1 * y
plt.plot(y, reg_line, color='red', label='Regression Line')
plt.xlabel("Year")
plt.ylabel("Import Volume")
plt.title("Import Volume vs Year with Regression Line")
plt.legend()
plt.show()
