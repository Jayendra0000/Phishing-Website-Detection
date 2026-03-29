import pandas as pd

# Load datasets
phishing = pd.read_csv("dataset/processed/phishtank_clean.csv")
legitimate = pd.read_csv("dataset/processed/legitimate.csv")

# Keep only required columns
phishing = phishing[["url", "label"]]
legitimate = legitimate[["url", "label"]]

# Combine
full_df = pd.concat([phishing, legitimate], ignore_index=True)

# Shuffle data
full_df = full_df.sample(frac=1, random_state=42).reset_index(drop=True)

# Save final dataset
full_df.to_csv("dataset/processed/full_dataset.csv", index=False)

print("✅ Dataset merged successfully")
print("Total URLs:", len(full_df))
print("Phishing:", sum(full_df["label"] == 1))
print("Legitimate:", sum(full_df["label"] == 0))
