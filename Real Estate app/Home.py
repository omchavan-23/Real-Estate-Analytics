import streamlit as st


st.set_page_config(
    page_title="Real Estate Analytics of Gurgaon",
    page_icon="👋",
)
# st.set_page_config(page_title='Home')

st.title("Real Estate Analytics of Gurgaon")


st.markdown('''Welcome to the Real Estate Analytics platform dedicated to the bustling 
city of Gurgaon. Our platform provides a comprehensive suite of tools to 
assist you in making informed decisions about the real estate market.''')

st.header('Explore Our Features')

st.subheader('1. Price Predictor')
st.markdown('Accurately estimate property prices in Gurgaon using our advanced machine learning model. Input various property features to get an instant price prediction.')


st.subheader('2. Analytic Module')
st.markdown('Dive deep into the trends and patterns of the Gurgaon real estate market. Analyze historical data, visualize market trends, and gain insights into price movements and property demands.')


st.subheader('3. Recommender System')
st.markdown('Get personalized property recommendations tailored to your preferences. Whether you’re looking to buy, rent, or invest, our recommender system will help you find the best options available in the market.')
