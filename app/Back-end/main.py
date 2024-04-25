import datetime
import MySQLdb
from yad_2_objects import Yad_2_User, Item_For_Sale
import os





def create_connection():
    db_connection = MySQLdb.connect(
        host=os.getenv("SQL_HOST", "172.211.175.17"),
        user=os.getenv("SQL_USER", "root"),
        password=os.getenv("SQL_PASSWORD", "z1z2z3z4z5"),
        database=os.getenv("SQL_DB_NAME", "passover"),
        port=os.getenv("SQL_PORT", 3306)
    )
    return db_connection


# db_connection.cursor().fetchone()
def add_user_to_db(user: Yad_2_User, connection):
    db_cursor = connection.cursor()
    db_cursor.execute(f"""
    INSERT INTO user_data(FirstName, LastName, Email, PhoneNumber, UserName, UserPassword, City) VALUES({user})
    """)
    connection.commit()


# receiving a username and verifies its unique
def check_if_username_available(connection: MySQLdb.connect, username):
    db_cursor = connection.cursor()
    db_cursor.execute(f"""
    SELECT * FROM user_data WHERE UserName = '{username}'
    """)
    res = db_cursor.fetchall()
    if len(res) > 0:
        return False
    else:
        return True


def check_if_email_available(connection: MySQLdb.connect, email):
    db_cursor = connection.cursor()
    db_cursor.execute(f"""
    SELECT * FROM user_data WHERE UserName = '{email}'
    """)
    res = db_cursor.fetchall()
    if len(res) > 0:
        return False
    else:
        return True


def check_email_availability():
    pass


def update_user_data():
    pass


def create_a_new_user_interface():
    new_user = Yad_2_User(
        FirstName=input("enter your first name: "),
        LastName=input("enter your last name: "),
        Email=input("enter your email address: "),
        PhoneNumber=input("enter your phone number: "),
        UserName=input("enter your username: "),
        UserPassword=input("enter your password: "),
        City=input("enter the city you live in: ")
    )
    return new_user
    # check_username_availability(new_user.UserName)





def create_a_new_user(connection, new_user = None):
    if new_user == None:
        new_user = create_a_new_user_interface()
    # add_user_to_db(new_user, connection)

    try:
        add_user_to_db(new_user, connection)

    except MySQLdb.IntegrityError:
        # print("there was an error")

        if check_if_username_available(connection, new_user.UserName) == False:
            raise Exception("the username is already taken")
        
        if check_if_email_available(connection, new_user.Email) == False:
            raise Exception("the email is already taken")



    # add_user_to_db(new_user, connection)


def add_item_to_db(item: Item_For_Sale):
    pass


def list_a_new_item():
    pass


if __name__ == '__main__':
    # create_a_new_user(create_connection())
    my_user = Yad_2_User(
        FirstName='ariel',
        LastName='agranovich',
        Email='ariel.agra2@gmail.com',
        PhoneNumber='0527501333',
        UserName='sababa2',
        UserPassword='12345678',
        City="rehovot")
    create_a_new_user(create_connection(), my_user)






