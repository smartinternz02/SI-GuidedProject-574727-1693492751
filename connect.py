from flask import Flask, render_template, request,session

import ibm_db

def showall():
    sql = "SELECT * from APPOINTMENT"
    stmt = ibm_db.exec_immediate(conn, sql)
    dictionary = ibm_db.fetch_both(stmt)
    while dictionary != False:
      
        print("The fullname is : ",  dictionary["NAME"])
        print("The role is : ",  dictionary["ROLE"])
        print("The mail id is : ",  dictionary["EMAIL"])
        print("The username is : ",  dictionary["USERNAME"])
        print("The pwd is : ",  dictionary["PWD"])
        dictionary = ibm_db.fetch_both(stmt)

def insert_db(conn, NAME,ROLE,EMAIL,USERNAMER,PWD):
    sql = "INSERT into APPOINTMENT VALUES('{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(NAME,ROLE,EMAIL,USERNAME,PWD)
    stmt = ibm_db.exec_immediate(conn, sql)
    print("Number of affected rows: ", ibm_db.num_rows(stmt))

    

try:
    conn = ibm_db.connect("DATABASE=bludb;HOSTNAME=fbd88901-ebdb-4a4f-a32e-9822b9fb237b.c1ogj3sd0tgtu0lqde00.databases.appdomain.cloud;PORT=32731;SECURITY=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt;UID=bfb81601;PWD=oIY0vANO8L2ecmm3", '', '')
    print(conn)
    print("Connection successful...")
    
    # Call the function to show all records
    showall()
 # Example of inserting a new record
    insert_db(conn, "AVNR", "FACULTY", "avnr424@nrtec.in", "avnr424", "akowshik")
    
   

except Exception as e:
    print("Error connecting to the database:", e)