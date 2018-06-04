import mysql.connector

def data_exists(key):
    # uses provided key (anime title) to determine if the
    # data already exists
    db_connection = mysql.connector.connect(user='josh', database='mal_scraper', password='dbpass')
    cursor = db_connection.cursor()

    # format to query data
    query = 'SELECT * from animu WHERE title = "' + str(key) + '"'
    cursor.execute(query)
    cursor.fetchall()

    # check to see if any rows were affected
    print(cursor.rowcount)
    if cursor.rowcount > 0:
        cursor.close()
        db_connection.close()
        return True
    else:
        cursor.close()
        db_connection.close()
        return False

def add_data(data):
    # setup database connection
    db_connection = mysql.connector.connect(user='josh', database='mal_scraper', password='dbpass')
    cursor = db_connection.cursor()

    # format to insert data
    data_format = ("INSERT INTO animu "
                   "(title, airing_status, num_episodes, start_date, end_date, synopsis, genres, studios) "
                   "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)")

    # insert data
    cursor.execute(data_format, data)
    db_connection.commit()

    # close connection
    cursor.close()
    db_connection.close()
