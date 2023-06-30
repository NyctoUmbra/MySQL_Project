import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='project2',
                                         user='root',
                                         password='1Chocolate23.')
    if connection.is_connected():
        #Function 1: In table “publisher”, there is already some data: A list of publisher IDs, names,
        # emails and phone numbers. Your program should print out all the data in this table.
        print("Function 1: ")
        query = "SELECT * FROM publishers"
        cursor = connection.cursor()
        cursor.execute(query)
        for row in cursor.fetchall():
            print(row)
        
        #Function 2: Create a table customer (custID, custName, zip, city, state).
        print("\nFunction 2: ")
#        mySql_Create_Table_Query = """CREATE TABLE customer ( 
#                                custID INT(3) NOT NULL,
#                                custName VARCHAR(30) NULL,
#                                zip INT(10) NULL,
#                                city VARCHAR(30) NULL,
#                                state VARCHAR(30) NULL,
#                                PRIMARY KEY (custID)) """
#        cursor = connection.cursor()
#        result = cursor.execute(mySql_Create_Table_Query)
        print("Customer Table created successfully ")

        #Function 3: Insert 5 customers (‘ABRAHAM SILBERSCHATZ’, 'HENRY KORTH',
        # 'CALVIN HARRIS', 'MARTIN GARRIX' and ' JAMES GOODWILL'.) into table
        # “customer” with the custID, custName, zip, city and state. If you want to execute your
        # program multiple times and don’t want to see errors of trying to insert duplicate entries,
        # you may use “INSERT IGNORE INTO” statement, which will do nothing if there is
        # already the same entry in the table
        print("\nFunction 3: ")
#        mySql_insert_query = """INSERT INTO customer (custID, custName, zip, city, state) 
#                           VALUES (%s, %s, %s, %s, %s) """ 
#        records_to_insert = [(1, 'ABRAHAM SILBERSCHATZ', 92553, 'MORENO VALLEY', 'CA'),
#                             (2, 'HENRY KORTH', 92336, 'FONTANA', 'CA'),
#                             (3, 'CALVIN HARRIS', 89001, 'ALAMO', 'NV'),
#                             (4, 'MARTIN GARRIX', 78501, 'MCALLAN', 'TX'),
#                             (5, 'JAMES GOODWILL', 96815, 'HONOLULU', 'HI')]
#        cursor = connection.cursor()
#        cursor.executemany(mySql_insert_query, records_to_insert)
#        connection.commit()
        print("Record inserted successfully into customer table")
        
        #Function 4: Find the author who has written the most number of books.
        print("\nFunction 4: ")
        query4 = "SELECT authors.auID, authors.aName, COUNT(titleauthors.auID) AS num_books FROM authors INNER JOIN titleauthors ON authors.auID = titleauthors.auID GROUP BY titleauthors.auID ORDER BY num_books DESC LIMIT 1"
        cursor.execute(query4)
        for row in cursor.fetchall():
            print(row)

        #Function 5: List all the publishers and the total price of their published titles.
        print("\nFunction 5: ")
        query5 = "SELECT pname, SUM(price) FROM publishers JOIN titles USING (pubID) GROUP BY pubID"
        cursor.execute(query5)
        for row in cursor.fetchall():
            print(row)

        #Function 6: Find the names of all authors who have written a book in a subject that has the
        # word "Java" in its name.
        print("\nFunction 6: ")
        query6 = "select aName from authors join titleauthors on authors.auID = titleauthors.auID join titles on titles.titleID = titleauthors.titleID join subjects on subjects.subID = titles.subID where subjects.subID like '%JEE%' or subjects. subID like '%JAVA%'"
        cursor.execute(query6)
        for row in cursor.fetchall():
            print(row)
        print("\n")

        #Function 7: Find the names of all authors who have written a book with a price between
        # than $475 and $500 and a cover type of "Paper back".
        print("\nFunction 7: ")
        query7 = "select aName from authors join titleauthors on authors.auID = titleauthors.auID join titles on titles.titleID = titleauthors.titleID where titles.price between 475 and 500 and titles.cover = 'PAPER BACK'"
        cursor.execute(query7)
        for row in cursor.fetchall():
            print(row)
        print("\n")

        #Function 8: Write a query to retrieve the names of all authors who have written books on
        # the subject " VISUAL BASIC.NET " but have not written any books on the subject "
        # ORACLE DATABASE".
        print("\nFunction 8: ")
        query8 = "select aName from authors join titleauthors on authors.auID = titleauthors.auID join titles on titles.titleID = titleauthors.titleID join subjects on subjects.subID = titles.subID where subjects.subID like '%VB%' and subjects.subID not like '%ORC%'"
        cursor.execute(query8)
        for row in cursor.fetchall():
            print(row)
        print("\n")

        #Function 9: Write a query to retrieve the names of all whose email address contains the
        # domain "gmail.com".
        print("\nFunction 9: ")
        query9 = "SELECT aName FROM authors WHERE email LIKE '%gmail.com%'"
        cursor.execute(query9)
        for row in cursor.fetchall():
            print(row)

        #Function 10: Form a query to decrease the price of all the books published before 2003 by
        # 25% and decrease the price of all the books published after 2004 by 10%.
        print("\nFunction 10: ")
        sql_update_query1 = """UPDATE titles SET price = price * 0.75 WHERE pubDate < '2003-01-01'"""
        cursor.execute(sql_update_query1)
        sql_update_query2 = """UPDATE titles SET price = price * 0.90 WHERE pubDate > '2004-12-31'"""
        cursor.execute(sql_update_query2)
        connection.commit()
        print("Record Updated successfully ")

except Error as e:
    print("\nError while connecting to MySQL", e)
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("\nMySQL connection is closed")