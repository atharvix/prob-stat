import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv("port.csv")
prices = data["Price"]
plt.scatter(range(len(prices)), prices)
plt.xlabel("Stock Index")
plt.ylabel("Stock Price")
plt.title("Scatter Plot of Stock Prices")
plt.show()
mprice = sum(prices) / len(prices)
sprices = prices.sort_values().reset_index(drop=True)
n = len(sprices)
if n % 2 == 0:
    medprice = (sprices[n//2 - 1] + sprices[n//2]) / 2
else:
    medprice = sprices[n//2]
var = sum((prices - mprice) ** 2) / n
std_dev = var ** 0.5
print("Mean : ", mprice)
print("Median : ", medprice)
print("Standard Deviation : ", std_dev)

