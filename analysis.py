from pathlib import Path
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import linregress

DATA_URL = "https://raw.githubusercontent.com/VStanys/CSV-WHR/main/world-happiness-report.csv"
OUTPUT_DIR = Path("plots")
OUTPUT_DIR.mkdir(exist_ok=True)

df = pd.read_csv(DATA_URL)
df.columns = df.columns.str.strip()

required = [
    "year", "Ladder score", "Log GDP per capita", "Social support",
    "Healthy life expectancy at birth", "Freedom to make life choices",
    "Generosity", "Perceptions of corruption"
]
missing = [column for column in required if column not in df.columns]
if missing:
    raise ValueError(f"Dataset is missing required columns: {missing}")

# The supplied report's figures describe the 2011–2017 period.
df["year"] = pd.to_numeric(df["year"], errors="coerce")
analysis = df[df["year"].between(2011, 2017)].copy()

numeric_columns = required
for column in numeric_columns:
    analysis[column] = pd.to_numeric(analysis[column], errors="coerce")

print("Dataset shape:", df.shape)
print("Analysis period: 2011–2017")
print("Rows in selected period:", len(analysis))
print("\nHappiness score summary:")
print(analysis["Ladder score"].describe())
print("Mean:", round(analysis["Ladder score"].mean(), 3))
print("Median:", round(analysis["Ladder score"].median(), 3))

sns.set_theme(style="whitegrid")

# Figure 1: Distribution of national happiness scores
happiness = analysis["Ladder score"].dropna()
mean_score = happiness.mean()
median_score = happiness.median()

plt.figure(figsize=(9, 5.5))
sns.histplot(happiness, bins=25, kde=True, color="steelblue", edgecolor="white")
plt.axvline(mean_score, color="red", linestyle="--", linewidth=1.8,
            label=f"Mean = {mean_score:.2f}")
plt.axvline(median_score, color="black", linestyle=":", linewidth=1.8,
            label=f"Median = {median_score:.2f}")
plt.title("Distribution of National Happiness Scores (2011–2017)")
plt.xlabel("Life Ladder Score (0–10)")
plt.ylabel("Number of observations")
plt.legend()
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "figure_1_happiness_distribution.png", dpi=300)
plt.show()

# Figure 2: GDP per capita and happiness
scatter = analysis[["Log GDP per capita", "Ladder score"]].dropna()
reg = linregress(scatter["Log GDP per capita"], scatter["Ladder score"])
r_value = reg.rvalue
r_squared = r_value ** 2

plt.figure(figsize=(9, 5.5))
sns.regplot(
    data=scatter, x="Log GDP per capita", y="Ladder score",
    scatter_kws={"alpha": 0.45, "s": 22},
    line_kws={"color": "red", "linewidth": 2}
)
plt.title(
    f"GDP per Capita vs Happiness (r = {r_value:.3f}, R² = {r_squared:.3f})"
)
plt.xlabel("Log GDP per Capita")
plt.ylabel("Life Ladder Score (0–10)")
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "figure_2_gdp_vs_happiness.png", dpi=300)
plt.show()

print(f"Pearson correlation (GDP and happiness): {r_value:.3f}")
print(f"R-squared: {r_squared:.3f}")
print(f"Number of complete observations: {len(scatter)}")

# Figure 3: Correlation matrix
factor_columns = [
    "Ladder score",
    "Log GDP per capita",
    "Social support",
    "Healthy life expectancy at birth",
    "Freedom to make life choices",
    "Generosity",
    "Perceptions of corruption"
]
correlation = analysis[factor_columns].corr(method="pearson")

plt.figure(figsize=(10, 8))
sns.heatmap(
    correlation, annot=True, fmt=".2f", cmap="coolwarm",
    vmin=-1, vmax=1, center=0, square=True,
    linewidths=0.5, cbar_kws={"label": "Pearson correlation"}
)
plt.title("Correlation Between Happiness and Selected Factors (2011–2017)")
plt.xticks(rotation=45, ha="right")
plt.yticks(rotation=0)
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "figure_3_correlation_matrix.png", dpi=300)
plt.show()

print("\nCorrelation with happiness:")
print(correlation["Ladder score"].sort_values(ascending=False))
print("\nAnalysis complete. Figures saved in the plots/ folder.")
