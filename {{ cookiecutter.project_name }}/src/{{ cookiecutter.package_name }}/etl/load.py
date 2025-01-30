from dagster import op, AssetMaterialization, MetadataValue, Out
from {{ cookiecutter.package_name }}.utils.logger import logger
import os 

PROCESSSED_PATH = os.path.join("..", "data", "processed")

@op(out=Out(is_required=False))
def save_data(context, dataframes: dict):
    output_path = PROCESSSED_PATH
    for df_name, df in dataframes.items():
        context.log.info(f"Saved processed data to {df_name}")
        logger.info(f"Saved processed data to {df_name}")
        df.to_parquet(output_path+"/"+df_name+".parquet")
        # Log an asset materialization
        yield AssetMaterialization(
            asset_key="processed_data",
            description="Processed data saved to parquet",
            metadata={
                "output_path": MetadataValue.path(output_path),
                "num_rows": MetadataValue.int(len(df)),
            },
        )
