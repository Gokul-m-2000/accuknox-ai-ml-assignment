import csv
import sqlite3

def read_from_csv():

    users=[]

    with open("users.csv","r",newline="") as file:
        reader=csv.DictReader(file)

        for row in reader:
            users.append(row)

    return users




def save_users_to_database(users) :


    connection=sqlite3.connect("users.db")
    cursor=connection.cursor()


    cursor.execute("""
            CREATE TABLE IF NOT EXISTS users(
            Name TEXT,
            email TEXT
            )

    """)

    cursor.execute("DELETE FROM users")

    for user in users:
            
        name=user['name']
        email=user['email']


        cursor.execute("INSERT INTO users (Name, email) VALUES (?,?)",
                    (name,email) )

    connection.commit()
    connection.close()

    print("Saving users to database successful")


def display_users():

     connection=sqlite3.connect("users.db")
     cursor=connection.cursor()


     cursor.execute("SELECT Name,email FROM users")

     rows=cursor.fetchall()
     
     for row in rows:
            print(row)

     connection.close()

if __name__=="__main__":
    
    users=read_from_csv()

    save_users_to_database(users)

    display_users()
