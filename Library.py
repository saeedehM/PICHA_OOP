import psycopg2
from tkinter import *
from tkinter import messagebox

global i
i = 20


class Book:
    def __init__(self, name, author, genre):
        global i
        i = i + 1
        self.id = i
        self.name = name
        self.author = author
        self.genre = genre


hostname = 'localhost'
database = 'Library'
username = 'postgres'
pwd = '2871375!!!'
port_id = 5432
conn = psycopg2.connect(host=hostname, dbname=database, user=username, password=pwd, port=port_id)
cur = conn.cursor()


# create_script = '''Create table if not exists books(
# id  int Primary Key,
#     name    varchar(100) Not Null,
#     author  varchar(100),
#     genre varchar(30)
# )
# '''
# cur.execute(create_script)


def insert_book(book, cur):
    insert_script = 'Insert into Books (id,name,author, genre) values(%s,%s,%s,%s)'
    insert_value = (book.id, book.name, book.author, book.genre)
    cur.execute(insert_script, insert_value)


def show_all(cur):
    cur.execute('Select * from Books')
    print(cur.fetchall())


def find_book_by_name(name, cur):
    cur.execute("Select * from Books where name='" + name + "'")
    res = cur.fetchone()
    book = Book(res[1], res[2], res[3])
    return book


def find_all_books_by_author(author, cur):
    cur.execute("Select * from Books where name='" + author + "'")
    res = cur.fetchone()
    bookArr = []
    for r in res:
        book = Book(r[1], r[2], r[3])
        bookArr.append(book)
    return bookArr


def delete_book(name, cur):
    cur.execute("delete from Books where name='" + name + "'")


def save_button():
    title = titleEnt.get()
    author = authorEnt.get()
    genre = genreEnt.get()
    newBook = Book(title, author, genre)
    insert_book(newBook, cur)
    messagebox.showinfo("showinfo", "Book Saved")


def single_search_button():
    name = searchEnt.get()
    book = find_book_by_name(name, cur)
    text = 'Results: ' + book.name + ' author ' + book.author + ' genre ' + book.genre
    Label(frame2, text=text, font='arial 20 bold').place(x=10, y=100)

def delete_button():
    name = deleteEnt.get()
    delete_book(name, cur)
    messagebox.showinfo("showinfo", "Book deleted")

root = Tk()
frame1 = Frame(height=250, width=800, bg='#C1FFC1', highlightbackground="black", highlightthickness=2)
frame1.pack()
Label(frame1, text="Insert a book", font='arial 15').place(x=0, y=10)
Label(frame1, text="Book title : ", font='arial 15').place(x=0, y=40)
titleEnt = Entry(root, width=50)
titleEnt.place(x=150, y=45)
Label(frame1, text="Author Name : ", font='arial 15').place(x=0, y=70)
authorEnt = Entry(root, width=50)
authorEnt.place(x=150, y=75)
Label(frame1, text="Genre: ", font='arial 15').place(x=0, y=100)
genreEnt = Entry(root, width=50)
genreEnt.place(x=150, y=105)
Button(root, text='Save Book', font='arial 15', command=save_button, bg='ghost white').place(x=200, y=200)

frame2 = Frame(height=250, width=800, bg='#97FFFF', highlightbackground="black", highlightthickness=2)
frame2.pack()
Label(frame2, text="Search for a book", font='arial 15').place(x=0, y=10)
Label(frame2, text="Book title : ", font='arial 15').place(x=0, y=40)
searchEnt = Entry(frame2, width=50)
searchEnt.place(x=150, y=45)
Button(frame2, text='Search', font='arial 15', command=single_search_button, bg='ghost white').place(x=200, y=200)

frame3 = Frame(height=250, width=800, bg='#FCE6C9', highlightbackground="black", highlightthickness=2)
frame3.pack()
Label(frame3, text="Delete a book", font='arial 15').place(x=0, y=10)
Label(frame3, text="Book title : ", font='arial 15').place(x=0, y=40)
deleteEnt = Entry(frame3, width=50)
deleteEnt.place(x=150, y=45)
Button(frame3, text='Delete', font='arial 15', command=delete_button, bg='ghost white').place(x=200, y=200)
# for fm in ['#C1FFC1', '#97FFFF', '#FCE6C9', '#FFBBFF', 'white', 'black']:
#     Frame(height=50, width=640, bg=fm).pack()
root.mainloop()
# B1 = Book('A', 'B', 'C')
# insert_book(B1, cur)
# find_book_by_name('A', cur)
conn.commit()
cur.close()
conn.close()
