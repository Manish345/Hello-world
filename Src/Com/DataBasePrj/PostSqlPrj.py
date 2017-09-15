''' In windows if want to switch to Postgresql user i.e. postgre superuser then use psql -U postgres command.
While want to create new database then use autocommit=True in pyodbc.connect() function 
'''

import psycopg2
import pyodbc
import subprocess
from pyodbc import DatabaseError

class DatabaseTests:
    
    def databaseConnection(self):
        try:
            self.con = pyodbc.connect(DRIVER='{PostgreSQL Unicode(x64)}',SERVER='localhost',DATABASE='testdb',USER='postgres', password='@India123@')
#             self.con = psycopg2.connect(host="localhost",database="testdb", user="postgres", password="@India123@")
#             self.con = pyodbc.connect(DRIVER='{PostgreSQL Unicode(x64)}',SERVER='localhost',DATABASE='testdb',USER='postgres', password='@India123@',autocommit=True)
            print("Database connection established")
            self.cur = self.con.cursor()
        except DatabaseError as e:
            print("Not able to connect to database")
            print(e)
    
    def databaseVersion(self):
        self.cur.execute("Select version()")
        print(self.cur.fetchone())
        
    def createNewDatabase(self):
        ''' add autocommit=True in pyodbc.connect() function while creating new databases''' 
        self.cur.execute("CREATE DATABASE suppliers;")
        
    def closeCursor(self):
        self.cur.close()
        print("Database Cursor closed")
        
    def closeConnection(self):
        self.con.close()
        print("Database Connection closed")
        
    def databaseCommit(self):
        self.cur.commit()
        self.con.commit()
        
    def executeCommands(self,databaseCommand):
        self.cur.execute(databaseCommand)
    
    def fetchDatabase(self):
        return self.cur.fetchone()
    
    def fetchAllDatabase(self):
        return self.cur.fetchall()
    
    def fetchTableAttributes(self):
        return self.cur.description
        
    def insertValues(self, Tablename, fields, values):
        DatabaseCommand = "INSERT INTO "+Tablename+fields+" VALUES"+values
        print("Database Command:",DatabaseCommand)
        self.cur.execute(DatabaseCommand)
        
if __name__ == "__main__":
    databaseObj = DatabaseTests()
    databaseObj.databaseConnection()
    databaseObj.databaseVersion()
#     databaseObj.createTable("CREATE TABLE vendors (\
#             vendor_id SERIAL PRIMARY KEY,\
#             vendor_name VARCHAR(255) NOT NULL)")
#     databaseObj.createTable("CREATE TABLE parts (\
#                 part_id SERIAL PRIMARY KEY,\
#                 part_name VARCHAR(255) NOT NULL)")
#     databaseObj.createTable("CREATE TABLE part_drawings (\
#                 part_id INTEGER PRIMARY KEY,\
#                 file_extension VARCHAR(5) NOT NULL,\
#                 drawing_data BYTEA NOT NULL,\
#                 FOREIGN KEY (part_id)\
#                 REFERENCES parts (part_id)\
#                 ON UPDATE CASCADE ON DELETE CASCADE)")
#     databaseObj.createTable("CREATE TABLE vendor_parts (\
#                 vendor_id INTEGER NOT NULL,\
#                 part_id INTEGER NOT NULL,\
#                 PRIMARY KEY (vendor_id , part_id),\
#                 FOREIGN KEY (vendor_id)\
#                     REFERENCES vendors (vendor_id)\
#                     ON UPDATE CASCADE ON DELETE CASCADE,\
#                 FOREIGN KEY (part_id)\
#                     REFERENCES parts (part_id)\
#                     ON UPDATE CASCADE ON DELETE CASCADE)")
#     databaseObj.databaseCommit()
#     databaseObj.insertValues("vendors","vendor_name","Ajay")
#     databaseObj.insertValues("parts","(part_id, part_name)","(5, 'Brakes')")
#     databaseObj.databaseCommit()
    databaseObj.executeCommands("select * from vendors")
#     Data = databaseObj.fetchDatabase()
#     print(Data)
    Data = databaseObj.fetchAllDatabase()
    print(Data)
#     Data = databaseObj.fetchTableAttributes()
    for column in Data:
        print(column[0])
    databaseObj.closeCursor()
    databaseObj.closeConnection()
    
    
    
    