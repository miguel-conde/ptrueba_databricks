# Databricks notebook source
# MAGIC %md
# MAGIC # Este es el primer nb

# COMMAND ----------

# MAGIC %load_ext autoreload
# MAGIC %autoreload 2

# COMMAND ----------

# Hello world!
print("Hello, world!")

# COMMAND ----------

df = spark.read.format("csv") \
    .option("header", "true") \
    .option("sep", ";") \
    .load("/Volumes/ml_workspace/default/my_sample_data/winequality-red.csv")
display(df)

# COMMAND ----------

df.columns

# COMMAND ----------

[x for x in list(dir(df)) if not x.startswith("_")]

# COMMAND ----------

from utils import common_fun

common_fun()

# COMMAND ----------

from libutils.utils import common_fun as lib_common_fun

lib_common_fun()

# COMMAND ----------

import inspect
import libutils.utils

functions_list = [func for func in dir(libutils.utils) if inspect.isfunction(getattr(libutils.utils, func))]
functions_list

# COMMAND ----------

from libutils.utils import compute_first_n_primes


# COMMAND ----------

# Now calling the function should work without errors
primes = compute_first_n_primes(101)
print(primes)
