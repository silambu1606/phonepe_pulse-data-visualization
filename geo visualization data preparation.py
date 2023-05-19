import pandas as pd
df = pd.read_csv("C:\\Users\\silam\\OneDrive\\Desktop\\Guvi notes\\phonepe\\AggTrans.csv", index_col=0)
state = pd.read_csv("C:\\Users\\silam\\OneDrive\\Desktop\\Guvi notes\\phonepe\\Longitude_Latitude_State_Table.csv")
districts = pd.read_csv("C:\\Users\\silam\\OneDrive\Desktop\\Guvi notes\\phonepe\\Data_Map_Districts_Longitude_Latitude.csv")
districts_tran = pd.read_csv("C:\\Users\\silam\\OneDrive\\Desktop\\Guvi notes\\phonepe\\MapTrans.csv", index_col=0)
#app_opening = pd.read_csv("C:\\Users\\silam\\OneDrive\\Desktop\\Guvi notes\\phonepe\\DistRegistering.csv", index_col=0)
#user_device = pd.read_csv("C:\\Users\\silam\\OneDrive\\Desktop\\Guvi notes\\phonepe\\UserByDevice.csv", index_col=0)
#Top_transaction=pd.read_csv("C:\\Users\\silam\\OneDrive\\Desktop\\Guvi notes\\phonepe\\Top_transaction.csv",index_col=0)
#Top_user=pd.read_csv("C:\\Users\\silam\OneDrive\\Desktop\\Guvi notes\\phonepe\\Top_registerd_user.csv",index_col=0)

state = state.reset_index(drop=True)
df2 = df.groupby(['state']).sum()[['Transaction_count', 'Transaction_amount']]
df2 = df2.reset_index()

choropleth_data = state.copy()
for column in df2.columns:
    choropleth_data[column] = df2[column]
choropleth_data = choropleth_data.drop(labels='state', axis=1)
df.rename(columns={'State': 'state'}, inplace=True)

state_list = ['andaman-&-nicobar-islands', 'andhra-pradesh', 'arunachal-pradesh',
            'assam', 'bihar', 'chandigarh', 'chhattisgarh',
            'dadra-&-nagar-haveli-&-daman-&-diu', 'delhi', 'goa', 'gujarat',
            'haryana', 'himachal-pradesh', 'jammu-&-kashmir', 'jharkhand',
            'karnataka', 'kerala', 'ladakh', 'lakshadweep', 'madhya-pradesh',
            'maharashtra', 'manipur', 'meghalaya', 'mizoram', 'nagaland',
            'odisha', 'puducherry', 'punjab', 'rajasthan', 'sikkim',
            'tamil-nadu', 'telangana', 'tripura', 'uttar-pradesh',
            'uttarakhand', 'west-bengal']
state['state'] = pd.Series(data=state_list)
state_final = pd.merge(df, state, how='outer', on='state')
state_final['state']=state_final['state'].replace({'andaman-&-nicobar-islands':'Andaman & Nicobar','andhra-pradesh':'Andhra Pradesh','arunachal-pradesh':'Arunachal Pradesh','assam':'Assam','bihar':"Bihar", 'chandigarh':"Chandigarh", 'chhattisgarh':"Chhattisgarh",
            'dadra-&-nagar-haveli-&-daman-&-diu':"Dadra and Nagar Haveli and Daman and Diu", 'delhi':"Delhi", 'goa':"Goa", 'gujarat':"Gujarat",
            'haryana':"Haryana", 'himachal-pradesh':"Himachal Pradesh", 'jammu-&-kashmir':"Jammu & Kashmir", 'jharkhand':"Jharkhand",
            'karnataka':"Karnataka", 'kerala':"Kerala", 'ladakh':"Ladakh", 'lakshadweep':"Lakshadweep", 'madhya-pradesh':"Madhya Pradesh",
            'maharashtra':"Maharashtra", 'manipur':"Manipur", 'meghalaya':"Meghalaya", 'mizoram':"Mizoram", 'nagaland':"Nagaland",
            'odisha':"Odisha", 'puducherry':"Puducherry", 'punjab':"Punjab", 'rajasthan':"Rajasthan", 'sikkim':"Sikkim",
            'tamil-nadu':"Tamil Nadu", 'telangana':"Telangana", 'tripura':"Tripura", 'uttar-pradesh':"Uttar Pradesh",
            'uttarakhand':"Uttarakhand", 'west-bengal':"West Bengal"})
districts_final = pd.merge(districts_tran, districts,
                           how='outer', on=['State', 'District'])
districts_final['State']=districts_final['State'].replace({'andaman-&-nicobar-islands':'Andaman & Nicobar','andhra-pradesh':'Andhra Pradesh','arunachal-pradesh':'Arunachal Pradesh','assam':'Assam','bihar':"Bihar", 'chandigarh':"Chandigarh", 'chhattisgarh':"Chhattisgarh",
            'dadra-&-nagar-haveli-&-daman-&-diu':"Dadra and Nagar Haveli and Daman and Diu", 'delhi':"Delhi", 'goa':"Goa", 'gujarat':"Gujarat",
            'haryana':"Haryana", 'himachal-pradesh':"Himachal Pradesh", 'jammu-&-kashmir':"Jammu & Kashmir", 'jharkhand':"Jharkhand",
            'karnataka':"Karnataka", 'kerala':"Kerala", 'ladakh':"Ladakh", 'lakshadweep':"Lakshadweep", 'madhya-pradesh':"Madhya Pradesh",
            'maharashtra':"Maharashtra", 'manipur':"Manipur", 'meghalaya':"Meghalaya", 'mizoram':"Mizoram", 'nagaland':"Nagaland",
            'odisha':"Odisha", 'puducherry':"Puducherry", 'punjab':"Punjab", 'rajasthan':"Rajasthan", 'sikkim':"Sikkim",
            'tamil-nadu':"Tamil Nadu", 'telangana':"Telangana", 'tripura':"Tripura", 'uttar-pradesh':"Uttar Pradesh",
            'uttarakhand':"Uttarakhand", 'west-bengal':"West Bengal"})
districts_final.to_csv("C:\\Users\\silam\OneDrive\\Desktop\\Guvi notes\\phonepe\\districts_final.csv")

plot_state_total = state_final.groupby(
    ['state', 'year', 'Quater', 'Latitude', 'Longitude']).sum()
plot_state_total = plot_state_total.reset_index()  
plot_state_total.rename(columns={'state': 'State'}, inplace=True)
plot_state_total.rename(columns={'year': 'Year'}, inplace=True)
plot_state_total = plot_state_total.reset_index()
state_code = ['AN', 'AD', 'AR', 'AS', 'BR', 'CH', 'CG', 'DNHDD', 'DL', 'GA',
                  'GJ', 'HR', 'HP', 'JK', 'JH', 'KA', 'KL', 'LA', 'LD', 'MP', 'MH',
                  'MN', 'ML', 'MZ', 'NL', 'OD', 'PY', 'PB', 'RJ', 'SK', 'TN', 'TS',
                  'TR', 'UP', 'UK', 'WB']
plot_state_total['code'] = pd.Series(data=state_code)
plot_state_total.to_csv("C:\\Users\\silam\OneDrive\\Desktop\\Guvi notes\\phonepe\\plot_state_total.csv")