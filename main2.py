import pandas as pd
import streamlit as st
import pymysql
import pandas as pd 
import mysql.connector

conn=mysql.connector.connect(user='root', password='Silambu@1606', host='localhost',port=3306,database='phonepe_pulse',
                             auth_plugin='mysql_native_password')
cursor=conn.cursor()
#df = pd.read_csv("C:\\Users\\silam\\OneDrive\\Desktop\\Guvi notes\\phonepe\\AggTrans.csv", index_col=0)
#state = pd.read_csv("C:\\Users\\silam\\OneDrive\\Desktop\\Guvi notes\\phonepe\\Longitude_Latitude_State_Table.csv")
#districts = pd.read_csv("C:\\Users\\silam\\OneDrive\Desktop\\Guvi notes\\phonepe\\Data_Map_Districts_Longitude_Latitude.csv")
#districts_tran = pd.read_csv("C:\\Users\\silam\\OneDrive\\Desktop\\Guvi notes\\phonepe\\MapTrans.csv", index_col=0)
#app_opening = pd.read_csv("C:\\Users\\silam\\OneDrive\\Desktop\\Guvi notes\\phonepe\\DistRegistering.csv", index_col=0)
#user_device = pd.read_csv("C:\\Users\\silam\\OneDrive\\Desktop\\Guvi notes\\phonepe\\UserByDevice.csv", index_col=0)
#Top_transaction=pd.read_csv("C:\\Users\\silam\\OneDrive\\Desktop\\Guvi notes\\phonepe\\Top_transaction.csv",index_col=0)
#Top_user=pd.read_csv("C:\\Users\\silam\OneDrive\\Desktop\\Guvi notes\\phonepe\\Top_registerd_user.csv",index_col=0)


import numpy as np
import matplotlib.pyplot as plt

import seaborn as sns
import streamlit as st
import plotly.express as px
from streamlit_option_menu import option_menu

st.set_page_config(page_title='Phonepe Pulse')

# Creating Options in app
#with st.sidebar:
SELECT = option_menu(
        menu_title = None,
        options = ["Search","Basic insights"],
        icons =["bar-chart","search"],
        default_index=1,
        orientation="horizontal",
        styles={
            "container": {"padding": "0!important", "background-color": "white","size":"cover"},
            "icon": {"color": "black", "font-size": "20px"},
            "nav-link": {"font-size": "20px", "text-align": "center", "margin": "-2px", "--hover-color": "#6F36AD"},
            "nav-link-selected": {"background-color": "#6F36AD"}
        }

    )
