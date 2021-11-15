import os

usr = os.getenv("DB_USER")
pwd = os.getenv("DB_PWD")
ip_address = os.getenv("DB_IP_ADDRESS")
db_port = os.getenv("DB_PORT")
db_name = os.getenv("DB_NAME")

DATABASE_URI = f'postgres+psycopg2://{usr}:{pwd}@{ip_address}:{db_port}/{db_name}'