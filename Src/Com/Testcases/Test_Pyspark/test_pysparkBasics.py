from pyspark import SparkContext
import os, logging, pytest

logging.basicConfig(level=logging.INFO)

class xTest_PySparkBasics:
    
    @classmethod
    def setup_class(self):
        self.sc = SparkContext()
        txtFilePath = os.path.join(os.getcwd(),"..\\TestFiles\\ReadFile.txt")
        ActualPath = os.path.normpath(txtFilePath)
        logging.info(ActualPath)
        self.rDD = self.sc.textFile(ActualPath)
    
    def test_py(self):
        logging.info("In Test_py")
        data = self.rDD.collect()
        logging.info(data)
        tt = self.rDD.flatMap(lambda name:name.split('\t')).collect()
        logging.info(tt)
#         d = tt.reduce(lambda name:name==20)
#         logging.info(d)

    def test_aggregate(self):
        seqOp = (lambda x, y: (x[0] + y, x[1] + 1))
        combOp = (lambda x, y: (x[0] + y[0], x[1] + y[1]))
        d1 = self.sc.parallelize([1, 2, 3, 4]).aggregate((0, 0), seqOp, combOp)
        logging.info(d1)
        d2 = self.sc.parallelize([1, 2, 3, 4]).aggregate((0, 0), seqOp, combOp)
        logging.info(d2)
        
    def test_value(self):
        xx = ['big','small', 'able', 'about', 'hairdresser', 'laboratory']
        l = list(map(lambda x: len(x),xx))
        logging.info("Inside test_value")
        logging.info(l)
    
    def test_words(self):
        sentence = "Dis-moi ce que tu manges, je te dirai ce que tu es."
#         num = list(map(lambda x:x.split(" "),sentence))
        num = sentence.split(" ")
        logging.info("Inside test_words")
        logging.info(num)
        logging.info(len(num))
        
    def test_toughWay(self):
        import string
        from functools import reduce
        sentence = "Dis-moi ce que tu manges, je te dirai ce que tu es."
        no_punctuation=sentence.translate(str.maketrans("","",string.punctuation))
        logging.info(no_punctuation)
        xx = reduce(lambda x,y: x+y, map(lambda x: 1, no_punctuation.split()))
        logging.info("Inside test_toughWay")
        logging.info(xx)
        