#Top and least ten transaction and user:
if SELECT == "Basic insights":
    st.title("BASIC INSIGHTS")
    #st.write("----")
    st.subheader("Let's know some basic insights about the data")
    options = ["--select--","Top 10 states based on year and amount of transaction","Least 10 states based on type and amount of transaction",
               "Top 10 mobile brands based on percentage of transaction","Top 10 Registered-users based on States and District(pincode)",
               "Top 10 Districts based on states and amount of transaction","Least 10 Districts based on states and amount of transaction",
               "Least 10 registered-users based on Districts and states","Top 10 transactions_type based on states and transaction_amount"]
    select = st.selectbox("Select the option",options)
    if select=="Top 10 states based on year and amount of transaction":
        Top_df1=pd.read_csv("https://raw.githubusercontent.com/silambu1606/phonepe_pulse-data-visualization/main/phonepe/Top_transaction10.csv")
        columns=list(Top_df1.columns)
        col1,col2 = st.columns(2)
        with col1:
            st.write(Top_df1)
        with col2:
            st.subheader("Top 10 states based on type and amount of transaction")
            fig=px.bar(Top_df1,x='State',y="Transaction_amount")
            tab1, tab2 = st.tabs(["Streamlit theme (default)", "Plotly native theme"])
            with tab1:
                st.plotly_chart(fig, theme="streamlit", use_container_width=True)
            with tab2:
                st.plotly_chart(fig, theme=None, use_container_width=True)
    
    elif select=="Least 10 states based on type and amount of transaction":
        df2=pd.read_csv("https://raw.githubusercontent.com/silambu1606/phonepe_pulse-data-visualization/main/phonepe/Top_transaction-10.csv")
        columns=list(df2.columns)
        col1,col2 = st.columns(2)
        with col1:
            st.write(df2)
        with col2:
            st.subheader("Least 10 states based on type and amount of transaction")
            fig=px.bar(df2,x='State',y="Transaction_amount")
            
            tab1, tab2 = st.tabs(["Streamlit theme (default)", "Plotly native theme"])
            with tab1:
                st.plotly_chart(fig, theme="streamlit", use_container_width=True)
            with tab2:st.plotly_chart(fig, theme=None, use_container_width=True)

    elif select=="Top 10 mobile brands based on percentage of transaction":
        cursor.execute("SELECT DISTINCT Brand,Brand_percentage FROM agg_user GROUP BY state,year,Quater,Brand,Brand_count,Brand_percentage  ORDER BY Brand_percentage DESC LIMIT 10");
        df = pd.DataFrame(cursor.fetchall(),columns=['Brand','Brand_percentage'])
        col1,col2 = st.columns(2)
        with col1:
            st.write(df)
        with col2:
            st.subheader("Top 10 mobile brands based on percentage of transaction")
            fig=px.bar(df,x="Brand",y="Brand_percentage")
            tab1, tab2 = st.tabs(["Streamlit theme (default)", "Plotly native theme"])
            with tab1:
                st.plotly_chart(fig, theme="streamlit", use_container_width=True)
            with tab2:
                st.plotly_chart(fig, theme=None, use_container_width=True)
    
    elif select=="Top 10 Registered-users based on States and District(pincode)":
        cursor.execute("SELECT DISTINCT State,District,Registered_user FROM top_user GROUP BY State,District,Year,Quater,Registered_user  ORDER BY Registered_user DESC LIMIT 10");
        df = pd.DataFrame(cursor.fetchall(),columns=['State','District','Registered-user'])
        col1,col2 = st.columns(2)
        with col1:
            st.write(df)
        with col2:
            st.subheader("Top 10 Registered-users based on States and District(pincode)")
            fig=px.bar(df,x="State",y="Registered-user")
            tab1, tab2 = st.tabs(["Streamlit theme (default)", "Plotly native theme"])
            with tab1:
                st.plotly_chart(fig, theme="streamlit", use_container_width=True)
            with tab2:
                st.plotly_chart(fig, theme=None, use_container_width=True)

    elif select=="Top 10 Districts based on states and amount of transaction":
        cursor.execute("SELECT DISTINCT state,District,Transaction_amount FROM map_trans GROUP BY state,year,Quater,District,Transaction_count,Transaction_amount ORDER BY Transaction_amount DESC LIMIT 10");
        df = pd.DataFrame(cursor.fetchall(),columns=['state','District','Transaction_amount'])
        col1,col2 = st.columns(2)
        with col1:
            st.write(df)
        with col2:
            st.subheader("Top 10 Districts based on states and amount of transaction")
            fig=px.bar(df,x="District",y="Transaction_amount")
            tab1, tab2 = st.tabs(["Streamlit theme (default)", "Plotly native theme"])
            with tab1:
                st.plotly_chart(fig, theme="streamlit", use_container_width=True)
            with tab2:
                st.plotly_chart(fig, theme=None, use_container_width=True)
    elif select=="Least 10 Districts based on states and amount of transaction":
        cursor.execute("SELECT DISTINCT state,District,Transaction_amount FROM map_trans GROUP BY state,year,Quater,District,Transaction_count,Transaction_amount ORDER BY Transaction_amount ASC LIMIT 10");
        df = pd.DataFrame(cursor.fetchall(),columns=['state','District','Transaction_amount'])
        col1,col2 = st.columns(2)
        with col1:
            st.write(df)
        with col2:
            st.subheader("Least 10 Districts based on states and amount of transaction")
            fig=px.bar(df,x="District",y="Transaction_amount")
            tab1, tab2 = st.tabs(["Streamlit theme (default)", "Plotly native theme"])
            with tab1:
                st.plotly_chart(fig, theme="streamlit", use_container_width=True)
            with tab2:
                st.plotly_chart(fig, theme=None, use_container_width=True)

    elif select=="Least 10 registered-users based on Districts and states":
        cursor.execute("SELECT DISTINCT State,District,Registered_user FROM top_user GROUP BY State,District,Year,Quater,Registered_user  ORDER BY Registered_user ASC LIMIT 10");
        df = pd.DataFrame(cursor.fetchall(),columns=['State','District','Registered_user'])
        col1,col2 = st.columns(2)
        with col1:
            st.write(df)
        with col2:
            st.subheader("Least 10 registered-users based on Districts and states")
            fig=px.bar(df,x="State",y="Registered_user")
            tab1, tab2 = st.tabs(["Streamlit theme (default)", "Plotly native theme"])
            with tab1:
                st.plotly_chart(fig, theme="streamlit", use_container_width=True)
            with tab2:
                st.plotly_chart(fig, theme=None, use_container_width=True)


    elif select=="Top 10 transactions_type based on states and transaction_amount":
        cursor.execute("SELECT DISTINCT state,Transaction_type,Transaction_amount FROM agg_trans GROUP BY  state,Transaction_amount,year,Quater,Transaction_type  ORDER BY Transaction_amount DESC LIMIT 10")
        df = pd.DataFrame(cursor.fetchall(),columns=['state','Transaction_type','Transaction_amount'])
        
        col1,col2 = st.columns(2)
        with col1:
            st.write(df)
        with col2:
            st.subheader("Top 10 transactions_type based on states and transaction_amount")
            fig=px.bar(df,x="state",y="Transaction_amount")
            tab1, tab2 = st.tabs(["Streamlit theme (default)", "Plotly native theme"])
            with tab1:
                st.plotly_chart(fig, theme="streamlit", use_container_width=True)
            with tab2:
             st.plotly_chart(fig, theme=None, use_container_width=True)







