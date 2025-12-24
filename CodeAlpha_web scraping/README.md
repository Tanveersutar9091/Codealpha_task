**Titanic Data Analysis: Exploratory Data Analysis (EDA)**

This repository contains a comprehensive Exploratory Data Analysis (EDA) of the famous **Titanic Dataset**. The goal of this project is to explore the factors that influenced survival rates and to identify patterns, trends, and anomalies in the data.

**🎯 Objectives & Questions**

Before diving into the code, this analysis aims to answer:

- **Survival Demographics:** Did gender and passenger class significantly affect the chance of survival?
- **Age Impact:** Were children prioritized, or did age not play a significant role?
- **Data Integrity:** What percentage of data is missing, and how does it impact our analysis?
- **Financial Factors:** How did the ticket fare distribution look, and were there extreme outliers?

**🛠️ Tech Stack**

- **Python 3.x**
- **Pandas:** Data manipulation and cleaning.
- **Seaborn/Matplotlib:** Data visualization.
- **Numpy:** Numerical operations.

**📊 Key Findings**

**1\. The "Class" Effect**

There was a clear correlation between socio-economic status and survival. Passengers in **1st Class** had a much higher survival probability compared to those in 3rd Class.

**2\. Gender Patterns**

The "Women and Children First" policy is clearly reflected in the data. Female passengers across all classes had significantly higher survival rates than males.

**3\. Missing Data & Anomalies**

- **Missing Values:** The Age column has ~20% missing values, while the Deck column is missing over 75% of its data.
- **Outliers:** The Fare column contains several outliers, with some tickets costing over \$500, while the median fare was significantly lower.

**📈 Visualizations Included**

In this project, you will find:

- **Heatmaps:** To visualize missing data patterns and feature correlations.
- **Histograms/KDE Plots:** To observe age distributions among survivors.
- **Boxplots:** To detect price anomalies in fares.
- **Bar Plots:** To compare survival rates across categorical variables.
