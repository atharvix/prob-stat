import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv("hw.csv")
h=data["Height"]
w=data["Width"]
n=len(h)
m_h=sum(h)/n
m_w=sum(w)/n
num_h=sum((w - m_w)*(h - m_h))
den_h=sum((w - m_w)**2)
b1_h=num_h/den_h
b0_h=m_h - b1_h*m_w
print("Least squares line for predicting height from width:")
print("\nHeight =", b0_h, "+", b1_h, "* Width")
num_w=sum((h - m_h)*(w - m_w))
den_w=sum((h - m_h)**2)
b1_w=num_w/den_w
b0_w=m_w - b1_w*m_h
print("\nLeast squares line for predicting width from height:")
print("\nWidth =", b0_w, "+", b1_w, "* Height")
plt.scatter(w, h, color='blue', label='Data Points')
x_vals = pd.Series([min(w), max(w)])
y_vals_h = b0_h + b1_h * x_vals
plt.plot(x_vals, y_vals_h, color='red', label='Height from Width')
y_vals_w = (x_vals - b0_w) / b1_w
plt.plot(y_vals_w, x_vals, color='green', label='Width from Height')
plt.xlabel("Width")
plt.ylabel("Height")
plt.title("Scatter Plot with Least Squares Lines")
plt.legend()
plt.show()