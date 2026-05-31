import pandas as pd


print("Program Started")
# Load dataset
df = pd.read_csv("data/raw_data.csv")

print("Original Shape:", df.shape)

# Remove duplicate rows
df = df.drop_duplicates()

# Handle missing values
for col in df.select_dtypes(include='object').columns:
    df[col] = df[col].fillna(df[col].mode()[0])

for col in df.select_dtypes(include=['int64', 'float64']).columns:
    df[col] = df[col].fillna(df[col].median())

# Standardize text columns
for col in df.select_dtypes(include='object').columns:
    df[col] = df[col].str.strip().str.title()

# Remove extra spaces in column names
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

# Validate data types
print("\nData Types:")
print(df.dtypes)

# Save cleaned dataset
df.to_csv("data/cleaned_data.csv", index=False)

print("\nCleaning Completed Successfully!")
print("Cleaned Shape:", df.shape)