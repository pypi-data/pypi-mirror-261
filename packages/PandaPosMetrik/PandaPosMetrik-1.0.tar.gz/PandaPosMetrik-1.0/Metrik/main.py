from utils.sql_helper import SQLHelper

sqlHelper = SQLHelper("127.0.0.1", 1433, "PandaBOS", "SQL Server")

print(sqlHelper.get_tickets())