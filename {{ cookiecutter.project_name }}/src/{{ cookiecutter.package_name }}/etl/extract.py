from dagster import op
from {{ cookiecutter.package_name }}.utils.reader import Reader
from {{ cookiecutter.package_name }}.utils.logger import logger
import os

RAW_PATH = os.path.join("..", "data", "raw")
INTERM_PATH = os.path.join("..", "data", "interm")

@op
def load_data(context):
    file_path = RAW_PATH
    output_path = INTERM_PATH
    context.log.info(f"Loaded data from {file_path}")
    logger.info(f"Loaded data from {file_path}")
    dataframes = Reader.read_all_files_in_directory(file_path)
    for df_name, df in dataframes.items():
        context.log.info(f"transformed {df_name} into parquet")
        logger.info(f"transformed {df_name} into parquet")
        df.to_parquet(output_path+"/"+df_name+".parquet")
    return dataframes