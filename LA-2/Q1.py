import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv("cdata.csv")
chil = data["Children"]
m_chil = sum(chil)/len(chil)
med_chil = chil[len(chil)//2]
print("Mean of children: ",m_chil)
print("Median of children: ",med_chil)
print("Mode of children: ",chil.mode()[0])
plt.bar(data["Month"],chil)
plt.xlabel("Month")
plt.ylabel("Number of Children")
plt.title("Number of Children Born Each Month")
plt.show()


