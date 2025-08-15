# Sales Analysis Project

## Description
This project cleans and analyzes sales data. It handles missing values, removes duplicates, standardizes formats, and performs comprehensive analysis including sales trends, product performance, customer segmentation, and pricing analysis.

## Requirements
- Python 3.12+
- Pandas 2.3.1

## Installation
To get started with the project, follow these steps:

1. **Clone the repository:**
    ```bash
    git clone https://github.com/HADIJJM/SalesAnalysisProject.git
    cd SalesAnalysisProject
    ```

2. **Install dependencies:**
    The project uses a `requirements.txt` file to manage its dependencies.
    ```bash
    pip install -r requirements.txt
    ```

3. **Run the project:**
    To execute the data cleaning and analysis pipeline, run the main script.
    ```bash
    python main.py
    ```

## Project Structure
The repository is organized as follows:

SalesAnalysisProject/
├─ data/
│  ├─ raw/            # Original sales data
│  ├─ interim/        # Partially cleaned data
│  └─ processed/      # Final cleaned data
├─ clean.py           # Data cleaning functions
├─ analysis.py        # Analysis functions
├─ main.py            # Pipeline execution
├─ requirements.txt   # Python dependencies
├─ README.md          # Project description
└─ .gitignore         # Git ignore rules

## How It Works
* **`main.py`**: This is the entry point of the project. It orchestrates the entire workflow by calling functions from `clean.py` and `analysis.py`.
* **`clean.py`**: Contains all functions for data preprocessing including handling missing values, removing duplicates, standardizing formats, and optimizing dataset structure.
* **`analysis.py`**: Contains the core analysis functions which process the cleaned data to generate sales trends, product performance metrics, customer segmentation, and pricing insights.

## License
This project is licensed under the MIT License.
