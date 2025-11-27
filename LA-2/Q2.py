import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv("age.csv")
l = data["Lower"]
u = data["Upper"]
f = data["Frequency"]
mp = (l + u) / 2
n = sum(f)
mage = sum(mp * f) / n
cum_freq = []
total = 0
for freq in f:
    total += freq
    cum_freq.append(total)

half = n / 2
med=0
for i in range(len(cum_freq)):
    if cum_freq[i] >= half:
        med = i 
        break
L_m = l[med]
h= u[med] - l[med]
f_m = f[med]
cf_p= cum_freq[med - 1] if med != 0 else 0
median = L_m + ((half - cf_p) / f_m) * h
mod_i=0
max_freq = f[0]
for i in range(1, len(f)):
    if f[i] > max_freq:
        max_freq = f[i]
        mod_i = i
L_o = l[mod_i]
h= u[mod_i] - l[mod_i]
f_1 = f[mod_i]
f_0 = f[mod_i - 1] if mod_i != 0 else 0
f_2 = f[mod_i + 1] if mod_i != len(f) - 1 else 0
mode = L_o + ((f_1 - f_0) / ((f_1 - f_0) + (f_1 - f_2))) * h
print("Mean age: ", mage)
print("Median age: ", median)
print("Mode age: ", mode)
value = []
for i in range(len(f)):
    for j in range(f[i]):
        value.append(mp[i])
plt.hist(value, bins=len(l), edgecolor='black')
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.title("Age Distribution Histogram")
plt.show()