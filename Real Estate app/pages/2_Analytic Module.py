import streamlit as st
import pickle
import pandas as pd
import numpy as np
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title='ploting_demo')

st.title('Analyic_module')

st.title('Geomap for Sector Price_per_sqft')

new_df=pd.read_csv('dataset/data_viz1.csv')

non_numeric_cols = new_df.select_dtypes(include=['object']).columns
numeric_cols = new_df.select_dtypes(exclude=['object']).columns
grouped_df = new_df.groupby('sector')[numeric_cols].mean()
grouped_df=grouped_df[['price','price_per_sqft','built_up_area','latitude','longitude']]

# st.dataframe(grouped_df)


fig = px.scatter_mapbox(grouped_df, lat="latitude", lon="longitude",size='built_up_area',color='price_per_sqft',color_discrete_sequence=["fuchsia"], zoom=10, height=300)
fig.update_layout(mapbox_style="open-street-map")
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})


st.plotly_chart(fig,use_container_width=True)


st.title("Area Vs Price")

property_type=st.selectbox('Property Type',['overall','flat','house'])

df=pd.read_csv('dataset/gurgaon_properties_missing_value_imputation.csv')

# property_type=df['sector'].unique().tolist()
# property_type.insert(0,'overall')


if property_type == 'overall':
    fig= px.scatter(df,x='built_up_area',y='price',color='bedRoom',title='Area vs Price')
    st.plotly_chart(fig,use_container_width=True)
elif property_type == 'flat':
    fig= px.scatter(df[df['property_type']=='flat'],x='built_up_area',y='price',color='bedRoom',title='Area vs Price')
    st.plotly_chart(fig,use_container_width=True)
else:
    fig= px.scatter(df[df['property_type']=='house'],x='built_up_area',y='price',color='bedRoom',title='Area vs Price')
    st.plotly_chart(fig,use_container_width=True)

st.header('BHK Pie Chart')

sector_options = new_df['sector'].unique().tolist()
sector_options.insert(0,'overall')

selected_sector = st.selectbox('Select Sector', sector_options)

if selected_sector == 'overall':
    fig2 = px.pie(new_df, names='bedRoom')
    st.plotly_chart(fig2, use_container_width=True)
else:
    fig2 = px.pie(new_df[new_df['sector'] == selected_sector], names='bedRoom')

    st.plotly_chart(fig2, use_container_width=True)


st.header('Side by Side BHK price comparison')

fig3=px.box(new_df[new_df['bedRoom'] <= 8],x='bedRoom',y='price',title='BHK Price Range')
st.plotly_chart(fig3, use_container_width=True)


st.header('Side by Side Distplot for property type')

fig4 = plt.figure(figsize=(10, 4))
sns.distplot(new_df[new_df['property_type'] == 'house']['price'],label='house')
sns.distplot(new_df[new_df['property_type'] == 'flat']['price'], label='flat')
plt.legend()
st.pyplot(fig4)