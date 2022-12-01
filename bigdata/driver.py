import os
from pyspark.conf import SparkConf
from pyspark.sql import SparkSession
from pyspark.sql.types import DecimalType
from pyspark.sql.window import Window
from pyspark.sql.functions import col

if __name__ == "__main__":
    spark = SparkSession.Builder().appName("abc").master("local[4]").getOrCreate()




    # print(dir(spark))
    # sc = spark.sparkContext
    # print(dir(sc))
    # rdd = sc.parallelize([1,2,3,4,5])
    # print(rdd.count())
    # df = spark.read.csv("D:\\Support\\snowflakedata\\PersonDemographics", header=True)
    # df.registerTempTable("tbl")
    # spark.sql("select * from tbl").show()

    df = spark.read.text("D:\\Support\\snowflakedata\\StateProvince").rdd
    print (df.take(10))
    # records_rdd = file_rdd.flatMap(parse_xml)
    # book_df = records_rdd.toDF(my_schema)
    # df = spark.read.csv('D:\\Support\\snowflakedata\\PersonDemographics', header=True)

    # df_gender  = df.filter(col('Gender') == 'M')
    #
    # df_final = df_gender.groupBy(col('MaritalStatus')).count()
    #
    # df_final.repartition(50).write.csv('D:\\Support\\snowflakedata\\PersonDemographics_output_50_file')

    # df.registerTempTable('tbl')

    # spark.sql(" select MaritalStatus, count(*) from (select * from tbl where gender = 'M') T group by T.MaritalStatus").show()