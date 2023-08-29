import pandas as pd 
import plotly.express as px
import streamlit as st 

st.set_page_config(page_title="Supermarket Sales",page_icon=":bar_chart",layout="wide")


df=pd.read_csv("all_df.csv")
#df.columns=df.columns.str.replace(" ","")

st.sidebar.header("Please choose the criteria")
city=st.sidebar.multiselect("Select City",
                         options=df["City"].unique(),
                         default=df["City"].unique()[:3])

product=st.sidebar.multiselect("Select product",
                         options=df["Product"].unique(),
                         default=df["Product"].unique()[:3])

month=st.sidebar.multiselect("Select Month",
                         options=df["Month"].unique(),
                         default=df["Month"].unique()[:3])

st.title(":bar_chart:2019 Sales Dashboard") 

totalsales=df["Sales Amount"].sum()

item=df["Product"].nunique()

a,b=st.columns(2)

with a:
    st.subheader("Total Sales:")
    st.subheader(f"US $ {totalsales}")
    
with b:
    st.subheader("Total number of products:")
    st.subheader(f" {item}")
    
df_selection=df.query("Product==@product and Month==@month and City==@city")

sales_by_product=df_selection.groupby("Product")["Sales Amount"].sum().sort_values(ascending=False)

barchart=px.bar(
sales_by_product, x=["Sales Amount"],y=sales_by_product.index,orientation="h",title="<b>Sales Bar Chart by Product</b>",template="plotly_white",
)  
barchart.update_layout(
    plot_bgcolor="rgba(0,0,0,0)",
    xaxis=(dict(showgrid=False))
)

sales_by_city=df_selection.groupby("City")["Sales Amount"].sum().sort_values(ascending=False)

barchart_city=px.bar(
sales_by_city, y=["Sales Amount"],x=sales_by_city.index,title="<b>Sales Bar Chart by City</b>",template="plotly_white",
)  


sales_by_month=df_selection.groupby("Month")["Sales Amount"].sum().sort_values(ascending=False)

piechart_month=px.pie(
sales_by_month,values=sales_by_month.values,names=sales_by_month.index,title="<b>Sales Bar Chart by Month</b>",template="plotly_white",
)  
barchart.update_layout(
    plot_bgcolor="rgba(0,0,0,0)",
    xaxis=(dict(showgrid=False))
)

chart_col1,chart_col2,chart_col3=st.columns(3)
chart_col1.plotly_chart(barchart,use_container_width=True)
chart_col2.plotly_chart(piechart_month,use_container_width=True)
chart_col3.plotly_chart(barchart_city,use_container_width=True)

col1,col2=st.columns(2)

value=df_selection.groupby("City")["Sales Amount"].sum()
linechart_city=px.line(
value, y=value.values,x=value.index,title="<b>Sales Bar Chart by City</b>",template="plotly_white",
)
col1.plotly_chart(linechart_city,use_container_width=True) 

scatterchart_city=px.scatter(df_selection, y="Quantity Ordered",x="Sales Amount",title="<b>Sales Bar Chart by City</b>",template="plotly_white",
)

col2.plotly_chart(scatterchart_city,use_container_width=True)  
    