from dagster import op
import numpy as np
from {{ cookiecutter.package_name }}.utils.logger import logger


@op
def process_data(context, dataframes: dict):
    """
        Processes a dictionary of dataframes by applying a series of transformations.

        Args:
            context: The context object containing logging information.
            dataframes (dict): A dictionary where keys are dataframe names and values are pandas DataFrame objects.

        Returns:
            dict: A dictionary with the same keys as the input, where each DataFrame has been processed.

        Transformation steps:
            1. Fill NA values with NaN.
            2. Drop duplicate rows.
            3. Add a new column '_id_' with unique integer identifiers for each row.
    """
    # Example: Filter rows where the "value" column is greater than 50
    for df_name, df in dataframes.items():
        context.log.info(f"Transformation of {df_name}...")
        logger.info(f"Transformation of {df_name}...")
        # ADD YOUR TRANSFORMATION LOGIC HERE
        processed_df = df
        # 1. fill na values
        processed_df = processed_df.fillna(np.nan)
        # 2. drop duplicates
        processed_df = processed_df.drop_duplicates()
        # 3. add _id_ column
        processed_df['_id_'] = np.arange(len(processed_df))
        dataframes[df_name] = processed_df
    return dataframes