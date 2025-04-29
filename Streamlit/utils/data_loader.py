import pandas as pd
import streamlit as st


@st.cache_data
def load_data():
    """
    Load and cache the dataset from file
    """
    df = pd.read_csv(r'Streamlit/data/train_preprocess.csv', sep=';')
    return df
