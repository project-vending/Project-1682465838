python
import streamlit as st
import psycopg2

# Connect to Redshift database
conn = psycopg2.connect(
    host="redshift-host",
    port=5439,
    database="redshift-database",
    user="redshift-user",
    password="redshift-password"
)

# Define SQL query to retrieve data
query = "SELECT * FROM my_table"

# Execute SQL query and fetch results
cur = conn.cursor()
cur.execute(query)
results = cur.fetchall()

# Display results in Streamlit table
st.table(results)

# Close database connection
cur.close()
conn.close()
