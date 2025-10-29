import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")


avg_bill = tips.groupby(['day', 'time'], as_index=False)['total_bill'].mean()
avg_bill.columns = ['day', 'time', 'avg_total_bill']

max_tip = tips.groupby('smoker', as_index=False)['tip'].max()
max_tip.columns = ['smoker', 'max_tip']

print("=== Average Total Bill by Day and Time ===")
print(avg_bill)
print("\n=== Maximum Tip by Smoker Status ===")
print(max_tip)

plt.figure(figsize=(8, 5))
sns.barplot(data=avg_bill, x='day', y='avg_total_bill', hue='time')
plt.title("Average Total Bill by Day and Time")
plt.xlabel("Day of Week")
plt.ylabel("Average Total Bill ($)")
plt.tight_layout()
sns.set_style("dark")
plt.show()

plt.figure(figsize=(5, 4))
sns.barplot(data=max_tip, x='smoker', y='max_tip',hue='smoker', palette='cividis',legend=False)
plt.title("Maximum Tip by Smoker Status")
plt.xlabel("Smoker")
plt.ylabel("Maximum Tip ($)")
plt.tight_layout()
sns.set_style("dark")
plt.show()
