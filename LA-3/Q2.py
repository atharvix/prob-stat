import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv("emp.csv")
l = data["Lower"]
u = data["Upper"]
mp = (l + u) / 2
n = len(mp)
m_h = sum(mp) / n
mean_dev = sum(abs(mp - m_h)) / n
variance = sum((mp - m_h) ** 2) / n
std_dev = variance ** 0.5
print("Mean : ", m_h)
print("Mean Deviation : ", mean_dev)
print("Variance : ", variance)
print("Standard Deviation : ", std_dev)
plt.boxplot(mp, vert=False)
plt.xlabel("Working Hours")
plt.title("Boxplot of Monthly Working Hours")
plt.show()
