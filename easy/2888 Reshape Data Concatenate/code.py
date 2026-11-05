import pandas as pd


def concatenateTables(df1: pd.DataFrame, df2: pd.DataFrame) -> pd.DataFrame:
    return df1._append(df2)


data1 = {
    "student_id": [1, 2, 3, 4],
    "name": ["Mason", "Ava", "Taylor", "Georgia"],
    "age": [8, 6, 15, 17]
}

# Creating the second DataFrame
data2 = {
    "student_id": [5, 6],
    "name": ["Leo", "Alex"],
    "age": [7, 7]
}

print(concatenateTables(pd.DataFrame(data1), pd.DataFrame(data2)))
