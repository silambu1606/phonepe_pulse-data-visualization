import os
import pandas as pd
import json


path = "E:/guvi/pulse/data/aggregated/transaction/country/india/state/"
user_state_list=os.listdir(path)

clm={'state':[],'year':[],'Quater':[],'Transaction_type':[],'Transaction_count':[],'Transaction_amount':[]}
for i in user_state_list:
    p_i=path+i+"/"
    Agg_yr=os.listdir(p_i)
    for j in Agg_yr:
        p_j=p_i+j+"/"
        Agg_yr_list=os.listdir(p_j)
        for k in Agg_yr_list:
            p_k=p_j+k
            Data=open(p_k,'r')
            D=json.load(Data)
            try:
                for z in D['data']['transactionData']:
                    Name=z['name']
                    count=z['paymentInstruments'][0]['count']
                    amount=z['paymentInstruments'][0]['amount']
                    clm['Transaction_type'].append(Name)
                    clm['Transaction_count'].append(count)
                    clm['Transaction_amount'].append(amount)
                    clm['state'].append(i)
                    clm['year'].append(j)
                    clm['Quater'].append(int(k.strip('.json')))
            except:
                pass
            

Agg_Trans = pd.DataFrame(clm)
Agg_Trans
Agg_Trans.to_csv("C:\\Users\\silam\\OneDrive\\Desktop\\Guvi notes\\phonepe\\AggTrans.csv")


path ="E:/guvi/pulse/data/map/transaction/hover/country/india/state/"

state_list = os.listdir(path)

clm = {'State': [], 'Year': [], 'Quater': [], 'District': [],
    'Transaction_count': [], 'Transaction_amount': []}
for i in state_list:
    p_i = path+i+"/"
    year = os.listdir(p_i)
    for j in year:
        p_j = p_i+j+"/"
        file = os.listdir(p_j)
        for k in file:
            p_k = p_j+k
            Data = open(p_k, 'r')
            D = json.load(Data)
            try:
                for z in D['data']["hoverDataList"]:
                    district = z['name']
                    transaction_count = z['metric'][0]['count']
                    transaction_amount = z['metric'][0]['amount']
                    clm['District'].append(district)
                    clm['Transaction_count'].append(transaction_count)
                    clm['Transaction_amount'].append(transaction_amount)
                    clm['State'].append(i)
                    clm['Year'].append(j)
                    clm['Quater'].append(int(k.strip('.json')))

            except:
                pass   
                

map_transaction = pd.DataFrame(clm)
map_transaction
map_transaction.to_csv("C:\\Users\\silam\\OneDrive\\Desktop\\Guvi notes\\phonepe\\MapTrans.csv")


path = "E:/guvi/pulse/data/map/user/hover/country/india/state/"
state_list = os.listdir(path)

clm = {'State': [], 'Year': [], 'Quater': [], 'District': [],
    'Registered_user': [], 'App_opening': []}
for i in state_list:
    p_i = path+i+"/"
    year = os.listdir(p_i)
    for j in year:
        p_j = p_i+j+"/"
        file = os.listdir(p_j)
        for k in file:
            p_k = p_j+k
            Data = open(p_k, 'r')
            D = json.load(Data)
            try:
                for z in D['data']["hoverData"]:
                    district = z
                    registered_user =  D['data']["hoverData"][z]["registeredUsers"]
                    app_opening = D['data']["hoverData"][z]["appOpens"]
                    clm['District'].append(district)
                    clm['Registered_user'].append(registered_user)
                    clm['App_opening'].append(app_opening)
                    clm['State'].append(i)
                    clm['Year'].append(j)
                    clm['Quater'].append(int(k.strip('.json')))
            except:
                pass       
                 

district_registering = pd.DataFrame(clm)
district_registering
district_registering.to_csv("C:\\Users\\silam\\OneDrive\\Desktop\\Guvi notes\\phonepe\\DistRegistering.csv")


path="E:/guvi/pulse/data/aggregated/user/country/india/state/"
user_state_list=os.listdir(path)

clm={'State':[],'Year':[],'Quater':[],'Brand':[],'Brand_count':[],'Brand_percentage':[]}
for i in user_state_list:
    p_i=path+i+"/"
    year=os.listdir(p_i)
    for j in year:
        p_j=p_i+j+"/"
        file=os.listdir(p_j)
        for k in file:
            p_k=p_j+k
            Data=open(p_k,'r')
            D=json.load(Data)
            try:
                for z in D['data']["usersByDevice"]:
                    brand=z['brand']
                    brand_count=z['count']
                    brand_percentage=z["percentage"]
                    clm['Brand'].append(brand)
                    clm['Brand_count'].append(brand_count)
                    clm['Brand_percentage'].append(brand_percentage)
                    clm['State'].append(i)
                    clm['Year'].append(j)
                    clm['Quater'].append(int(k.strip('.json')))
            
                    
            except:
                pass
            
            
user_by_device=pd.DataFrame(clm)
user_by_device
user_by_device.to_csv("C:\\Users\\silam\\OneDrive\\Desktop\\Guvi notes\\phonepe\\UserByDevice.csv")

path="E:/guvi/pulse/data/top/transaction/country/india/state/"
TOP_list = os.listdir(path)
clm = {'State': [], 'Year': [], 'Quater': [], 'District': [],
    'Transaction_count': [], 'Transaction_amount': []}


col5 = {'State': [], 'Year': [], 'Quater': [], 'District': [], 'Transaction_count': [],
        'Transaction_amount': []}
for i in TOP_list:
    p_i = path + i + "/"
    Agg_yr = os.listdir(p_i)

    for j in Agg_yr:
        p_j = p_i + j + "/"
        Agg_yr_list = os.listdir(p_j)

        for k in Agg_yr_list:
            p_k = p_j + k
            # print(p_k)
            Data = open(p_k, 'r')
            E = json.load(Data)
            for z in E['data']['pincodes']:
                Name = z['entityName']
                count = z['metric']['count']
                amount = z['metric']['amount']
                clm['District'].append(Name)
                clm['Transaction_count'].append(count)
                clm['Transaction_amount'].append(amount)
                clm['State'].append(i)
                clm['Year'].append(j)
                clm['Quater'].append(int(k.strip('.json')))
Top_transaction = pd.DataFrame(clm)
Top_transaction.to_csv("C:\\Users\\silam\\OneDrive\\Desktop\\Guvi notes\\phonepe\\Top_transaction.csv",index=False)



path = "E:/guvi/pulse/data/top/user/country/india/state/"
state_list = os.listdir(path)

clm = {'State': [], 'Year': [], 'Quater': [], 'District': [],
    'Registered_user': []}
for i in state_list:
    p_i = path+i+"/"
    year = os.listdir(p_i)
    for j in year:
        p_j = p_i+j+"/"
        file = os.listdir(p_j)
        for k in file:
            p_k = p_j+k
            Data = open(p_k, 'r')
            D = json.load(Data)
            try:
                for z in D["data"]["pincodes"]:
                    district = z["name"]
                    registered_user = z["registeredUsers"]
                    clm['District'].append(district)
                    clm['Registered_user'].append(registered_user)
                    clm['State'].append(i)
                    clm['Year'].append(j)
                    clm['Quater'].append(int(k.strip('.json')))
            except:
                pass       
                 

Top_registered_user = pd.DataFrame(clm)
Top_registered_user
Top_registered_user.to_csv("C:\\Users\\silam\\OneDrive\\Desktop\\Guvi notes\\phonepe\\Top_registerd_user.csv",index=False)