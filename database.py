
import mysql.connector
class Crud:
    def __init__(self):
        self.__mydb = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "",
            database="mynewdb"
        )
        self.__mycursor = self.__mydb.cursor()
        
    def set_table(self,table):
        self.__table = table
        return self
        
    def read(self,sl = '*',where = None , order = 'id' , sort='ASC'):
        if where != None:
            sql = f"SELECT {sl} FROM {self.__table} WHERE {where[0]} = '{where[1]}' ORDER BY  {order} {sort}"
        else:
            sql = f"SELECT {sl} FROM {self.__table}  ORDER BY  {order} {sort}"
        print(sql)
        
        self.__mycursor.execute(sql)
        rs = self.__mycursor.fetchall()
        for x in rs:
            print(x)

 
   
    def insert(self,column_name,val):
        columns = "("
        for i in column_name:
            columns += i+ ' ,'
        else:
            columns = columns[:-1]
            columns+=")"
        print(columns)
        sql = f"INSERT INTO {self.__table} {columns}VALUES {val}"
        print(sql)
        self.__mycursor.execute(sql)
        self.__mydb.commit()
        print(self.__mycursor.rowcount,"record(s) affected .")
        
    def Update(self,col,where):
        sql = f"UPDATE {self.__table} SET {col[0]} = '{col[1]}' WHERE {where[0]}='{where[1]}'" 
        print(sql)
        self.__mycursor.execute(sql)
        self.__mydb.commit()
        print(self.__mycursor.rowcount,"record(s) affected ")
    
    def Del(self,valu):
        sql = f"DELETE FROM {self.__table} WHERE {valu[0]} = '{valu[1]}' "
        print(sql)
        self.__mycursor.execute(sql)
        self.__mydb.commit()
        print(self.__mycursor.rowcount,"record(s) deleted . ")
        
    def Order(self,col,ord):
        sql = f"SELECT {col} FROM esm ORDER BY {col} {ord}" 
        self.__mycursor.execute(sql)
        res = self.__mycursor.fetchall()
        for i in res:
            print(i)
    
    def Limit(self,n = '*'):
        sql = f"SELECT {n} FROM esm LIMIT 2 " 
        self.__mycursor.execute(sql)
        res = self.__mycursor.fetchall() 
        for i in res:
            print(i)   
            
obj = Crud()
obj.set_table("customers")
# col = ('id','1')
# where = ('id','33')
# obj.Update(col,where)
# valu = ('adress','tabriz')
# obj.Del(valu)




# value = "adress = 'shiraz'"
value = ['id' , '10']
obj.read( order='id',sort='DESC')
# col = ('name')
# ord = ('DESC')
# obj.Order(col,ord)
# n = ('name')
# obj.Limit(n)





# value = ('zahra','ahar')
# column_name = ('name','adress')
# obj.insert(column_name,value)
            
            