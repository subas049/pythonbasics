#import cx_Oracle
from sqlalchemy import create_engine
import pandas as pd


# Connection details
username = "testuser"      # database username
password = "demo1234"      # database password
host = "localhost"              # localhost
port = 1521                     # Oracle port
service_name = "orcl"           # service name

'''# Create a connection string for cx_Oracle
dsn = cx_Oracle.makedsn(host, port, service_name=service_name)

# Connect to the database for cx_Oracle
try:
    connection = cx_Oracle.connect(user=username, password=password, dsn=dsn)
    print("Database connection successful!")
except cx_Oracle.DatabaseError as e:
    print("There was an error connecting to the database:", e)'''

# Create the Oracle connection string
connection_string = f'oracle+cx_oracle://{username}:{password}@{host}:{port}/?service_name={service_name}'

# Create the SQLAlchemy engine
engine = create_engine(connection_string)
connection = engine.connect()

try:
    query = "SELECT * FROM student"
    df = pd.read_sql(query, con=connection)
    print("Data loaded successfully!")
    print(df)
except Exception as e:
    print("Error loading data into DataFrame:", e)
finally:
    connection.close()
    print("Database connection closed.")

print(df.describe())


