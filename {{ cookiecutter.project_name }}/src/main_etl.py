# %% Import libraries
from {{ cookiecutter.package_name }}.utils.logger import logger
from {{ cookiecutter.package_name }}.etl.extract import load_data
from {{ cookiecutter.package_name }}.etl.transform import process_data
from {{ cookiecutter.package_name }}.etl.load import save_data
from dagster import job
import os

# Utiliser la fonction configurer_logger pour obtenir un logger configuré
logger.info("====================================")
logger.info("START the ETL script")


#%% Define main functions
@job
def main():

    # Load the data
    logger.info("Extract the data")
    dataframes = load_data()
    logger.info("Raw data transformed into parquet and saved in the data/interm folder") 
    
    # Make the pre-processing
    logger.info("Transform the data")
    dataframes = process_data(dataframes)
    
    # Train & Predict on your model
    logger.info("Load the data")
    save_data(dataframes)
    logger.info("Data saved in the data/processed folder")
    
    
    logger.info("END the ETL script")
    logger.info("====================================")
    
if __name__ == "__main__":
    result = main.execute_in_process()
    print("Pipeline execution result:", result.success)
    
