import psycopg2

def connection_db(): 
    # Enter password under ******** field. 
    connection = psycopg2.connect("dbname=PassWordManager user=root password=1234") 
    return connection