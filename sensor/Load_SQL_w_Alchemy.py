from sqlalchemy import create_engine
import pyodbc

server_name = "DESKTOP-0AQJLP0"
database_name = "TSQLV3"

#mssql_engine = create_engine("mssql://"+server_name+"/"+database_name+"?trusted_connection=yes", module_name="pyodbc")
#mssql_engine.table_names

### {Database Type}+{Database Connector}://{host}:{port}/{Database}?driver={Driver with spaces replaced with +}?TrustedConnection=yes
engine =  create_engine("mssql+pyodbc://127.0.0.1:1433/TSQLV3?driver=ODBC+Driver+17+for+SQL+Server?TrustedConnection=yes")
connection = engine.connect()
query = "SELECT TOP (10) [empid],[lastname],[firstname],[title] \
         FROM [TSQLV3].[HR].[Employees]"
result = connection.execute(query)
for row in result:
     print ("Name: {}".format(row["CompanyName"]))
result.close()
connection.close()