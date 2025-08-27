from bronze_schema_decl import cust_info_schema, prd_info_schema, sales_details_schema, erp_loc_a101_schema, erp_cust_az12_schema, erp_px_cat_g1v2_schema

envs = {
"dev" : {
    "format": "cloudFiles",
    "catalog":"ete_catalog",
    "bronze_schema" : "ete_schema_bronze",
    "silver_schema" : "ete_schema_silver",
    "gold_schema" : "ete_schema_gold",
    "schemaLocation":"/Volumes/ete_catalog/ete_schema_bronze/ete_bronze_checkpoint",
    "source_path": "/Volumes/ete_catalog/ete_schema_source/ete_volume_source/",
    "crm_cust_info": {"schema": cust_info_schema, "pattern": "cust_info*.csv","quality":"bronze","format":"csv","header":"true","delimiter":",","folder":"source_crm"},
    "crm_prd_info": {"schema": prd_info_schema, "pattern": "prd_info*.csv","quality":"bronze","format":"csv","header":"true","delimiter":",","folder":"source_crm"},
    "crm_sales_details": {"schema": sales_details_schema, "pattern": "sales_details*.csv","quality":"bronze","format":"csv","header":"true","delimiter":",","folder":"source_crm"},
    "erp_loc_a101": {"schema": erp_loc_a101_schema, "pattern": "CUST_AZ12*.csv","quality":"bronze","format":"csv","header":"true","delimiter":",","folder":"source_erp"},
    "erp_cust_az12": {"schema": erp_cust_az12_schema, "pattern": "LOC_A101*.csv","quality":"bronze","format":"csv","header":"true","delimiter":",","folder":"source_erp"},
    "erp_px_cat_g1v2": {"schema": erp_px_cat_g1v2_schema, "pattern": "PX_CAT_G1V2*.csv","quality":"bronze","format":"csv","header":"true","delimiter":",","folder":"source_erp"}
    },


"qa" : {
    "format": "cloudFiles",
    "catalog":"ete_catalog",
    "bronze_schema" : "ete_schema_bronze",
    "silver_schema" : "ete_schema_silver",
    "gold_schema" : "ete_schema_gold",
    "schemaLocation":"/Volumes/ete_catalog/ete_schema_bronze/ete_bronze_checkpoint",
    "source_path": "/Volumes/ete_catalog/ete_schema_source/ete_volume_source/",
    "crm_cust_info": {"schema": cust_info_schema, "pattern": "cust_info*.csv","quality":"bronze","format":"csv","header":"true","delimiter":",","folder":"source_crm"},
    "crm_prd_info": {"schema": prd_info_schema, "pattern": "prd_info*.csv","quality":"bronze","format":"csv","header":"true","delimiter":",","folder":"source_crm"},
    "crm_sales_details": {"schema": sales_details_schema, "pattern": "sales_details*.csv","quality":"bronze","format":"csv","header":"true","delimiter":",","folder":"source_crm"},
    "erp_loc_a101": {"schema": erp_loc_a101_schema, "pattern": "CUST_AZ12*.csv","quality":"bronze","format":"csv","header":"true","delimiter":",","folder":"source_erp"},
    "erp_cust_az12": {"schema": erp_cust_az12_schema, "pattern": "LOC_A101*.csv","quality":"bronze","format":"csv","header":"true","delimiter":",","folder":"source_erp"},
    "erp_px_cat_g1v2": {"schema": erp_px_cat_g1v2_schema, "pattern": "PX_CAT_G1V2*.csv","quality":"bronze","format":"csv","header":"true","delimiter":",","folder":"source_erp"}
    },


"prod" : {
    "format": "cloudFiles",
    "catalog":"ete_catalog",
    "bronze_schema" : "ete_schema_bronze",
    "silver_schema" : "ete_schema_silver",
    "gold_schema" : "ete_schema_gold",
    "schemaLocation":"/Volumes/ete_catalog/ete_schema_bronze/ete_bronze_checkpoint",
    "source_path": "/Volumes/ete_catalog/ete_schema_source/ete_volume_source/",
    "crm_cust_info": {"schema": cust_info_schema, "pattern": "cust_info*.csv","quality":"bronze","format":"csv","header":"true","delimiter":",","folder":"source_crm"},
    "crm_prd_info": {"schema": prd_info_schema, "pattern": "prd_info*.csv","quality":"bronze","format":"csv","header":"true","delimiter":",","folder":"source_crm"},
    "crm_sales_details": {"schema": sales_details_schema, "pattern": "sales_details*.csv","quality":"bronze","format":"csv","header":"true","delimiter":",","folder":"source_crm"},
    "erp_loc_a101": {"schema": erp_loc_a101_schema, "pattern": "CUST_AZ12*.csv","quality":"bronze","format":"csv","header":"true","delimiter":",","folder":"source_erp"},
    "erp_cust_az12": {"schema": erp_cust_az12_schema, "pattern": "LOC_A101*.csv","quality":"bronze","format":"csv","header":"true","delimiter":",","folder":"source_erp"},
    "erp_px_cat_g1v2": {"schema": erp_px_cat_g1v2_schema, "pattern": "PX_CAT_G1V2*.csv","quality":"bronze","format":"csv","header":"true","delimiter":",","folder":"source_erp"}
    }
}