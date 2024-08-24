import streamlit as st
#import plotly.express as px
import pandas as pd
import os
import warnings 
from datetime import date
import time
warnings.filterwarnings('ignore')

#title of the page
st.set_page_config(page_title="Solar radiation", page_icon=":chart_with_upwards_trend:", layout="wide" )
st.title(" :chart_with_upwards_trend: Statistics for Solar radiation EDA")
st.markdown('<style>div.block-container{padding-top:2.5rem}</style>',unsafe_allow_html=True )

f1 = st.file_uploader(":file_folder: Upload a file", type=(["csv", "txt", "xlsx", "jpg", "png"]))
if f1 is not None:
    filename = f1.name
    st.write(filename)
    df = pd.read_csv(filename, encoding = "ISO-8859-1")
else:
    os.chdir(r"C:\Users\Hello\Desktop\Html Tutorial\Document\Dashboard using Streamlit")
    df = pd.read_csv("data/benin-malanville.csv", encoding = "ISO-8859-1")

data_df = pd.DataFrame(
    {
        "widgets": ["st.selectbox", "st.number_input", "st.text_area", "st.button"],
    }
)

st.data_editor(
    data_df,
    column_config={
        "widgets": st.column_config.Column(
            "Streamlit Widgets",
            help="Streamlit **widget** commands 🎈",
            width="medium",
            required=True,
        )
    },
    hide_index=True,
    num_rows="dynamic",
)

data_df = pd.DataFrame(
    {
        "birthday": [
            date(1990, 1, 1),
            date(2025, 1, 1),
          
        ]
    }
)

st.data_editor(
    data_df,
    column_config={
        "birthday": st.column_config.DateColumn(
            "Birthday",
            min_value=date(1900, 1, 1),
            max_value=date(2025, 1, 1),
            format="DD.MM.YYYY",
            step=1,
        ),
    },
    hide_index=True,
)

with st.sidebar:
    with st.echo():
        print('Home')

    with st.spinner("Loading..."):
        time.sleep(5)
    st.success("Done!")