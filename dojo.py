import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
import numpy as np
#import datetime
import mysql.connector
import seaborn as sns
from PIL import Image 
import numpy as np
connection=mysql.connector.connect(user = 'toyscie', password = 'WILD4Rdata!', host = '51.68.18.102', port = '23456', database = 'toys_and_models')
query_finances_to='''select country, sum(priceeach*quantityordered) as turnover, month(orderDate) as month_, city
from orders o
join orderdetails od on od.ordernumber=o.ordernumber
join customers c on c.customernumber=o.customernumber
WHERE orderdate >= DATE_FORMAT(CURDATE(), '%Y-%m-01') - INTERVAL 2 MONTH
Group by country
order by turnover desc'''

st.set_page_config(
    page_title="Finance",
    page_icon="💰",
    layout="wide",
    initial_sidebar_state="auto")

# add_selectbox = st.sidebar.selectbox(
#     "Index:",
#     ["Cover","Turn over"])   

# if add_selectbox == 'Cover':
#      st.title('Dojo- Luísa')
#      image = Image.open("C:/Users/luisa/OneDrive/Ambiente de Trabalho/Dojo-pic.png")
#      st.image(image)
# else:
col1, col2, col3 = st.columns(3)
image = Image.open("Dojo-pic.png")

image2 = Image.open("car.png")

with col1:
    st.image(image)
with col2:
    st.header('Turnover per country ')
    st.subheader('*Which Country will receive the prize?*')
with col3:
    st.image(image2)
    
    fig05, ax = plt.subplots(figsize = (10,2))
df_finances_to = pd.read_sql(query_finances_to, con=connection)
df_finances_to = pd.read_sql(query_finances_to, con=connection)
df_finances_to.head(7)
st.title('''Finances ''')
st.subheader('''The turnover of the orders of the last two months by country:''')
st.info('Information from last 2 months', icon="ℹ️")

col4, col5, col6 = st.columns(3)
with col4:
    st.header('Turnover📦🌎🌎')
    # st.set_option('deprecation.showPyplotGlobalUse', False)
    print(df_finances_to.head(7))
    fig3, ax = plt.subplots(figsize=(10, 4))
    # sns.pointplot(data=df_finances_to, x="country", y= 'turnover')
    sns.lineplot(data=df_finances_to, x="country", y= 'turnover')
    ax.set_title('The turnover of orders')
    ax.set_ylabel('Orders')
    ax.set_xlabel('Country')
    st.pyplot(fig3)
    
with col5:
    st.header("Value💰")
    df_finances_to = df_finances_to[df_finances_to['country'] == 'France']
    df_finances_to2 = df_finances_to.loc[:, ["country", "city", "turnover"]]
    st.dataframe (df_finances_to2)
    
with col6:
    st.header("Winner👑")
    image3 = Image.open("prize.png")
    image4= Image.open('france.png')
    st.image(image3)



        
