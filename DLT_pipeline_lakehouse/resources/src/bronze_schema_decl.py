from pyspark.sql.types import *

cust_info_schema = StructType([
    StructField("cst_id",IntegerType(),False),
    StructField("cst_key",StringType(),False),
    StructField("cst_firstname",StringType(),True),
    StructField("cst_lastname",StringType(),True),
    StructField("cst_marital_status",StringType(),True),
    StructField("cst_gndr",StringType(),True),
    StructField("cst_create_date",DateType(),True)
])

prd_info_schema = StructType([
    StructField("prd_id",IntegerType(),False),
    StructField("prd_key",StringType(),False),
    StructField("prd_nm",StringType(),True),
    StructField("prd_cost",IntegerType(),True),
    StructField("prd_line",StringType(),True),
    StructField("prd_start_dt",TimestampType(),True),
    StructField("prd_end_dt",TimestampType(),True)
])

sales_details_schema = StructType([
    StructField("sls_ord_num",StringType(),False),
    StructField("sls_prd_key",StringType(),False),
    StructField("sls_cust_id",IntegerType(),False),
    StructField("sls_order_dt",IntegerType(),True),
    StructField("sls_ship_dt",IntegerType(),True),
    StructField("sls_due_dt",IntegerType(),True),
    StructField("sls_sales",IntegerType(),True),
    StructField("sls_quantity",IntegerType(),True),
    StructField("sls_price",IntegerType(),True)
])


erp_loc_a101_schema = StructType([
    StructField("cid",StringType(),False),
    StructField("cntry",StringType(),True)
])

erp_cust_az12_schema = StructType([
    StructField("cid",StringType(),False),
    StructField("bdate",DateType(),True),
    StructField("gen",StringType(),True)
])

erp_px_cat_g1v2_schema = StructType([
    StructField("id",StringType(),False),
    StructField("cat",StringType(),True),
    StructField("subcat",StringType(),True),
    StructField("maintenance",StringType(),True)
])