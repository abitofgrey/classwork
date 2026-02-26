import pandas as pd
import numpy as np

def eda(df: pd.DataFrame) -> pd.DataFrame:
    
    """
    Do stat eval on dataframe
    
    Args:
        df (pd.DataFrame): Dataframe to evaluate
    Returns:
        pd.DataFrame: New Dataframe with column evals
    """
    
    data = []
    index = df.columns
    new_columns = [
        "is_numeric",
        "mean",
        "median",
        "min",
        "max",
        "range",
        "std",
        "num_na",
        "perc_na",
        "num_unique",
        "unique_vals"
        ]
    total_vals = len(df)
    for col in df.columns:
        num_na = df[col].isna().sum()
        perc_na = round(num_na / total_vals, 4)
        num_unique = df[col].nunique()
        if pd.api.types.is_numeric_dtype(df[col]):
            is_num = True
            mean = df[col].mean()
            median = df[col].median()
            min = df[col].min()
            max = df[col].max()
            rng = max - min
            std = round(df[col].std(), 4)
            unique_vals = np.nan
            row = [is_num, mean, median, min, max, rng, std, num_na, perc_na, num_unique, unique_vals]
            data.append(row)
        else:
            is_num = False
            mean = np.nan
            median = np.nan
            min = np.nan
            max = np.nan
            rng = np.nan
            std = np.nan
            unique_vals = df[col].unique() if num_unique < 8 else np.nan
            row = [is_num, mean, median, min, max, rng, std, num_na, perc_na, num_unique, unique_vals]
            data.append(row)
    new_df = pd.DataFrame(data = data, columns = new_columns, index = index)
    return new_df