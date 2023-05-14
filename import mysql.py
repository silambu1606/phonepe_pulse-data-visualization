import pandas as pd 
import mysql.connector

conn=mysql.connector.connect(user='root', password='Silambu@1606', host='localhost',port=3306,
                             auth_plugin='mysql_native_password')
cursor=conn.cursor()
cursor.execute("DROP DATABASE IF EXISTS phonepe_pulse")
cursor.execute("CREATE DATABASE phonepe_pulse")
cursor.execute("USE phonepe_pulse")
#Table creation in phonepe_pulse database:
cursor.execute('''CREATE TABLE agg_trans(MyIndex INTEGER,state VARCHAR(50),year YEAR,
                Quater INTEGER, Transaction_type VARCHAR(50),TRansaction_count INTEGER,Transaction_amount FLOAT,
                PRIMARY KEY (MyIndex))''')
agg_trans_df=pd.read_csv("C:\\Users\\silam\\OneDrive\\Desktop\\Guvi notes\\phonepe\\AggTrans.csv")
#Data Insert into table using for loop:
for i, row in agg_trans_df.iterrows():
        sql = "INSERT INTO phonepe_pulse.agg_trans VALUES (%s,%s,%s,%s,%s,%s,%s)"
        cursor.execute(sql, tuple(row))
        print("Record inserted")
        conn.commit()
# Reapeted for how many tables do you want.      
cursor.execute('''CREATE TABLE agg_user(MyIndex INTEGER,state VARCHAR(50),year YEAR,
                Quater INTEGER,Brand VARCHAR(50),Brand_count INTEGER,Brand_percentage FLOAT,
                PRIMARY KEY (MyIndex))''')
agg_user_df=pd.read_csv("C:\\Users\\silam\\OneDrive\\Desktop\\Guvi notes\\phonepe\\UserByDevice.csv")               
for i, row in agg_user_df.iterrows():
        sql = "INSERT INTO phonepe_pulse.agg_user VALUES (%s,%s,%s,%s,%s,%s,%s)"
        cursor.execute(sql, tuple(row))
        print("Record inserted")
        conn.commit()
        
cursor.execute('''CREATE TABLE map_trans(MyIndex INTEGER,state VARCHAR(50),year YEAR,
                Quater INTEGER, Transaction_type VARCHAR(50),TRansaction_count INTEGER,Transaction_amount FLOAT,
                PRIMARY KEY (MyIndex))''')
map_trans_df=pd.read_csv("C://Users//silam//OneDrive//Desktop//Guvi notes//phonepe//MapTrans.csv")

for i, row in map_trans_df.iterrows():
        sql = "INSERT INTO phonepe_pulse.map_trans VALUES (%s,%s,%s,%s,%s,%s,%s)"
        cursor.execute(sql, tuple(row))
        print("Record inserted")
        conn.commit()
        
cursor.execute('''CREATE TABLE district_register(MyIndex INTEGER,state VARCHAR(50),year YEAR,
                Quater INTEGER, District VARCHAR(50),Registered_user INTEGER,App_opening FLOAT,
                PRIMARY KEY (MyIndex))''')
district_register_df=pd.read_csv("C://Users//silam//OneDrive//Desktop//Guvi notes//phonepe//DistRegistering.csv")

for i, row in district_register_df.iterrows():
        sql = "INSERT INTO phonepe_pulse.district_register VALUES (%s,%s,%s,%s,%s,%s,%s)"
        cursor.execute(sql, tuple(row))
        print("Record inserted")
        conn.commit()
        
cursor.execute('''CREATE TABLE map_district(state VARCHAR(50),District VARCHAR(50),
                Latitude FLOAT,Longitude FLOAT,
                PRIMARY KEY (District(50)))''')
                
map_district_df=pd.read_csv("C://Users//silam//OneDrive//Desktop//Guvi notes//phonepe//Data_Map_Districts_Longitude_Latitude.csv",index_col=None)
for i, row in map_district_df.iterrows():
        sql = "INSERT INTO phonepe_pulse.map_district VALUES (%s,%s,%s,%s)"
        cursor.execute(sql, tuple(row))
        print("Record inserted")
        conn.commit()

cursor.execute('''CREATE TABLE map_state(code VARCHAR(50),
                Latitude FLOAT,Longitude FLOAT,state VARCHAR(50),
                PRIMARY KEY (state(50)))''')
                
map_state_df=pd.read_csv("C://Users//silam//OneDrive//Desktop//Guvi notes//phonepe//Longitude_Latitude_State_Table.csv")
for i, row in map_state_df.iterrows():
        sql = "INSERT INTO phonepe_pulse.map_state VALUES (%s,%s,%s,%s)"
        cursor.execute(sql, tuple(row))
        print("Record inserted")
        conn.commit()