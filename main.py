import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("/Users/kevingarcia/Code/Coding projects/pandasPractice/student_spending.csv", delimiter = ",", header=0)
df.drop(columns=['Unnamed: 0', 'gender', 'preferred_payment_method'], inplace=True)


df.boxplot(column=['tuition', 'housing', 'food', 'books_supplies', 'transportation',
                     'entertainment', 'health_wellness', 'personal_care', 'technology', 'miscellaneous'], 
                     rot=45)
plt.title("Spending categories")
plt.ylabel("Monthly Spending ($)")
plt.tight_layout() 
plt.show()

# Group by academic year and average the relevant spending columns
yearlySpending = df.groupby("year_in_school")[[
    "tuition", "housing", "transportation", "books_supplies", "technology",
    "entertainment", "health_wellness", "personal_care", "miscellaneous"
]].mean()

df["totalSpending"] = df[[
    "tuition", "housing", "transportation", "books_supplies",
    "technology", "entertainment", "health_wellness",
    "personal_care", "miscellaneous"
]].sum(axis=1)
# Plotting the total spending by year in school
df['spendingRatio'] = df['totalSpending'] / (df['monthly_income'] + df['financial_aid'])

df = df. replace([np.inf, -np.inf], np.nan)
df.dropna(subset=['spendingRatio'], inplace=True)

orderedYears = ['Freshman', 'Sophomore', 'Junior', 'Senior'] 
spendingByYear = df.groupby("year_in_school")['spendingRatio'].mean().reindex(orderedYears)

# Plot average spending ratio by year in school
spendingByYear.plot(kind='bar', rot=0)
plt.title("Average Spending Ratio by Year in School")
plt.ylabel("Net Spending Ratio")
plt.tight_layout()
plt.show()
#plot average spending by major
df.groupby("major")[['technology', 'entertainment', 'books_supplies']].mean().plot(kind='bar', rot=45)
plt.title("Average Spending by Major")
plt.ylabel("Average monthly costs ($)")
plt.tight_layout()
plt.show()

# Plot average spending by major and year in school
df['year_in_school'] = pd.Categorical(df['year_in_school'], categories=orderedYears, ordered=True)

df.boxplot(column='spendingRatio', by='year_in_school', grid=False)
plt.title("Spending Ratio Distribution by Year in School")
plt.suptitle("")
plt.xlabel("Year in School")
plt.ylabel("Spending-to-Income Ratio")
plt.tight_layout()
plt.show()