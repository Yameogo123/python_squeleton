import pandas as pd
from {{ cookiecutter.package_name }}.utils.logger import logger
from {{ cookiecutter.package_name }}.utils.utils import are_df_columns

from autots import AutoTS

def time_series_automl(df:pd.DataFrame, date:str):
    if not are_df_columns(df, [date]):
        raise ValueError(f"Target column {date} not found in the dataframe")
    df[date] = pd.to_datetime(df[date])
    df0 = df.set_index(date)
    model_list = ['ARIMA', 'ETS', 'Prophet', 'SeasonalNaive']
    logger.info("Running AutoTS")
    model = AutoTS(
        forecast_length=12,  model_list=model_list,
        max_generations=2, num_validations=2, verbose=0           
    )
    model.fit(df0)
    bstname = model.best_model_name
    logger.info(f"Best model found: {bstname}")
    return model.best_model