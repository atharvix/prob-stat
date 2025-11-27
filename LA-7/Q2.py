import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv("sper.csv")
hours = data["Hours"]
test = data["Test"]
n = len(hours)
m_hours = sum(hours) / n
m_test = sum(test) / n
cov = sum((hours - m_hours) * (test - m_test)) / n
std_hours = (sum((hours - m_hours) ** 2) / n) ** 0.5
std_test = (sum((test - m_test) ** 2) / n) ** 0.5
pearson_corr = cov / (std_hours * std_test)
print("Pearson Correlation Coefficient between Hours and Test Scores: ", pearson_corr)
data['Hours_Rank'] = data['Hours'].rank()
data['Test_Rank'] = data['Test'].rank()
rank_hours = data["Hours_Rank"]
rank_test = data["Test_Rank"]
m_rank_hours = sum(rank_hours) / n
m_rank_test = sum(rank_test) / n
cov_rank = sum((rank_hours - m_rank_hours) * (rank_test - m_rank_test)) / n
std_rank_hours = (sum((rank_hours - m_rank_hours) ** 2) / n) ** 0.5
std_rank_test = (sum((rank_test - m_rank_test) ** 2) / n) ** 0.5
spearman_corr = cov_rank / (std_rank_hours * std_rank_test)
print("Spearman Correlation Coefficient between Hours and Test Scores: ", spearman_corr)
print("\nComparison:")
print("Pearson's correlation measures linear relationships, while Spearman's correlation measures monotonic relationships.")
print("Spearman's correlation is preferred when the data is ordinal, not normally distributed, or contains outliers.")
plt.scatter(hours, test, color='blue', label='Actual Data')
plt.xlabel("Hours Studied")
plt.ylabel("Test Score")
plt.title("Test Score vs Hours Studied")
plt.legend()
plt.show()
