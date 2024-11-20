import pandas as pd

import numpy as np
import pandas as pd

# 1. Generate random data using NumPy
np.random.seed(42)
data = np.random.randint(1, 101, (10, 3))  # 10 rows, 3 columns of random integers between 1 and 100

# 2. Create a pandas DataFrame
df = pd.DataFrame(data, columns=["Math", "Science", "English"])

# 3. Add a "Total" column
df["Total"] = df.sum(axis=1)

# 4. Add a "Grade" column based on conditions
df["Grade"] = np.where(df["Total"] >= 250, "A", 
              np.where(df["Total"] >= 200, "B", "C"))

# 5. Calculate subject-wise mean scores
subject_means = df[["Math", "Science", "English"]].mean()

# 6. Add a row for the subject means
df.loc["Mean"] = subject_means.append(pd.Series({"Total": df["Total"].mean(), "Grade": "N/A"}))

# 7. Filter rows for students with Grade "A"
grade_a_students = df[df["Grade"] == "A"]

# 8. Print results
print("Original DataFrame:\n", df)
print("\nStudents with Grade A:\n", grade_a_students)
print("\nSubject-Wise Means:\n", subject_means)
