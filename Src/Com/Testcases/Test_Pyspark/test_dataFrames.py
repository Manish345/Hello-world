from pyspark import SparkContext
from pyspark.sql import SQLContext
from Src.Com.ConstantsFile import Constants
import logging, os
from pyspark.sql import Row

class Test_dataFrames:
    
    def setup_class(self):
        self.sc = SparkContext()
        self.sqlCon = SQLContext(self.sc)
    
    def test_RDD(self):
        ''' If want to replace String None value then put None without quotes
        If want to replace int then put 'null' or 'None' or '' '''
        namesList = [('Ajay', 34), ('Vijay', 24), (None, 30), ('Ram', 'None'), (None, '')]
#         namesList = [('null', 'null'), ('null', 'null'), ('null', 'null'), ('null', 'null'), ('null', 'null')]
        eRDD = self.sc.parallelize(namesList)
        logging.info("Inside test_RDD")
        logging.info(type(eRDD))
        mapRDD = eRDD.map(lambda x: Row(name=x[0], age=x[1]))
#         DataFrame = self.sqlCon.createDataFrame(eRDD, ['name', 'age'])
        DataFrame = self.sqlCon.createDataFrame(mapRDD)
        logging.info(type(DataFrame))
        logging.info(DataFrame.collect())
        logging.info("DataFrame Dropna function")
        pp = DataFrame.dropna()
        logging.info(type(pp))
        pp.show()
        DataFrame.printSchema()
        logging.info("fillna Dataframe")
        ppp = DataFrame.fillna(4)
        ppp.show()
        pppp = ppp.fillna("Raj")
#         logging.info(ppp.type())
        pppp.show()
    
    def test_CSV(self):
        csvFilePath = os.path.join(os.getcwd(),"..\\TestFiles\\ReadCSV.csv")
#         CsvLoad = SQLContext.DataFrameReader.load(self,path=csvFilePath, header=True, inferSchema=True)
#         CsvLoad = SQLContext.read.load(path=csvFilePath, header=True, inferSchema=True)
#         CsvLoad = (SQLContext.read\
#          .format("csv")\
#          .option("header", "true")\
#          .load(csvFilePath))
#         CsvLoad.printSchema()
#         df = SQLContext.load(self,source="com.databricks.spark.csv", header="true", path = csvFilePath)
#         df = SQLContext.read.load(source="com.databricks.spark.csv", header="true", path = csvFilePath)
        rDD = self.sc.textFile(csvFilePath)
        mapCSV = rDD.map(lambda y: y.split(","))
        logging.info(mapCSV.collect())
        mapCSV1 = mapCSV.map(lambda x: Row(name=x[0], age=x[1]))
        logging.info(type(mapCSV1))
        CSvLoad = self.sqlCon.createDataFrame(mapCSV1)
        logging.info(type(CSvLoad))
        logging.info(CSvLoad.collect())
        CSvLoad.printSchema()
        logging.info(CSvLoad.head(5))
        CSvLoad.show(3, truncate=True)
        logging.info(CSvLoad.count())
        CSvLoad.describe().show()
        CSvLoad.describe('name').show(4, truncate=True)
        logging.info(CSvLoad.columns)
        logging.info(len(CSvLoad.columns))
        CSvLoad.select('name').show(2, truncate=True)
        logging.info(CSvLoad.distinct().count())
        CSvLoad.distinct().show()
        CSvLoad.select('age').distinct().show()
        CSvLoad.crosstab('name', 'age').show()
        CSvLoad.crosstab('age', 'name').show()
        CSvLoad.show()
        pp = CSvLoad.dropna()
        logging.info("CSVLoad Dropna")
        logging.info(type(pp))
        pp.show()
        newDataframe = CSvLoad.dropDuplicates()
        newDataframe.show()
        logging.info(type(newDataframe))
        p = newDataframe.select('age').dropna()
        logging.info("Type of p:")
        logging.info(type(p))
        logging.info(p.count())
        p.show()
        CSvLoad.fillna({'name':'Raj','age':"2"}).show()
        logging.info("Aggregate of dataframe")
        meanDataframe = CSvLoad.groupBy('age').agg({'age':'mean'}).show()
        CSvLoad.groupBy('name').count().show()
        CSvLoad.groupBy('name').sum().show()
#         CSvLoad.groupBy('name').avg('age').show()
#         CSvLoad.groupBy('name').max('age').show()
        CSvLoad.groupBy('name').agg({'age':'mean'}).show()
        CSvLoad.groupBy('name').agg({'age':'max'}).show()
        
        
        
        