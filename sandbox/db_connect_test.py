import mysql.connector

db_cnct = mysql.connector.connect(user='josh', password='dbpass',host='localhost',database='mal_scraper')
cursor = db_cnct.cursor()

query = ("SELECT name, rating, start_airing, finish_airing, watched FROM animu")
cursor.execute(query)

for (name, rating, start_airing, finish_airing, watched) in cursor:
    print("name: {}".format(name))
    print("rating: {}".format(rating))
    print("air date: {}".format(start_airing))
    print("finish date: {}".format(finish_airing))
    print("completed: {}".format("yes" if watched == 1 else "no"))

cursor.close()
db_cnct.close()
