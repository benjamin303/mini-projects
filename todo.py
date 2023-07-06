from os import system
import mysql.connector

mydb = mysql.connector.connect(
    host="192.168.1.103",
    user="benjamin",
    password="benjamin",
    database="learning"
)

mycursor = mydb.cursor()

mycursor.execute("SHOW TABLES LIKE 'todo'")

if not mycursor.fetchone():
    mycursor.execute('''CREATE TABLE todo (
        id INT AUTO_INCREMENT PRIMARY KEY, 
        title VARCHAR(100), 
        task VARCHAR(255), 
        status VARCHAR(15)
        )''')



def display_menu():
    print("----- ToDo App Menu -----")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Open")
    print("4. Mark Task as In Progress")
    print("5. Mark Task as Complete")
    print("6. Delete Task")
    print("0. Exit")


def add_task():
    title = input("Vnesi naslov: ")
    task = input("Vnesi task/description: ")
    status = input("Vnesi status (open/progress/close): ")
    sql = "INSERT INTO todo (title, task, status) VALUES (%s, %s, %s)"
    val = (title, task, status)
    mycursor.execute(sql, val)
    mydb.commit()
    system('cls')
    print(mycursor.rowcount, "podatek vnesen.")
    pass


def view_tasks():
    mycursor.execute("SELECT * FROM todo")
    myresult = mycursor.fetchall()
    for x in myresult:
        print(x)
    pass


def mark_task_open():
    mycursor.execute("SELECT * FROM todo")
    myresult = mycursor.fetchall()
    for x in myresult:
        print(x)
    id = int(input("Vnesite id taska: "))
    sql = "UPDATE todo SET status = 'Open' WHERE id = %s"
    val = (id,)
    mycursor.execute(sql, val)
    mydb.commit()
    system('cls')
    print(mycursor.rowcount, "record affected")
    pass


def mark_task_in_progress():
    mycursor.execute("SELECT * FROM todo")
    myresult = mycursor.fetchall()
    for x in myresult:
        print(x)
    id = int(input("Vnesite id taska: "))
    sql = "UPDATE todo SET status = 'In progress' WHERE id = %s"
    val = (id,)
    mycursor.execute(sql, val)
    mydb.commit()
    system('cls')
    print(mycursor.rowcount, "record affected")
    pass


def mark_task_complete():
    mycursor.execute("SELECT * FROM todo")
    myresult = mycursor.fetchall()
    for x in myresult:
        print(x)
    id = int(input("Vnesite id taska: "))
    sql = "UPDATE todo SET status = 'Completed' WHERE id = %s"
    val = (id,)
    mycursor.execute(sql, val)
    mydb.commit()
    system('cls')
    print(mycursor.rowcount, "record affected")
    pass

def delete_task():
    mycursor.execute("SELECT * FROM todo")
    myresult = mycursor.fetchall()
    for x in myresult:
        print(x)
    id = int(input("Vnesi id taska za brisanje: "))
    sql = "DELETE FROM todo WHERE id = %s"
    val = (id,)
    mycursor.execute(sql, val)
    mydb.commit()
    system('cls')
    print(mycursor.rowcount, "record deleted")
    pass


while True:
    display_menu()
    choice = input("Enter your choice (0-6): ")
    system('cls')
    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        mark_task_open()
    elif choice == "4":
        mark_task_in_progress()
    elif choice == "5":
        mark_task_complete()
    elif choice == "6":
        delete_task()
    elif choice == "0":
        print("Exiting ToDo App...")
        system('cls')
        break
    else:
        print("Invalid choice. Please try again.")
