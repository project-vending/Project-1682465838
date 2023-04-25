python
import psycopg2

# Redshift database connection parameters
DB_NAME = 'your_database_name'
DB_USER = 'your_database_username'
DB_PASSWORD = 'your_database_password'
DB_HOST = 'your_database_host'
DB_PORT = 'your_database_port'

# Function to load data from staging table to final table in Redshift
def load_data(table_name):
    with psycopg2.connect(database=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST, port=DB_PORT) as conn:
        with conn.cursor() as cursor:
            cursor.execute(f"INSERT INTO {table_name} SELECT * FROM staging_table;")
            conn.commit()
            print(f"Data loaded into {table_name} table successfully.")

if __name__ == "__main__":
    # Table names to load data
    table1 = "table_1"
    table2 = "table_2"

    # Load data to final tables
    load_data(table1)
    load_data(table2)
