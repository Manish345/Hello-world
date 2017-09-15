import pytest
import logging
# from logging import basicConfig

handler = logging.basicConfig(level=logging.INFO)
class Test_Rough1:
    
#     def setUp(self):
#         logging.basicConfig(level=logging.INFO)
    
    def test_1(self):
#         print("Hello")
        logging.info("Hello")
        logging.info("Helloooo")
        
    def test_2(self):
        logging.basicConfig(level=logging.DEBUG)
        logging.info("Successful")
        assert 1==2



# if __name__=="__main__":
#     pytest.main(['-m','Test_Rough'])
     
    
    