if SELECT =="Search":
    Topic = ["--Select--","Over All Transactions","Overall India User Device Analysis","Geo Visualization And District Wise Registered User"]
    choice_topic = st.selectbox("Search by",Topic)
    #Data preparation throuh mysql connector and pandas:
    def Quater_(Quater):
        cursor.execute(f"SELECT DISTINCT State,Quater,Year,Transaction_count,Transaction_amount FROM agg_trans WHERE Quater = '{Quater}' ORDER BY state,Quater,year");
        df = pd.DataFrame(cursor.fetchall(), columns=['state','Quater', 'year', 'Transaction_count', 'Transaction_amount'])
        return df
    def Quater_year(year, Quater):
        cursor.execute(f"SELECT DISTINCT state,year,Quater,Transaction_count,Transaction_amount,Transaction_type FROM agg_trans WHERE year = '{year}' AND Quater = '{Quater}' ORDER BY state,Quater,year");
        df = pd.DataFrame(cursor.fetchall(), columns=['state', 'year',"Quater", 'Transaction_count', 'Transaction_amount','Transaction_type'])
        return df
    def Quater_state(state,year, Quater):
        cursor.execute(f"SELECT DISTINCT state,year,Quater,Transaction_count,Transaction_amount,Transaction_type FROM agg_trans WHERE state = '{state}' AND Quater = '{Quater}' And year = '{year}' ORDER BY state,Quater,year");
        df = pd.DataFrame(cursor.fetchall(), columns=['state', 'year',"Quater", 'Transaction_count', 'Transaction_amount','Transaction_type'])
        return df
    def Brand_(Brand):
        cursor.execute(f"SELECT DISTINCT state,Quater,year,Brand,Brand_percentage FROM agg_user WHERE  Brand = '{Brand}' ORDER BY state,Quater,year,Brand DESC");
        df = pd.DataFrame(cursor.fetchall(), columns=['state','Quater', 'year', 'Brand', 'Brand_percentage'])
        return df
    def Brand_year(Brand,year):
        cursor.execute(f"SELECT DISTINCT State,Quater,year,Brand,Brand_percentage FROM agg_user WHERE  year = '{year}' AND Brand = '{Brand}' ORDER BY state,Quater,year,Brand DESC");
        df = pd.DataFrame(cursor.fetchall(), columns=['state','Quater', 'year', 'Brand', 'Brand_percentage'])
        return df
    def Brand_state(state,year,Brand):
        cursor.execute(f"SELECT DISTINCT State,Quater,year,Brand,Brand_percentage,Brand_count FROM agg_user WHERE  state = '{state}' AND year = '{year}' AND Brand = '{Brand}' ORDER BY state,Quater,year,Brand DESC");
        df = pd.DataFrame(cursor.fetchall(), columns=['state','Quater', 'year', 'Brand', 'Brand_percentage','Brand_count'])
        return df
    choropleth_data=pd.read_csv("phonepe/choropleth_data.csv",index_col=0)
    #plot_state_total=pd.read_csv("C:\\Users\\silam\OneDrive\\Desktop\\Guvi notes\\phonepe\\plot_state_total.csv",index_col=0)
    districts_final=pd.read_csv("phonepe/districts_final.csv",index_col=0)
    state_final=pd.read_csv("phonepe/state_final.csv",index_col=0)
    app_opening = pd.read_csv("phonepe/DistRegistering.csv", index_col=0)
    #Aggregated Transaction amount and type of transaction:
    if choice_topic == "Over All Transactions":
        select = st.selectbox('SELECT VIEW', ['Tabular view', 'Plotly View'], 0)
        if select=='Tabular view':
            col1, col2, col3 = st.columns(3)
            with col1:
                st.subheader(" SELECT MODE OF TRANSACTION ")
                Quater= st.selectbox("search by", ["","1", "2","3","4"], 0)
            with col2:
                st.subheader("SELECT YEAR ")
                choice_year = st.selectbox("Year", ["", "2018", "2019", "2020", "2021", "2022"], 0)
            with col3:
                st.subheader(" SELECT STATES ")
                menu_state = ['', 'andaman-&-nicobar-islands', 'andhra-pradesh', 'arunachal-pradesh', 'assam', 'bihar', 'chandigarh', 'chhattisgarh','dadra-&-nagar-haveli-&-daman-&-diu', 
                              'delhi', 'goa', 'gujarat', 'haryana', 'himachal-pradesh', 'jammu-&-kashmir', 'jharkhand', 'karnataka', 'kerala', 'ladakh','lakshadweep', 'madhya-pradesh', 
                              'maharashtra', 'manipur', 'meghalaya', 'mizoram', 'nagaland', 'odisha', 'puducherry', 'punjab', 'rajasthan', 'sikkim', 
                              'tamil-nadu', 'telangana', 'tripura', 'uttar-pradesh', 'uttarakhand', 'west-bengal']
                choice_state = st.selectbox("State", menu_state, 0)
            if Quater:
                col1, col2, col3, = st.columns(3)
                with col1:
                    st.subheader(f'Table view of {Quater}')
                    st.write(Quater_(Quater))

            if Quater and choice_year:
                with col2:
                    st.subheader(f' in {choice_year}')
                    st.write(Quater_year(choice_year,Quater))
            if Quater and choice_state and choice_year:
                with col3:
                    st.subheader(f' in {choice_state}')
                    st.write(Quater_state(choice_state, choice_year, Quater))
        else:
            col1, col2,col3 = st.columns(3)
            with col1:
                st.subheader(" SELECT MODE TRANSACTION ")
                Quater= st.selectbox("search by", ["1", "2","3","4"], 0)
                if Quater:
                    df = Quater_(Quater)
                    fig = px.bar(df, x="state", y="Transaction_amount", title=f'Plotly view of {Quater}',color='year')
                    st.plotly_chart(fig, theme=None, use_container_width=True)
            with col2:
                st.subheader(" SELECT YEAR ")
                choice_year = st.selectbox("Year", ["", "2018", "2019", "2020", "2021", "2022"], 0)
                if Quater and choice_year:
                    df = Quater_year(choice_year, Quater)
                    fig = px.bar(df, x="state", y="Transaction_amount",title=f"Plotly view of {Quater} in {choice_year}",color='Transaction_type')
                    st.plotly_chart(fig, theme=None, use_container_width=True)
            with col3:
                st.subheader(" SELECT STATE ")
                menu_state = ['', 'andaman-&-nicobar-islands', 'andhra-pradesh', 'arunachal-pradesh', 'assam', 'bihar', 'chandigarh', 'chhattisgarh','dadra-&-nagar-haveli-&-daman-&-diu', 
                              'delhi', 'goa', 'gujarat', 'haryana', 'himachal-pradesh', 'jammu-&-kashmir', 'jharkhand', 'karnataka', 'kerala', 'ladakh','lakshadweep', 'madhya-pradesh', 
                              'maharashtra', 'manipur', 'meghalaya', 'mizoram', 'nagaland', 'odisha', 'puducherry', 'punjab', 'rajasthan', 'sikkim', 
                              'tamil-nadu', 'telangana', 'tripura', 'uttar-pradesh', 'uttarakhand', 'west-bengal']
                choice_state = st.selectbox("State", menu_state, 0)
                if Quater and choice_state and choice_year:
                    df = Quater_state(choice_state, choice_year, Quater)
                    fig = px.bar(df, x="Transaction_type", y="Transaction_amount",title=f" {Quater} in {choice_year} at {choice_state}",color="Transaction_count")
                    st.plotly_chart(fig, theme=None, use_container_width=True)

    #Overall India Users Device Analysis by Brand:

    if choice_topic == "Overall India User Device Analysis":
        select = st.selectbox('SELECT VIEW', ['Tabular view', 'Plotly View'], 0)
        if select=='Tabular view':
            col1, col2, col3 = st.columns(3)
            with col1:
                st.subheader(" SELECT TYPE OF BRAND ")
                Brand= st.selectbox("search by", ['', 'Apple', 'Asus', 'COOLPAD', 'Gionee', 'HMD Global', 'Huawei', 'Infinix', 'Lava', 'Lenovo', 
                           'Lyf', 'Micromax', 'Motorola', 'OnePlus', 'Oppo', 'Others', 'Realme', 'Samsung', 'Tecno', 'Vivo', 'Xiaomi'], 0)
            with col2:
                st.subheader("SELECT YEAR ")
                choice_year = st.selectbox("Year", ["", "2018", "2019", "2020", "2021", "2022"], 0)
            with col3:
                st.subheader(" SELECT STATES ")
                menu_state = ['', 'andaman-&-nicobar-islands', 'andhra-pradesh', 'arunachal-pradesh', 'assam', 'bihar', 'chandigarh', 'chhattisgarh','dadra-&-nagar-haveli-&-daman-&-diu', 
                              'delhi', 'goa', 'gujarat', 'haryana', 'himachal-pradesh', 'jammu-&-kashmir', 'jharkhand', 'karnataka', 'kerala', 'ladakh','lakshadweep', 'madhya-pradesh', 
                              'maharashtra', 'manipur', 'meghalaya', 'mizoram', 'nagaland', 'odisha', 'puducherry', 'punjab', 'rajasthan', 'sikkim', 
                              'tamil-nadu', 'telangana', 'tripura', 'uttar-pradesh', 'uttarakhand', 'west-bengal']
                choice_state = st.selectbox("State", menu_state, 0)
            if Brand:
                col1, col2, col3, = st.columns(3)
                with col1:
                    st.subheader(f'{Brand}')
                    st.write(Brand_(Brand))
            if Brand and choice_year:
                with col2:
                    st.subheader(f' in {choice_year}')
                    st.write(Brand_year(Brand, choice_year))
            if Brand and choice_state and choice_year:
                with col3:
                    st.subheader(f' in {choice_state}')
                    st.write(Brand_state(choice_state, choice_year,Brand,))
                
        else:
            col1, col2,col3 = st.columns(3)
            with col1:
                st.subheader(" SELECT TYPE OF BRAND ")
                Brand= st.selectbox("search by", ['', 'Apple', 'Asus', 'COOLPAD', 'Gionee', 'HMD Global', 'Huawei', 'Infinix', 'Lava', 'Lenovo', 
                           'Lyf', 'Micromax', 'Motorola', 'OnePlus', 'Oppo', 'Others', 'Realme', 'Samsung', 'Tecno', 'Vivo', 'Xiaomi'], 0)
                if Brand:
                    df =Brand_(Brand)
                    fig = px.bar(df, x="state", y="Brand_percentage", title=f'Plotly view of {Brand}',color='year')
                    st.plotly_chart(fig, theme=None, use_container_width=True)
            with col2:
                st.subheader(" SELECT YEAR")
                choice_year = st.selectbox("Year", ["", "2018", "2019", "2020", "2021", "2022"], 0)
                if Brand and choice_year:
                    df=Brand_year(Brand, choice_year)
                    fig = px.bar(df, x="state", y="Brand_percentage",title=f"{Brand} Users in {choice_year}",color='Quater')
                    st.plotly_chart(fig, theme=None, use_container_width=True)
            with col3:
                st.subheader(" SELECT STATE ")
                menu_state = ['', 'andaman-&-nicobar-islands', 'andhra-pradesh', 'arunachal-pradesh', 'assam', 'bihar', 'chandigarh', 'chhattisgarh','dadra-&-nagar-haveli-&-daman-&-diu', 
                              'delhi', 'goa', 'gujarat', 'haryana', 'himachal-pradesh', 'jammu-&-kashmir', 'jharkhand', 'karnataka', 'kerala', 'ladakh','lakshadweep', 'madhya-pradesh', 
                              'maharashtra', 'manipur', 'meghalaya', 'mizoram', 'nagaland', 'odisha', 'puducherry', 'punjab', 'rajasthan', 'sikkim', 
                              'tamil-nadu', 'telangana', 'tripura', 'uttar-pradesh', 'uttarakhand', 'west-bengal']
                choice_state = st.selectbox("State", menu_state, 0)
                if Brand and choice_state and choice_year:
                    df = Brand_state(choice_state, choice_year, Brand)
                    fig = px.scatter(df, x="Quater", y="Brand_percentage",title=f" {Brand} in {choice_year} at {choice_state}",color="Quater")
                    st.plotly_chart(fig, theme=None, use_container_width=True)

    #State wise Geo Visualization And District Wise Registered User:

    if choice_topic == "Geo Visualization And District Wise Registered User" :
        select = st.selectbox('View', ["Geo Visualization", 'District Wise Registered User'], 0)
        if select == "Geo Visualization":
            st.subheader(" SELECT YEAR ")
            Year=st.selectbox("Year", ["", "2018", "2019", "2020", "2021", "2022"])
            st.subheader(" SELECT Quater")
            Quater=st.selectbox("Quater", ["", "1", "2", "3", "4", "5"]) 
       
           
            plot_district = districts_final[(districts_final['Year'] == Year) & (
            districts_final['Quater'] == Quater)]
            plot_state = state_final[(state_final['Year'] == Year)
                             & (state_final['Quater'] == Quater)]
            plot_state_total = plot_state.groupby(
            ['State', 'Year', 'Quater', 'Latitude', 'Longitude','code']).sum()
            plot_state_total = plot_state_total.reset_index()



            fig1 = px.scatter_geo(districts_final,
                          lon=districts_final['Longitude'],
                          lat=districts_final['Latitude'],
                          color=districts_final['Transaction_amount'],
                          size=districts_final['Transaction_count'],
                          hover_name="District",
                          hover_data=["State", 'Transaction_amount', 'Transaction_amount',
                                      'Transaction_count', 'Year', 'Quater'],
                          title='District',
                          size_max=22,)
            fig1.update_traces(marker={'color': "#CC0044",
                               'line_width': 1})
            fig2 = px.scatter_geo(plot_state_total,
                          lon=plot_state_total['Longitude'],
                          lat=plot_state_total['Latitude'],
                          hover_name='State',
                          text=plot_state_total['code'],
                          hover_data=['Transaction_count',
                                      'Transaction_amount', 'Year', 'Quater'],
                          )
            fig2.update_traces(marker=dict(color="#D5FFCC", size=0.3))
            fig = px.choropleth(
            choropleth_data,
            geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
            featureidkey='properties.ST_NM',
            locations='State',
            color='Transaction_amount',
            color_continuous_scale='twilight',
            hover_data=['Transaction_count', 'Transaction_amount']
            )

            fig.update_geos(fitbounds="locations", visible=False)
            fig.add_trace(fig1.data[0])
            fig.add_trace(fig2.data[0])
            fig.update_layout(height=1000, width=1000)
            st.plotly_chart(fig, theme=None, use_container_width=True)

        else:
            pass


        #District Wise Registered User 
       
        if select == 'District Wise Registered User':
            st.subheader(" SELECT STATE ")
            menu_state = ['', 'andaman-&-nicobar-islands', 'andhra-pradesh', 'arunachal-pradesh', 'assam', 'bihar', 'chandigarh', 'chhattisgarh','dadra-&-nagar-haveli-&-daman-&-diu', 
                              'delhi', 'goa', 'gujarat', 'haryana', 'himachal-pradesh', 'jammu-&-kashmir', 'jharkhand', 'karnataka', 'kerala', 'ladakh','lakshadweep', 'madhya-pradesh', 
                              'maharashtra', 'manipur', 'meghalaya', 'mizoram', 'nagaland', 'odisha', 'puducherry', 'punjab', 'rajasthan', 'sikkim', 
                               'tamil-nadu', 'telangana', 'tripura', 'uttar-pradesh', 'uttarakhand', 'west-bengal']
            choice_state = st.selectbox("State", menu_state, 0) 
            st.subheader(" SELECT YEAR ")
            Year=st.selectbox("Year", ["", "2018", "2019", "2020", "2021", "2022"],0)
            st.subheader(" SELECT Quater")
            Quater=st.selectbox("Quater", ["", "1", "2", "3", "4",],0)

            st.subheader(" SELECT REGISTERED ")
            R_A= st.selectbox("R_A",['Registered_user', 'App_opening'],0)
            
            Year=int(Year)
            Quater=int(Quater)
            pie_register_mode = app_opening[(app_opening['Year'] == Year) & (
            app_opening['Quater'] == Quater)&(app_opening['State'] == choice_state)]
        #Pie chart for District Registered User and App opening:
            pie_chart = px.pie( pie_register_mode, values= R_A ,
                          names= 'District', hole=.5, hover_data=['Quater'])
            st.plotly_chart(pie_chart)
          
        # Bar chart for app_opning with district wise:
            bar_chart = px.bar(pie_register_mode, x='District',
                     y='App_opening', color='District')
            st.plotly_chart(bar_chart)
            
