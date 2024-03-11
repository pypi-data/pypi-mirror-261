import pyodbc

from Metrik.models.Ticket import Tickets

class SQLHelper:
    def __init__(self, ip_address: str, port: str, db_name: str, driver: str):
        self.ip_address = ip_address
        self.port = port
        self.db_name = db_name
        self.driver = driver
        self.connection = pyodbc.connect(
            driver="{SQL Server}",
            database=self.db_name,
            server="LAPTOP-K3C6JQ36\\MSSQLPANDAPOS",
            user="sa",
            password="esat3535",
        )
    
    
    def get_tickets(self) -> list[Tickets]:
        tickets = Tickets.objects.all()
        return tickets
    
    
        
        
