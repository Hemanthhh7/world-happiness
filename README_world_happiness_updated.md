# Statistical Analysis of World Happiness

This project analyses World Happiness Report data from 2011 to 2017 using Python. It explores the distribution of national happiness scores, the relationship between GDP per capita and happiness, and correlations between happiness and selected social and economic factors.

## Project contents

| File | Description |
|---|---|
| `World_Happiness_Analysis.ipynb` | Google Colab/Jupyter notebook containing the analysis, statistical calculations and visualisations. |
| `analysis.py` | Python script for running the statistical analysis. |
| `requirements.txt` | Python libraries required to run the project. |
| `world_happiness_report_2018-Table2.1[1].csv` | CSV dataset used for the analysis. |
| `world_happiness_report_2018.xls` | Excel version of the World Happiness Report 2018 data. |

## Analysis performed

### 1. Distribution of national happiness scores

A histogram with a KDE curve is used to examine the distribution of Life Ladder scores from 2011 to 2017. The plot also marks the sample mean and median. Descriptive statistics include the count, mean, median, standard deviation, quartiles, minimum and maximum values, and skewness.

### 2. GDP per capita and happiness

A scatter plot compares log GDP per capita with the Life Ladder happiness score. A fitted linear regression line is included. The analysis reports the regression slope, Pearson correlation coefficient (r), coefficient of determination (R²), and number of complete observations.

### 3. Correlation analysis

A Pearson correlation matrix examines the relationships between happiness and the following factors:

- Life Ladder score
- Log GDP per capita
- Social support
- Healthy life expectancy at birth
- Freedom to make life choices
- Generosity
- Perceptions of corruption

The heatmap displays the lower triangle, including the diagonal, to make the correlation values easier to read.

## Tools and libraries

- Python
- Google Colab / Jupyter Notebook
- pandas
- NumPy
- Matplotlib
- Seaborn
- SciPy

## How to run the project

### Option 1: Google Colab

1. Open `World_Happiness_Analysis.ipynb` in Google Colab.
2. Upload the notebook and the CSV dataset to the Colab session, if they are not already available.
3. If the notebook reads the dataset from a local file, make sure the filename in the code matches `world_happiness_report_2018-Table2.1[1].csv`.
4. Select **Runtime → Run all**.
5. The notebook will display the statistical outputs and the three plots.

### Option 2: Run locally

1. Clone or download this repository.
2. Install the required libraries:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the Python script:

   ```bash
   python analysis.py
   ```

4. Keep the dataset file in the same working directory as the script, and ensure the code uses the correct CSV filename.

## Dataset and reference

The repository includes CSV and Excel files named for the *World Happiness Report 2018*. The analysis described in this project focuses on country-year observations from 2011 to 2017.

Reference:

Helliwell, J. F., Layard, R. and Sachs, J. (eds.) (2018). *World Happiness Report 2018*. The dataset files included in this repository are provided for the project analysis.

## Notes

- The number of observations can differ between analyses because some variables contain missing values.
- The correlation and regression results describe associations; they do not establish causation.
- The notebook and Python script should use the same dataset and year filter to keep the reported results consistent.
