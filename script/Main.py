from clean import all_clean_data
from analysis import all_analysis

def main():
    # Step 1: Clean data
    df_clean = all_clean_data()
    
    # Step 2: Run all analyses
    all_analysis()

if __name__ == "__main__":
    main()