#  Student Spending Analysis

This project analyzes how college students allocate their monthly budgets across key spending categories. The dataset comes from Kaggle and includes self-reported data on expenses, financial aid, and income.

---

## Objective

To uncover trends in student spending behavior:
- How do spending habits change by year in school (Freshman to Senior)?
- Do certain majors spend more on tech, books, or entertainment?
- What is the average spending-to-income ratio by year?

---

## Tools Used

- Python
- pandas
- matplotlib
- numpy

---

## What's Included

- Data cleaning (drop redundant columns, handle outliers)
- Total monthly spending calculation
- Spending-to-income ratio computed as:

  spendingRatio = Total Monthly Spending / (Monthly Income + Financial Aid)

- Visualizations:
  - Boxplots of spending categories
  - Bar charts of spending by major and year
  - Spending ratio distribution across academic years

---

## Key Insights

- **Sophomores** tend to overspend more relative to their available funds.
- **Freshmen** spend more on personal care early on, while **Seniors** show a spike again (possibly due to job interviews).
- Majors that are resource-heavy (like tech or design) have higher costs for **books** and **technology**.
