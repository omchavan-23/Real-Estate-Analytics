import streamlit as st
import pickle
import pandas as pd
import numpy as np

st.set_page_config(page_title='Price_Predictor')

with open ('df.pkl','rb') as file:
    df=pickle.load(file)

with open ('pipeline.pkl','rb') as file:
    pipeline =pickle.load(file)

# st.dataframe(df)

st.header('Enter your inputs')

# 'property_type'
property_type=st.selectbox('Property type',['flat','house'])

# 'sector'
sector=st.selectbox('Sector',sorted(df['sector'].unique().tolist()))

# 'bedRoom'
BedRooms=float(st.selectbox('Number of BedRooms',sorted(df['bedRoom'].unique().tolist())))

# 'bathroom'
bathroom=float(st.selectbox('Number of Bathroom',sorted(df['bathroom'].unique().tolist())))

# 'balcony'
balconies=st.selectbox('Number of Balconies',sorted(df['balcony'].unique().tolist()))

# 'agePossession'
Property_Age=st.selectbox('Property age',sorted(df['agePossession'].unique().tolist())) 

# 'built_up_area'
built_up_area=float(st.number_input('Built up area'))

# 'servant room'
servant_room=st.selectbox('Servant room',sorted(df['servant room'].unique().tolist())) 

# 'store room'
store_room=st.selectbox('Store room',sorted(df['store room'].unique().tolist())) 

# 'furnishing_type'
furnishing_type=st.selectbox('Furnishing type',sorted(df['furnishing_type'].unique().tolist())) 

# 'luxury_category'
luxury_category=st.selectbox('Luxury category',sorted(df['luxury_category'].unique().tolist())) 

# 'floor_category'
floor_category=st.selectbox('Floor category',sorted(df['floor_category'].unique().tolist())) 

if st.button('Predict'):
    # form a datafame
    data= [[property_type, sector, BedRooms, bathroom, balconies, Property_Age, built_up_area, servant_room, store_room,furnishing_type,luxury_category,floor_category]]
    columns = ['property_type', 'sector', 'bedRoom', 'bathroom', 'balcony',
       'agePossession', 'built_up_area', 'servant room', 'store room',
       'furnishing_type', 'luxury_category', 'floor_category']

# Convert to DataFrame
    one_df = pd.DataFrame(data, columns=columns)

    # st.dataframe(one_df)

    # predict
    base_price=np.expm1(pipeline  .predict(one_df))[0]

    low=base_price-0.22
    high=base_price+0.22

    # display

    st.text('The price of flat is between {} Cr and {} Cr'.format(round(low,2),round(high,2)))