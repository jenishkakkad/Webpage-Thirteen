import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('users.db')

# Create a cursor object to execute SQL queries
cursor = conn.cursor()

# Execute a SELECT query to retrieve data from the database
cursor.execute("SELECT * FROM users")

# Fetch all the rows returned by the SELECT query
rows = cursor.fetchall()

# Display the fetched data
for row in rows:
    print(row)

# Close the cursor and the database connection
cursor.close()
conn.close()
