#  Seaborn Data Analysis — Penguins & Tips Datasets

This project demonstrates **data analysis and visualization using Seaborn, Pandas, Matplotlib, and NumPy**.  
It includes two example scripts:
- **Correlation Heatmap of Penguin Features**
- **Restaurant Tips Data Analysis**

---

##  Project Overview

### 1️ Penguins Dataset Analysis
The `penguins_analysis.py` script:
- Loads the **Penguins** dataset from Seaborn.
- Selects only numeric features.
- Computes the **correlation matrix**.
- Visualizes correlations using a **heatmap**.
- Automatically identifies the **strongest correlation pair** among all numerical variables.

####  Key Learnings
- Understanding correlation between numerical variables.
- Using `sns.heatmap()` for visual representation.
- Using NumPy to find maximum correlation values programmatically.

---

### 2️ Tips Dataset Analysis
The `tips_analysis.py` script:
- Loads the **Tips** dataset from Seaborn.
- Calculates:
  - **Average total bill** by `day` and `time`.
  - **Maximum tip** by `smoker` status.
- Visualizes both results using **bar charts**.

####  Key Learnings
- Grouping and aggregating data using `pandas.groupby()`.
- Customizing bar plots using Seaborn (`hue`, `palette`, labels, titles).
- Understanding real-world restaurant data insights.

---

## 🛠️ Requirements

Make sure you have Python installed (3.8 or above).  
Then install the required libraries:

```bash
pip install seaborn pandas matplotlib numpy
