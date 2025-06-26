import pandas as pd
import os

# Get root directory (one level up from /src/)
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname('DS'), '..'))

# Define raw/processed paths
RAW_DATA_DIR = os.path.join(PROJECT_ROOT, 'data', 'raw')
PROCESSED_DATA_DIR = os.path.join(PROJECT_ROOT, 'data', 'processed')

# Define filenames
zusatz_file = os.path.join(RAW_DATA_DIR, "Zusatzbeitrag_je Kasse je Quartal.xlsx")
markt_file = os.path.join(RAW_DATA_DIR, "Marktanteile je Kasse.xlsx")
morbidity_file = os.path.join(RAW_DATA_DIR, "Morbidity_Region.xlsx")
kunden_2023_file = os.path.join(RAW_DATA_DIR, "Kundenmonitor_GKV_2023.xlsx")
kunden_2024_file = os.path.join(RAW_DATA_DIR, "Kundenmonitor_GKV_2024.xlsx")

# Load datasets
zusatz_df = pd.read_excel(zusatz_file)
markt_df = pd.read_excel(markt_file, sheet_name="data")
morbidity_df = pd.read_excel(morbidity_file)
kunden_2023 = pd.read_excel(kunden_2023_file)
kunden_2024 = pd.read_excel(kunden_2024_file)

# Fund name normalization
def clean_name(name):
    return name.strip().lower().replace("-", "").replace("/", "")

zusatz_df["kasse_clean"] = zusatz_df["Krankenkasse"].apply(clean_name)
markt_df["kasse_clean"] = markt_df["Krankenkasse"].apply(clean_name)
morbidity_df["kasse_clean"] = morbidity_df["Krankenkasse"].str.strip().str.lower()

# Standardize column names
zusatz_df.columns = zusatz_df.columns.str.strip().str.lower()
markt_df.columns = markt_df.columns.str.strip().str.lower()
morbidity_df.columns = morbidity_df.columns.str.strip().str.lower()
kunden_2023.columns = kunden_2023.columns.str.strip()
kunden_2024.columns = kunden_2024.columns.str.strip()

# Merge zusatz and markt data
merged_df = pd.merge(zusatz_df, markt_df, on=["jahr", "kasse_clean"], how="left")

# Sort by fund, year, and quarter
merged_df = merged_df.sort_values(by=["kasse_clean", "jahr", "quartal"])

# Lagged insured & churn rate
merged_df["insured_lag"] = merged_df.groupby("kasse_clean")["versicherte"].shift(1)
merged_df["churn_rate"] = (merged_df["insured_lag"] - merged_df["versicherte"]) / merged_df["insured_lag"]

# Lagged contribution and treatment flag
merged_df["zusatzbeitrag_lag"] = merged_df.groupby("kasse_clean")["zusatzbeitrag"].shift(1)
merged_df["treatment_flag"] = merged_df["zusatzbeitrag"] > merged_df["zusatzbeitrag_lag"]

# Merge with morbidity data
merged_df = pd.merge(
    merged_df,
    morbidity_df[["jahr", "kasse_clean", "risikofaktor"]],
    on=["jahr", "kasse_clean"],
    how="left"
)
merged_df.rename(columns={"risikofaktor": "morbidity_index"}, inplace=True)

# Clean and combine Kundenmonitor data
fund_col = 'Mitglied/Kunde einer Krankenkasse/Krankenversicherung'
kunden_2023["kasse_clean"] = kunden_2023[fund_col].str.lower().str.strip()
kunden_2024["kasse_clean"] = kunden_2024[fund_col].str.lower().str.strip()
kunden_2023["jahr"] = 2023
kunden_2024["jahr"] = 2024
kunden_df = pd.concat([kunden_2023, kunden_2024], ignore_index=True)

# Merge Kundenmonitor data
merged_df = pd.merge(merged_df, kunden_df, on=["jahr", "kasse_clean"], how="left")

# Sort again after merging
merged_df = merged_df.sort_values(by=["kasse_clean", "jahr", "quartal"])

# Recalculate churn-related variables after merge
merged_df["insured_lag"] = merged_df.groupby("kasse_clean")["versicherte"].shift(1)
merged_df["churn_rate"] = (merged_df["insured_lag"] - merged_df["versicherte"]) / merged_df["insured_lag"]
merged_df["zusatzbeitrag_lag"] = merged_df.groupby("kasse_clean")["zusatzbeitrag"].shift(1)
merged_df["treatment_flag"] = merged_df["zusatzbeitrag"] > merged_df["zusatzbeitrag_lag"]

# Add average zusatzbeitrag by period
period_avg = merged_df.groupby(["jahr", "quartal"])["zusatzbeitrag"].mean().reset_index()
merged_df = pd.merge(merged_df, period_avg, on=["jahr", "quartal"], how="left", suffixes=("", "_avg"))

# Drop rows with missing values in key columns
merged_df = merged_df.dropna(subset=["insured_lag", "zusatzbeitrag_lag", "churn_rate"])

# Save processed file
final_output_path = os.path.join(PROCESSED_DATA_DIR, "merged_panel_clean_data.csv")
merged_df.to_csv(final_output_path, index=False)

print(f"✅ Data preprocessing complete.\nSaved cleaned file to: {final_output_path}")
