import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv("monthly_sales.csv")
s = data["Units"]
m= data["Month"]
m_s = sum(s)/len(s)
med_s = s[len(s)//2]
mode_s = s.mode()[0]
mean_dev = sum(abs(s - m_s)) / len(s)
print("Mean sales: ", m_s)
print("Median sales: ", med_s)
print("Mode sales: ", mode_s)
print("Mean Deviation : ", mean_dev)
plt.bar(m, s)
plt.xlabel("Month")
plt.ylabel("Sales")
plt.title("Monthly Sales")
plt.show()
