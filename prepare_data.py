import pandas as pd

# Load all three files explicitly
df0 = pd.read_csv("data/daily_sales_data_0.csv")
df1 = pd.read_csv("data/daily_sales_data_1.csv")
df2 = pd.read_csv("data/daily_sales_data_2.csv")

# Combine them
df = pd.concat([df0, df1, df2], ignore_index=True)

# Keep only Pink Morsels (safe version)
df = df[df["product"].str.strip().str.lower() == "pink morsel"].copy()

# Clean price (remove $ if present)
df["price"] = df["price"].replace(r"[\$,]", "", regex=True).astype(float)

# Create Sales column
df["Sales"] = df["quantity"] * df["price"]

# Keep required columns
df = df[["Sales", "date", "region"]]

# Rename columns
df.columns = ["Sales", "Date", "Region"]

# Save output
df.to_csv("formatted_output.csv", index=False)

print("formatted_output.csv created")