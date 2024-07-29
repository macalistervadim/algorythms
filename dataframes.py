"""
Табличная структура данных DataFrame
"""

import pandas as pd


df = pd.DataFrame([
    ["1", "Fares", 32, True],
    ["2", "Danek", 32, False],
    ["3", "Aleks", 20, True],
])

df.columns = ["id", "name", "age", "decision"]

print(df)