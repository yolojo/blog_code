import streamlit as st 
import altair as alt
import requests
import numpy as np
import pandas as pd
import time 
from defines import getCreds, makeApiCall
from insights import getUserInsights, getUserMedia

#image = Image.open('Logo.jpg')

#st.image(image, use_column_width = False)

from streamlit_lottie import st_lottie

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_url = "https://assets6.lottiefiles.com/packages/lf20_arq6m8vt.json"
lottie_json = load_lottieurl(lottie_url)
st_lottie(lottie_json)
#st_lottie('https://assets6.lottiefiles.com/packages/lf20_arq6m8vt.json', key="user")

st.write("""
# INSTAGRAM ACCOUNT INSIGHTS 
""")

params = getCreds() # get creds

response = getUserInsights( params ) # get insights for a user

#follower_count = response['json_data']['data'][0]['values'][0]['value']
impressions = response['json_data']['data'][0]['values'][0]['value']
profile_views = response['json_data']['data'][1]['values'][0]['value']
reach = response['json_data']['data'][2]['values'][0]['value']


data = {'Metric': ['Impressions', 'Profile Views', 'Reach'], 'Count': [impressions, profile_views, reach]}

df = pd.DataFrame(data) 


p = alt.Chart(df).mark_bar().encode(x='Metric', y='Count')
p = p.properties(width=alt.Step(150))
st.write(p)