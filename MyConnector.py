import mysql.connector

myTestDb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='venkata1',
    port='3306',
    database='test_schema'
)


mycursor = myTestDb.cursor()

mycursor.execute('SELECT * FROM user')

users = mycursor.fetchall()
print('Users: ')
for user in users:
    print(user)


mycursor.execute('SELECT * FROM category')

categories = mycursor.fetchall()

print('\nCategories: ')
for category in categories:
    print(category)

name = 'ENTER NAME'
email = 'ENTER EMAIL'
password = 'ENTER PASSWORD'

mycursor.execute('INSERT INTO user(username,email,password) VALUES(\'' + name + '\',\'' + email + '\',\'' + password + '\');'
                 )

#Uncomment to commit to database
#myTestDb.commit()

mycursor.close()
myTestDb.close()
