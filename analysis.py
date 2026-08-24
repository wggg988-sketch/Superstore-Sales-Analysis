
!pip install pandas matplotlib seaborn -q

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


sns.set_theme(style="whitegrid")
plt.rcParams["figure.figsize"] = (10, 5)

# ======================
# 1. Datasetni yuklash
# ======================
url = "https://raw.githubusercontent.com/nileshiq/SuperStore-Dataset-2019-2022/main/superstore_dataset.csv"
df = pd.read_csv(url)

print("Dataset o'lchami:", df.shape)
print("\nUstunlar:", df.columns.tolist())
print("\nDastlabki 5 qator:")
display(df.head())


print("\n" + "="*40)
print("FILTR NATIJALARI")
print("="*40)

consumer = df[df["segment"] == "Consumer"]
west = df[df["region"] == "West"]
high_sales = df[df["sales"] > 500]
loss = df[df["profit"] < 0]
west_consumer = df[(df["region"] == "West") & (df["segment"] == "Consumer")]

print("Consumer segmenti:", len(consumer))
print("West region:", len(west))
print("Sales > 500:", len(high_sales))
print("Zarar ko'rganlar:", len(loss))
print("West + Consumer:", len(west_consumer))


# 1-grafik: Region bo'yicha Sales
plt.figure()
region_sales = df.groupby("region")["sales"].sum().sort_values(ascending=False)
sns.barplot(x=region_sales.index, y=region_sales.values, hue=region_sales.index, palette="viridis", legend=False)
plt.title("Region bo'yicha umumiy Sales", fontsize=14)
plt.ylabel("Sales ($)")
plt.show()

# 2-grafik: Category bo'yicha Profit
plt.figure()
cat_profit = df.groupby("category")["profit"].sum().sort_values(ascending=False)
sns.barplot(x=cat_profit.index, y=cat_profit.values, hue=cat_profit.index, palette="coolwarm", legend=False)
plt.title("Category bo'yicha umumiy Profit", fontsize=14)
plt.ylabel("Profit ($)")
plt.show()

# 3-grafik: Segment bo'yicha Sales (Pie)
plt.figure(figsize=(7,7))
segment_sales = df.groupby("segment")["sales"].sum()
plt.pie(segment_sales, labels=segment_sales.index, autopct="%1.1f%%", startangle=90)
plt.title("Segment bo'yicha Sales ulushi", fontsize=14)
plt.show()

print("\nTahlil tugadi!")
