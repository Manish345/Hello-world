import pytest
import logging
import os
from Src.Com.Apis.RoughApi import RoughApiFile


handler = logging.basicConfig(level=logging.INFO)
class Test_Rough:
    
    def setup(self):
        logging.info("In SetUp function")
    
    def test_1(self):
        logging.info("In Test_1")
        
    def test_2(self):
        try:
            logging.basicConfig(level=logging.DEBUG)
            logging.info("In Test_2")
            assert 1==2
        except AssertionError:
            logging.info("Values are not equal")
            pytest.fail("Values are not equal",pytrace=False)
    
    def test_3(self):
        RoughApiFile().printFun()
        



# if __name__=="__main__":
#     pytest.main(['-m','Test_Rough'])
     
    
    