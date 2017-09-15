from pyspark import SparkContext


sc =  SparkContext()
print(sc.applicationId)
print(sc.startTime)
print(sc.sparkUser())
print("New")
myRDD = sc.parallelize(range(6), 6)
xx = sc.runJob(myRDD, lambda part: [x * x for x in part],allowLocal=False)
print(xx)
xx = sc.runJob(myRDD, lambda part: [x * x for x in part], [2,0,5], False)
print(xx)



# x = sc.parallelize([1,2,3,4,5], 6).glom()
# print(x.collect())
# x = sc.parallelize([('rat', 2), ('elephant', 1), ('cat', 2)])
# y = x.aggregate(0, lambda acc, value: acc + value[1], lambda acc1, acc2: acc1 + acc2)
# print(y)
# eRDD = sc.textFile("C:/Work/ReadFile.txt")
# print(eRDD.first())
# mapData = eRDD.map(lambda x:x.split('\t')).map(lambda x:(x[0],x[2],x[1]))
# print(mapData.collect())
# newData = mapData.map(lambda x: (int(x[2]),int(x[1]))).reduce(lambda x,y:((x[0]+y[0]),(x[1]+y[1])))
# print(newData)
# Avgg = (newData[0]/newData[1])*100
# print(Avgg)
# # SumCount = eRDD.map(lambda x:(x[1]+x[2]))
# # print(SumCount.collect())
# Agg = mapData.map(lambda x: (x[0],(x[1],x[2])))
# print(Agg.collect())
# # SumValues = Agg.aggregateByKey((0,0.0), (lambda x,y:(int(x[0])+int(y[0]),int(x[1])+1)),(lambda rdd1, rdd2: (int(rdd1[0])+int(rdd2[0]),int(rdd1[1])+int(rdd2[1]))))
# # print(SumValues.collect())
# 
# movie_counts = mapData.map(lambda x: (x[2], 1)).reduceByKey(lambda x,y:x+y)
# print(movie_counts.collect())
# 
# 
# print(sc.parallelize([1,2,4,6,2], 8).glom().collect())