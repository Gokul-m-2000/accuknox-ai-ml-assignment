import requests
import sqlite3

API_URL="https://openlibrary.org/search.json"


def get_books():
    try:
        response=requests.get(
            API_URL,
            params={
                "q":"python programming",
                "limit":5
            },
            timeout=10
        )


        response.raise_for_status()

        data=response.json()
        books = data.get("docs",[])

        return books
    except requests.RequestException as e:
        print(f"failed to retrive books : {e}")
        return None
    
def save_books_to_database(books) :


    connection=sqlite3.connect("books.db")
    cursor=connection.cursor()


    cursor.execute("""
            CREATE TABLE IF NOT EXISTS books(
            title TEXT,
            author TEXT,
            publication_year INTEGER
            )

    """)


    cursor.execute("DELETE FROM books")

    for book in books:
        title=book.get('title')
        author=book.get('author_name')
        publication_year=book.get('first_publish_year')


        if author:
            author=", ".join(author)

        else:
            author=None

        cursor.execute(
            """
            INSERT INTO books (title,author,publication_year)
            VALUES(?,?,?)
            """,
            (title,author,publication_year)
        )
    connection.commit()
    connection.close()


def display_books():

    connection = sqlite3.connect("books.db")
    cursor = connection.cursor()

    cursor.execute(
    "SELECT title,author,publication_year FROM books")

    rows=cursor.fetchall()

    for row in rows:
        print(row)

    connection.close()


if __name__=="__main__":

    books=get_books()
    
    if books is not None:
        save_books_to_database(books)
        display_books()

  