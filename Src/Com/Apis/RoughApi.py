import os, logging
handler = logging.basicConfig(level=logging.INFO)

class RoughApiFile:
    def printFun(self, hr=0):
        self.hr = 10
        logging.info("In Rough API")
        self.methodStatic()
    
    @staticmethod
    def methodStatic():
        print("Hello Static method")
        print(RoughApiFile.hr)
    
    @classmethod
    def methodClass(cls):
        print("Hello Class method")
        print(cls.printFun(cls))
        print("Val:")
        print(cls.hr)
        print("Done")

cl = RoughApiFile()
cl.methodStatic()
cl.methodClass()
        

s = "abcdefg"
print(s[::-1])
print(s[3:0:-1])
print(s[3::-2])

from functools import reduce

d = list(map(lambda x:x**x,(1,2,3)))
print(d)
dd = list(filter(lambda x: x>4, (3,5,8,2)))
print(dd)
ddd = reduce(lambda x,y:x+y, [2,4,7,5,2])
print(ddd)

l = [2,5,4,1,6,8,3,5]
ll = [x if x>3 else 10 for x in l]
print(ll)




