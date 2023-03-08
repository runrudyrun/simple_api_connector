from Elt import ELTProcessor

import os
from dotenv import load_dotenv

load_dotenv()

api_url = os.getenv("API_URL")
api_key = os.getenv("API_KEY")
db_host = os.getenv("DB_HOST")
db_port = os.getenv("DB_PORT")
db_name = os.getenv("DB_NAME")
db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")
schema_name = os.getenv("SCHEMA_NAME")
table_name = os.getenv("TABLE_NAME")

if api_key == "":
    api_key = None

elt_processor = ELTProcessor(api_url, api_key, db_host, db_port, db_name, db_user, db_password, schema_name, table_name)

elt_processor.run()