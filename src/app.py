import configparser
import streamlit as st

st.header("Welcome to Streamlit! 👋")

config = configparser.ConfigParser()
config.read("config.ini")

st.write(config["DATABASE"]["name"])
st.write(config["API"]["key"])
st.write(config["API"]["url"])

