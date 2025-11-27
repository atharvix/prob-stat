"""using varnish.csv do  Draw a scatter plot to verify that it is reasonable to assume that the relationship is 
parabolic.  
b) Fit a second-degree polynomial by the method of least squares (curvilinear regression).  
c) Use the result of part (b) to predict the drying time of the varnish when 6.5 grams of the 
additive is being used."""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data = pd.read_csv("varnish.csv")
x = data["Additive"]
y = data["DryingTime"]
plt.scatter(x, y, color='blue', label='Data Points')
plt.xlabel("Additive (grams)")
plt.ylabel("Drying Time (minutes)")
plt.title("Scatter Plot of Drying Time vs Additive")
plt.legend()
plt.show()
# Fit a second-degree polynomial (quadratic) using numpy's polyfit
coefficients = np.polyfit(x, y, 2)
a, b, c = coefficients
print(f"Fitted quadratic equation: Drying Time = {a}*Additive^2 + {b}*Additive + {c}")
# Predict the drying time when 6.5 grams of additive is used
additive_amount = 6.5
predicted_drying_time = a * (additive_amount ** 2) + b * additive_amount + c
print(f"Predicted drying time for {additive_amount} grams of additive: {predicted_drying_time} minutes")
x_fit = np.linspace(min(x), max(x), 100)
y_fit = a * (x_fit ** 2) + b * x_fit + c
plt.scatter(x, y, color='blue', label='Data Points')
plt.plot(x_fit, y_fit, color='red', label='Fitted Quadratic Curve')
plt.xlabel("Additive (grams)")
plt.ylabel("Drying Time (minutes)")
plt.title("Fitted Quadratic Curve for Drying Time vs Additive")
plt.legend()
plt.show()
