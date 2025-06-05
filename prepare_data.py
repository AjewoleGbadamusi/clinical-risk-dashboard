import pandas as pd

INPUT_FILE = "scan_results.csv"
CLEANED_FILE = "cleaned_scan_results.csv"
LOG_FILE = "skipped_rows_log.csv"


def main():
    try:
        df = pd.read_csv(INPUT_FILE)
    except FileNotFoundError:
        print(f"Input file {INPUT_FILE} not found.")
        return

    # Identify rows where Signal is missing or NaN
    missing_mask = df["Signal"].isna() | (df["Signal"].astype(str).str.strip() == "")
    skipped_rows = df[missing_mask].copy()
    cleaned_df = df[~missing_mask].copy()

    # Log skipped rows with reason
    if not skipped_rows.empty:
        skipped_rows["Reason Skipped"] = "Missing Signal Score"
        skipped_rows.to_csv(LOG_FILE, index=False)
    else:
        # If no skipped rows but log file exists, create empty log
        pd.DataFrame(columns=list(df.columns) + ["Reason Skipped"]).to_csv(LOG_FILE, index=False)

    # Save cleaned data
    cleaned_df.to_csv(CLEANED_FILE, index=False)
    print(f"Cleaned data written to {CLEANED_FILE}.")
    if not skipped_rows.empty:
        print(f"Skipped rows written to {LOG_FILE}.")


if __name__ == "__main__":
    main()
