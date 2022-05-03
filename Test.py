# Databricks notebook source
# MAGIC %fs
# MAGIC 
# MAGIC ls s3://dsops-databucket/bronze/dsops_test/e2_test/dlt/cust-cluster-dlt/

# COMMAND ----------

# MAGIC %sql
# MAGIC 
# MAGIC show tables in dsops_bronze

# COMMAND ----------

# MAGIC %sh
# MAGIC 
# MAGIC ping 10.241.16.15

# COMMAND ----------

# MAGIC %sh
# MAGIC 
# MAGIC nc -zv oregon.cloud.databricks.com 443

# COMMAND ----------

# MAGIC %sh
# MAGIC 
# MAGIC traceroute oregon.cloud.databricks.com

# COMMAND ----------

# MAGIC %sh
# MAGIC 
# MAGIC nc -zv 10.241.16.15 22

# COMMAND ----------

# MAGIC %sh
# MAGIC 
# MAGIC ssh ec2-user@10.241.16.15 ec2-user

# COMMAND ----------

# MAGIC %fs
# MAGIC 
# MAGIC ls /databricks-datasets

# COMMAND ----------

# MAGIC %fs 
# MAGIC ls /databricks-datasets/learning-spark-v2/people/people-10m.delta

# COMMAND ----------

# MAGIC %sh
# MAGIC 
# MAGIC cat /dbfs/databricks-datasets/README.md

# COMMAND ----------



# COMMAND ----------

# MAGIC %sh
# MAGIC 
# MAGIC ping -c 4 mysql.hpc.biogen.com

# COMMAND ----------

# MAGIC %sh
# MAGIC nc -zv mysql.hpc.biogen.com 3306

# COMMAND ----------

# test
