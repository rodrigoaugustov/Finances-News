import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, inspect
from src.entities.news import Base as NewsTable

load_dotenv()

usr = os.getenv("DB_USER", "")
pwd = os.getenv("DB_PWD", "")
ip_address = os.getenv("DB_IP_ADDRESS", "")
db_port = os.getenv("DB_PORT", "")
db_name = os.getenv("DB_NAME", "")
database = os.getenv("DATABASE", "postgresql")

DATABASE_URI = f'postgresql+psycopg2://{usr}:{pwd}@{ip_address}:{db_port}/{db_name}'

if database == 'mysql':
    DATABASE_URI = f'mysql+pymysql://{usr}:{pwd}@{ip_address}:{db_port}/{db_name}'

ENGINE = create_engine(DATABASE_URI)

if not inspect(ENGINE).has_table('news'):
    NewsTable.metadata.create_all(ENGINE)
