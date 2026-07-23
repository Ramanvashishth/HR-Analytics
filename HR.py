# ============================================
# HR Analytics Project - Complete Source Code
# ============================================

# Step 1: Import Libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Step 2: Load Dataset
df = pd.read_excel("Book1.xlsx")

# Step 3: Remove Duplicate Records
df.drop_duplicates(inplace=True)

# Step 4: Check Missing Values
print("Missing Values:")
print(df.isnull().sum())

# ============================================
# Attrition Analysis
# ============================================

attrition_rate = df["Attrition"].value_counts(normalize=True) * 100

print("\nAttrition Rate (%):")
print(attrition_rate)

plt.figure(figsize=(6, 4))

df["Attrition"].value_counts().plot(
    kind="bar",
    color=["skyblue", "orange"]
)

plt.title("Attrition Distribution")
plt.xlabel("Attrition")
plt.ylabel("Employee Count")
plt.show()

# ============================================
# Department-wise Attrition
# ============================================

dept_attrition = pd.crosstab(
    df["Department"],
    df["Attrition"]
)

print("\nDepartment-wise Attrition:")
print(dept_attrition)

dept_attrition.plot(
    kind="bar",
    figsize=(8, 5)
)

plt.title("Department-wise Attrition")
plt.xlabel("Department")
plt.ylabel("Employee Count")
plt.show()

# ============================================
# Gender-wise Attrition
# ============================================

gender_attrition = pd.crosstab(
    df["Gender"],
    df["Attrition"]
)

print("\nGender-wise Attrition:")
print(gender_attrition)

gender_attrition.plot(
    kind="bar",
    figsize=(6, 4)
)

plt.title("Gender-wise Attrition")
plt.xlabel("Gender")
plt.ylabel("Employee Count")
plt.show()

# ============================================
# Job Role-wise Attrition
# ============================================

job_attrition = pd.crosstab(
    df["Job Role"],
    df["Attrition"]
)

print("\nJob Role Attrition:")
print(job_attrition)

job_attrition.plot(
    kind="bar",
    figsize=(12, 6)
)

plt.title("Job Role-wise Attrition")
plt.xlabel("Job Role")
plt.ylabel("Employee Count")
plt.xticks(rotation=45)
plt.show()

# ============================================
# Monthly Income vs Attrition
# ============================================

plt.figure(figsize=(8, 5))

df.boxplot(
    column="Monthly Income",
    by="Attrition"
)

plt.title("Monthly Income vs Attrition")
plt.suptitle("")
plt.xlabel("Attrition")
plt.ylabel("Monthly Income")
plt.show()

# ============================================
# Age Distribution by Attrition
# ============================================

plt.figure(figsize=(8, 5))

df.groupby("Attrition")["Age"].hist(
    alpha=0.6
)

plt.legend(["No", "Yes"])
plt.title("Age Distribution by Attrition")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.show()

# ============================================
# Overtime vs Attrition
# ============================================

overtime_attrition = pd.crosstab(
    df["Over Time"],
    df["Attrition"]
)

print("\nOvertime vs Attrition:")
print(overtime_attrition)

overtime_attrition.plot(
    kind="bar",
    figsize=(6, 4)
)

plt.title("Overtime Impact on Attrition")
plt.xlabel("Over Time")
plt.ylabel("Employee Count")
plt.show()

# ============================================
# Correlation Heatmap
# ============================================

numeric_df = df.select_dtypes(
    include=["int64", "float64"]
)

plt.figure(figsize=(15, 10))

sns.heatmap(
    numeric_df.corr(),
    cmap="coolwarm",
    annot=False
)

plt.title("Correlation Heatmap")
plt.show()

# ============================================
# Export Cleaned Dataset
# ============================================

df.to_csv(
    "HR_Analytics_Cleaned.csv",
    index=False
)

print("\nCSV Exported Successfully!")
