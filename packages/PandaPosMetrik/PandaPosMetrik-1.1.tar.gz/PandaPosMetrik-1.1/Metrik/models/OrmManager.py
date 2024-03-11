import pyodbc

class OrmManager(object):
    def __get__(self, instance, owner):
        self.owner = owner
        self.connection = pyodbc.connect(
            driver="{SQL Server}",
            database="PandaBOS",
            server="LAPTOP-K3C6JQ36\\MSSQLPANDAPOS",
            user="sa",
            password="esat3535",
        )
        return self

    def create(self, **kwargs):
        cursor = self.connection.cursor()
        
        sql = f"""
        INSERT INTO {self.owner} ({', '.join(list(kwargs.keys()))}) VALUES ({', '.join(['?']*len(kwargs))})
        """
        
        
        cursor.execute(sql, list(kwargs.values()))
        cursor.commit()
        return self.owner(**kwargs)
    
    def all(self):
        cursor = self.connection.cursor()
        sql = f"SELECT * FROM {self.owner}"
        cursor.execute(sql)
        rows = [self.owner(**row) for row in cursor.fetchall()] #cursor.fetchall()
        return rows