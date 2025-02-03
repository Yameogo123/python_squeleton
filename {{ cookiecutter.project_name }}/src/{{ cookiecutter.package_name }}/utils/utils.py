
import pandas as pd

def are_df_columns(df:pd.DataFrame, columns:list):
    return set(columns).issubset(df.columns)


def execute_script(function, message:str="erreur de script: ", *args, **kwargs):
    try:
        return function(*args, **kwargs)  
    except Exception as e:
        raise ValueError(f"{message}: {e}")  
