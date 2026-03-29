import pandas as pd
from urllib.parse import unquote

# file is in the SAME folder as this script
df = pd.read_csv("phishtank_clean.csv")

df["url"] = df["url"].astype(str).apply(unquote)

df.to_csv("phishtank_clean.csv", index=False)

print("URLs decoded successfully")
