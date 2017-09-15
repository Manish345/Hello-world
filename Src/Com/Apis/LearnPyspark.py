import time
import pytest
from pyspark import SparkContext
from pyspark import SparkConf
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils


#===============================================================================
# sc = SparkContext(appName="Learn")
# rDD = sc.textFile("C:/Work/ReadFile.txt")
# print(rDD.first())
# print(rDD.collect())
# print(rDD.take(7))
# print(rDD.name())
# print(rDD.takeSample(False, 10, None))
# # print(rDD.count())
# c = rDD.map(lambda line:line.split(" "))
# print(c.collect())
# b = rDD.filter(lambda line: "m1" in line)
# print(b.count())
#===============================================================================

sc = SparkContext("local[2]","NetworkWordCount")
ssc = StreamingContext(sc, 1)
lines = ssc.socketTextStream("localhost", 9999)
words = lines.flatMap(lambda line:line.split(" "))
 
s = words.transform(lambda rdd: sc.parallelize(rdd.take(5)))
print(s)
# print(words)
pairs = words.map(lambda word: (word, 1))
wordCounts = pairs.reduceByKey(lambda x, y: x + y)
s = wordCounts.transform(lambda rdd: sc.parallelize(rdd.take(5)))
print(s)
print(wordCounts)
wordCounts.pprint(num=2)
# Print the first ten elements of each RDD generated in this DStream to the console
ssc.start()             # Start the computation
ssc.awaitTermination()



