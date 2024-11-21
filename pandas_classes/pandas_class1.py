import pandas as pd

import numpy as np
import pandas as pd

# 1. Generate random data using NumPy
np.random.seed(42)
data = np.random.randint(1, 101, (10, 3))  # 10 rows, 3 columns of random integers between 1 and 100

# 2. Create a pandas DataFrame
df = pd.DataFrame(data, columns=["Math", "Science", "English"])

