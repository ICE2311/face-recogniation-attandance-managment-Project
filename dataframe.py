import mysql.connector


conn = mysql.connector.connect(host='localhost', user='root', password='1234',database='facial_recognizer')
my_cursor = conn.cursor()

#my_cursor.execute('select Name from student where Student_id='+str(id))
#n = my_cursor.fetchone()
