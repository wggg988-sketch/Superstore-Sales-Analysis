import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("https://raw.githubusercontent.com/nileshiq/SuperStore-Dataset-2019-2022/main/superstore_dataset.csv")

print(df.head())
print("Jami qatorlar:", len(df))

west = df[df["region"] == "West"]
print("West region:", len(west))
