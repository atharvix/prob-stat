##a) Construct line graphs for boiling points and barometric pressure. 
##b) Calculate the mean values. 
##c) Compute the standard deviations of the two data sets. 
##d) Which set of devices is better and why?
import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv("devices.csv")
d1=data[data["Device"]==1]
d2=data[data["Device"]==2]
t1=list(d1["Tbp"])
t2=list(d2["Tbp"])
p1=list(d1["Pressure"])
p2=list(d2["Pressure"])
plt.figure(figsize=(10,5))
plt.plot(t1, label="Device 1 Boiling Points")
plt.plot(t2, label="Device 2 Boiling Points")
plt.xlabel("Measurement Index")
plt.ylabel("Boiling Points")
plt.title("Boiling Points of Two Devices")
plt.legend()
plt.show()
plt.figure(figsize=(10,5))
plt.plot(p1, label="Device 1 Pressure", color='orange')
plt.plot(p2, label="Device 2 Pressure", color='green')
plt.xlabel("observation Index")
plt.ylabel("Barometric Pressure")
plt.title("Barometric Pressure of Two Devices")
plt.legend()
plt.show()
m_t1 = sum(t1) / len(t1)
m_t2 = sum(t2) / len(t2)
m_p1 = sum(p1) / len(p1)
m_p2 = sum(p2) / len(p2)
var_t1 = sum((x - m_t1) ** 2 for x in t1) / len(t1)
var_t2 = sum((x - m_t2) ** 2 for x in t2) / len(t2)
var_p1 = sum((x - m_p1) ** 2 for x in p1) / len(p1)
var_p2 = sum((x - m_p2) ** 2 for x in p2) / len(p2)
std_t1 = var_t1 ** 0.5
std_t2 = var_t2 ** 0.5
std_p1 = var_p1 ** 0.5
std_p2 = var_p2 ** 0.5
print("Device 1 Mean Boiling Point: ", m_t1)
print("Device 2 Mean Boiling Point: ", m_t2)
print("Device 1 Mean Pressure: ", m_p1)
print("Device 2 Mean Pressure: ", m_p2)
print("Device 1 Std Dev of Boiling Point: ", std_t1)
print("Device 2 Std Dev of Boiling Point: ", std_t2)
print("Device 1 Std Dev of Pressure: ", std_p1)
print("Device 2 Std Dev of Pressure: ", std_p2)
if std_t1 < std_t2 and std_p1 < std_p2:
    print("***Device 1 is better***")
else:
    print("***Device 2 is better***")
    
    





