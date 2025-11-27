import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv("temp.csv")
temp = data["Temperature"]
press = data["Pressure"]
plt.scatter(temp, press)
plt.xlabel("Temperature (°C)")
plt.ylabel("Pressure")
plt.title("Scatter Plot of Pressure vs Temperature")
plt.show()
sdata = data.sort_values(by="Temperature")
plt.plot(sdata["Temperature"], sdata["Pressure"], marker='o')
plt.xlabel("Temperature (°C)")
plt.ylabel("Pressure")
plt.title("Line Graph of Pressure over Temperature")
plt.show()
plt.boxplot(press, vert=False)
plt.ylabel("Pressure")
plt.title("Boxplot of Pressure")
plt.show()
m_press = sum(press) / len(press)
spr = press.sort_values().reset_index(drop=True)
n = len(spr)
if n % 2 == 0:
    med_press = (spr[n//2 - 1] + spr[n//2]) / 2
else:
    med_press = spr[n//2]
mode_press = spr.mode()[0]
var = sum((press - m_press) ** 2) / n
std_dev = var ** 0.5
skew= (sum((press - m_press) ** 3) / n) / (std_dev ** 3)
print("Mean Pressure: ", m_press)
print("Median Pressure: ", med_press)
print("Mode Pressure: ", mode_press)
print("Standard Deviation of Pressure: ", std_dev)
print("Skewness of Pressure: ", skew)
