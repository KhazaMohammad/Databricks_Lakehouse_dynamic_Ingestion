# Databricks_Lakehouse_dynamic_Ingestion  
Objective:  
The goal of this pipeline is to dynamically ingest multiple source datasets (e.g., sales transactions, customer info, product catalogs) into a Lakehouse architecture, starting with a Bronze layer for raw ingested data. The pipeline supports dynamic ingestion using Auto Loader and DLT, and allow config-driven creation of Bronze tables.  


<img width="1920" height="669" alt="image" src="https://github.com/user-attachments/assets/3b1b3422-4b74-4c55-8e94-8a1119a670c6" />

Key Advantages  
Dynamic ingestion: New datasets can be added by updating the config file.  
Automatic schema handling: Auto Loader handles schema evolution and inference.  
Scalable and reliable: DLT ensures exactly-once processing and maintains table lineage.  
Generic design: Reusable function reduces boilerplate code for each new dataset.  
