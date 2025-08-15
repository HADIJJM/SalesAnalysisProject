from pathlib import Path
import pandas as pd

# ======== Paths ========
DATA_DIR = Path("Data")
RAW_FILE = DATA_DIR / "raw" / "sales_data_sample.csv"
INTERIM_FILE = DATA_DIR / "interim" / "sales_data_proccess.csv"
FINAL_FILE = DATA_DIR / "processed" / "sales_data_final.csv"


# ======== Helpers ========
def check_file_exists(file_path: Path):
    """Check if file exists before processing."""
    if not file_path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")


# ======== Cleaning Functions ========
def load_data():
    """Load initial data from raw and save to interim."""
    check_file_exists(RAW_FILE)
    df = pd.read_csv(RAW_FILE, encoding="ISO-8859-1")
    
    # Create directories if they don't exist
    INTERIM_FILE.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(INTERIM_FILE, index=False)
    print(f"Original data loaded from '{RAW_FILE}' and saved to '{INTERIM_FILE}'.")
    return df


def clean_data():
    """Remove rows with missing values from interim file."""
    check_file_exists(INTERIM_FILE)
    df = pd.read_csv(INTERIM_FILE, encoding="ISO-8859-1")
    before = len(df)
    df.dropna(inplace=True)
    after = len(df)
    df.to_csv(INTERIM_FILE, index=False)
    print(f"Removed {before - after} rows with missing values." if before > after else "No missing values found.")


def remove_duplicates():
    """Remove duplicate rows from interim file."""
    check_file_exists(INTERIM_FILE)
    df = pd.read_csv(INTERIM_FILE, encoding="ISO-8859-1")
    before = len(df)
    df.drop_duplicates(inplace=True)
    after = len(df)
    df.to_csv(INTERIM_FILE, index=False)
    print(f"Removed {before - after} duplicate rows." if before > after else "No duplicate rows found.")


def strip_whitespace():
    """Remove leading/trailing whitespace from string columns in interim file."""
    check_file_exists(INTERIM_FILE)
    df = pd.read_csv(INTERIM_FILE, encoding="ISO-8859-1")
    for col in df.select_dtypes(include='object').columns:
        df[col] = df[col].str.strip()
    df.to_csv(INTERIM_FILE, index=False)
    print("Whitespace stripped from string columns.")


def create_date_column(year_col='YEAR_ID', month_col='MONTH_ID'):
    """Create a DATE column in interim file."""
    check_file_exists(INTERIM_FILE)
    df = pd.read_csv(INTERIM_FILE, encoding="ISO-8859-1")
    df['DATE'] = pd.to_datetime(df[year_col].astype(str) + '-' + df[month_col].astype(str) + '-01')
    df.to_csv(INTERIM_FILE, index=False)
    print("DATE column created and saved.")


def del_constant_col():
    """Delete constant columns from interim file."""
    check_file_exists(INTERIM_FILE)
    df = pd.read_csv(INTERIM_FILE, encoding="ISO-8859-1")
    constant_cols = [col for col in df.columns if df[col].nunique() == 1]
    if constant_cols:
        df.drop(columns=constant_cols, inplace=True)
        df.to_csv(INTERIM_FILE, index=False)
        print(f"Removed constant columns: {constant_cols}")
    else:
        print("No constant columns found.")


def finalize_data():
    """Save the final cleaned version to processed directory."""
    check_file_exists(INTERIM_FILE)
    df = pd.read_csv(INTERIM_FILE, encoding="ISO-8859-1")
    
    # Create processed directory if it doesn't exist
    FINAL_FILE.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(FINAL_FILE, index=False)
    print(f"Final cleaned data saved to '{FINAL_FILE}'.")


def all_clean_data():
    """Run all cleaning steps on sales data"""
    print("\n" + "="*50)
    print("STARTING DATA CLEANING PROCESS")
    print("="*50 + "\n")
    
    df = load_data()          # Load from raw to interim
    clean_data()              # Remove missing values
    remove_duplicates()       # Remove duplicate rows
    strip_whitespace()        # Remove extra spaces
    create_date_column()      # Create proper date columns
    del_constant_col()        # Remove constant columns
    finalize_data()           # Save final version to processed
    
    print("\n" + "="*50)
    print("CLEANING PROCESS COMPLETED")
    print("="*50)
    
    return pd.read_csv(FINAL_FILE, encoding="ISO-8859-1")