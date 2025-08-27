from bronze_schema_decl import (cust_info_schema,prd_info_schema,sales_details_schema,erp_loc_a101_schema,erp_cust_az12_schema,erp_px_cat_g1v2_schema)
from parameters_decl import envs
from pyspark.sql.functions import *
from pyspark.sql.types import *
import dlt

env = "dev"
config = envs[env]

def create_bronze_tables(
    table_name: str,
    table_info: dict,
    env_dict: dict
):
    @dlt.table(
        name=f"{env_dict['catalog']}.{env_dict['bronze_schema']}.{table_name}",
        table_properties={"quality": table_info["quality"]}
    )
    def load_table():
        df = (
            spark.readStream
            .format(table_info.get("format", "cloudFiles"))
            .option("cloudFiles.format", table_info.get("format", "csv"))
            .option("cloudFiles.schemaLocation", f"{env_dict['schemaLocation']}/{table_name}")
            .option("pathGlobFilter", table_info["pattern"])
            .option("header", table_info.get("header", "true"))
            .option("delimiter", table_info.get("delimiter", ","))
            .schema(table_info["schema"])
            .load(f"{env_dict['source_path']}/{table_info['folder']}/")
        )
        df = df.withColumn("_ingest_start_date", current_timestamp()).withColumn("_ingest_end_date", current_timestamp())
        return df
    return load_table

for table_name, table_info in config.items():
    if table_name in [
        "format",
        "catalog",
        "bronze_schema",
        "silver_schema",
        "gold_schema",
        "schemaLocation",
        "source_path"
    ]:
        continue
    create_bronze_tables(table_name, table_info, config)