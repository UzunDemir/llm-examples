from openai import OpenAI
import streamlit as st
import os
os.environ['OPENAI_API_KEY'] = st.secrets['OPENAI_API_KEY']
