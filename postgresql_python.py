import psycopg2
from psycopg2 import OperationalError

def create_connection(db_name, db_user, db_password, db_host, db_port):
    connection = None
    try:
        connection = psycopg2.connect(
            database=db_name,
            user=db_user,
            password=db_password,
            host=db_host,
            port=db_port,
        )
        print("Connection to PostgreSQL DB successful")
    except OperationalError as e:
        print(f"The error {e} has occurred")
    return connection

# connection = create_connection(
#                 "postgres",
#                 "postgres",
#                 "password",
#                 "localhost",
#                 "5432"
#             )

def create_database(connection, query):
    """This function will only work if you
    have a previous connection object ready to
    pass to the function as an argument - as in
    a connection to the default postgres db above."""
    connection.autocommit = True
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Query executed successfully")
    except OperationalError as e:
        print(f"The error {e} has occurred")

# create_database_query = "CREATE DATABASE sm_app"
# create_database(connection, create_database_query)

"""And then before running queries against the
sm_app DB you need use the create_connection() to
connect to it."""

# connection = create_connection(
#     "sm_app",
#     "postgres",
#     "password",
#     "localhost",
#     "5432",
# )







