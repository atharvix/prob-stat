import pandas as pd
from scipy import stats
data = pd.read_csv("height_weight.csv")
h = data["Height"]
w = data["Weight"]
m_h = sum(h)/len(h)
m_w = sum(w)/len(w)
med_h = h[len(h)//2]
med_w = w[len(w)//2]
print("Mean height: ", m_h)
print("Mean weight: ", m_w)
print("Median height: ", med_h)
print("Median weight: ", med_w)
print("Mode height: ", h.mode()[0])
print("Mode weight: ", w.mode()[0])

