# MultiGenoNexus: A Tool for Exploring Genetic Landscapes for Bulk RNA-Seq using ML

MultiGenoNexus is a Python-based tool designed for exploring genetic landscapes using bulk RNA-Seq data. This project leverages machine learning models to analyze and gain insights from RNA-Seq data.

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [R Program](#r-program)
- [Contribution](#contribution)
- [License](#license)

## Introduction
MultiGenoNexus aims to facilitate the analysis of bulk RNA-Seq data by providing a streamlined pipeline for data cleaning, normalization, and analysis using machine learning techniques. This tool is especially useful for researchers looking to uncover patterns and insights in genetic data from cancer studies.

## Features
- **Remove low counts and NA values**: Cleans the dataset by removing low-expression genes and missing values.
- **Data normalization**: Normalizes the RNA-Seq data to prepare it for downstream analysis.
- **Machine learning analysis**: Applies machine learning models to explore and interpret the genetic landscape.
- **Visualizations**: Generates visualizations to aid in the interpretation of results.

## Installation
To set up this project, ensure you have Python 3.7 or later installed, whilst the project was setup and run using Python 12.1. 
Follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/ChemBioAI/MultiGenoNexus
   cd MultiGenoNexus
   ```

2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
### Step 1: Preprocessing
Run the `preprocessing.py` script to clean and normalize your data. Ensure you have the counts data and metadata downloaded from the provided link.
   ```bash
   python preprocessing.py
   ```

### Step 2: Log2 Fold Change Calculation
Run the `log2foldchange.py` script to calculate the log2 fold changes. This step requires the `merged_final.csv` generated from the preprocessing step. Alternatively, you can download this file from the provided link.
   ```bash
   python log2foldchange.py
   ```

### Step 3: Z-Score Upsampling
Run the `zscore_upsampling.py` script to perform Z-score normalization and upsampling. This also requires the `merged_final.csv` from the previous step, which can be downloaded if needed.
   ```bash
   python zscore_upsampling.py
   ```
#### Link to Datasets: https://doi.org/10.6084/m9.figshare.25843819.v3

## R Program
The analysis workflow includes data cleaning steps such as removing low count reads and handling NA values, followed by differential expression analysis using DESeq2. DESeq2 normalizes the data, identifies the top significant genes, and exports lists of upregulated and downregulated genes to Excel sheets.

## Contribution
Contributions are welcome! If you have any ideas, suggestions, or bug fixes, please open an issue or submit a pull request. 

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

For further details and updates, please visit our [GitHub repository](https://github.com/ChemBioAI/MultiGenoNexus).
