#transformation.py
from pyspark.sql import SparkSession

spark = SparkSession \
    .builder \
    .appName("My PySpark code") \
    .getOrCreate()


#convert and write csv to parquet
df_temp = spark.read.options(header='true', inferSchema='true').csv("gs://datafinalproject/INPUT/GlobalLandTemperaturesByCity.csv")
df_temp.write.mode("Overwrite").parquet("gs://datafinalproject/STAGING/globaltempbycity.parquet")

df_airport = spark.read.options(header='true', inferSchema='true').csv("gs://datafinalproject/INPUT/airport-codes_csv.csv")
df_airport.write.mode("Overwrite").parquet("gs://datafinalproject/STAGING/airportcodes.parquet")

df_immigration = spark.read.options(header='true', inferSchema='true').csv("gs://datafinalproject/INPUT/immigration_data_sample.csv")
df_immigration.write.mode("Overwrite").parquet("gs://datafinalproject/STAGING/immigration.parquet")

df_port = spark.read.options(header='true', inferSchema='true').csv("gs://datafinalproject/INPUT/USPORT.csv")
df_port.write.mode("Overwrite").parquet("gs://datafinalproject/STAGING/usport.parquet")

df_state = spark.read.options(header='true', inferSchema='true').csv("gs://datafinalproject/INPUT/USSTATE.csv")
df_state.write.mode("Overwrite").parquet("gs://datafinalproject/STAGING/usstate.parquet")

df_country = spark.read.options(header='true', inferSchema='true').csv("gs://datafinalproject/INPUT/USCOUNTRY.csv")
df_country.write.mode("Overwrite").parquet("gs://datafinalproject/STAGING/uscountry.parquet")

# The delimiter for this file (us-cities-demographics.csv) is semicolon (;)
# We have to change the default delimiter
df_demographic = spark.read.options(header="true", inferSchema="true", delimiter=";").csv("gs://datafinalproject/INPUT/us-cities-demographics.csv")
df_demographic.printSchema()
# There is a problem in Header of this df, 
# Therefore, we need to rename the header before write it into parquet file
# Header: City;State;Median Age;Male Population;Female Population;Total Population;Number of Veterans;Foreign-born;Average Household Size;State Code;Race;Count

# Rename all column names with new column names
demographic_new_col_names = ["City", "State", "MedianAge", "MalePopulation", "FemalePopulation", "TotalPopulation", "NumberOfVeterans", "ForeignBorn", "AverageHouseholdSize", "StateCode", "Race", "Count"]
df_demographic = df_demographic.toDF(*demographic_new_col_names)

# Then, we convert it into parquet
df_demographic.write.mode("Overwrite").parquet("gs://datafinalproject/STAGING/demographic.parquet")

