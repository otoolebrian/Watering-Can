import mysql.connector 

conn  = mysql.connector.connect(user='root', password='password', host='127.0.0.1', database='wateringcan')

arg1 = '12';
arg2 = 'name';
arg3 = 'key';

c=conn.cursor();
print c.callproc('adddevice', (arg1, arg2, arg3))
print c.callproc('wateringcan.writecondition', (arg1, arg2))
print c.fetchwarnings()

conn.commit()
c.close()
conn.close()
