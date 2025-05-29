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

- Spending-to-income ratios are **most variable for Juniors and Seniors**, who show more high-end outliers
- **Sophomores** tend to have a tighter and more consistent financial profile with fewer outliers
- **Freshmen and Seniors** spend more on personal care, possibly related to onboarding and career preparation
- Tech-related majors tend to invest more in **technology** and **books**
