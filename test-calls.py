import MySQLdb 
conn = MySQLdb.connect(host='localhost',db='wateringcan',user='root',passwd='password')

arg1 = "id";
arg2 = "name";
arg3 = "key";

c=conn.cursor();
c.callproc('adddevice', (arg1, arg2, arg3))

print c.status()

c.execute("SELECT * from devices")
print c.fetchone()
