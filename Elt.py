from Connector import APIConnector
from Database import Database
import json


class ELTProcessor:
    def __init__(self, api_url, api_key, db_host, db_port, db_name, db_user, db_password, schema_name, table_name):
        self.api_connector = APIConnector(api_url=api_url, api_key=api_key)
        self.database = Database(host=db_host, port=db_port, dbname=db_name, user=db_user, password=db_password)
        self.schema_name = schema_name
        self.table_name = table_name

    def run(self):
        create_table_query = f'''
            CREATE TABLE IF NOT EXISTS {self.schema_name}.{self.table_name} (
            id SERIAL PRIMARY KEY,
            data JSON NOT NULL
            created_dttm TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
            '''
        self.database.execute_query(create_table_query)

        data = self.api_connector.get_data()
        data = json.dumps(data).replace("'", "''")
 
        insert_query = f"INSERT INTO {self.schema_name}.{self.table_name} (data) VALUES ('{data}')"
        self.database.execute_query(insert_query)

