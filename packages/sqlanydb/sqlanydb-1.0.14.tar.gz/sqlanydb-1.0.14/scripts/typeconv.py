import sqlanydb

def convert_to_int(num):
    return int(float(num)) 

sqlanydb.register_converter(sqlanydb.DT_DECIMAL, convert_to_int)

try: input = raw_input
except NameError: pass
myuid = input("Enter your user ID: ")
mypwd = input("Enter your password: ")

# Create a connection object, then use it to create a cursor
con = sqlanydb.connect( userid=myuid, password=mypwd )

cursor = con.cursor()

# Execute a SQL string
sql = "SELECT * FROM Employees WHERE EmployeeID=105"
cursor.execute(sql)

# Get a cursor description which contains column metadata
desc = cursor.description
print ("Number of columns = %d\n" % len(desc))

# Fetch all results from the cursor into a sequence and
# display the column metadata and values as name:value pairs

rowset = cursor.fetchall()
for row in rowset:
    col = 0
    for column in cursor.description:
        name, type_code, display_size, internal_size, precision, scale, null_ok = column
        
        print ("Column name: %s" % name)
        print ("Type code: %s" % type_code)
        print ("Display size: %s" % display_size)
        print ("Internal size: %d" % internal_size)
        print ("Precision: %d" % precision)
        print ("Scale: %d" % scale)
        print ("Null OK: %d" % null_ok)
        print ("Value: %s" % row[col])
        if type_code == sqlanydb.BINARY:
            print ("Python type: BINARY")
        if type_code == sqlanydb.DATE:
            print ("Python type: DATE")
        if type_code == sqlanydb.DATETIME:
            print ("Python type: DATETIME")
        if type_code == sqlanydb.NUMBER:
            print ("Python type: NUMBER")
        if type_code == sqlanydb.STRING:
            print ("Python type: STRING")
        if type_code == sqlanydb.TIME:
            print ("Python type: TIME")
        if type_code == sqlanydb.TIMESTAMP:
            print ("Python type: TIMESTAMP")
        print ("")
        col = col + 1

cursor.close()
con.close()
