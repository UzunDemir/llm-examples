from openai import OpenAI
import streamlit as st
import os
os.environ['OPENAI_API_KEY'] = st.secrets['OPENAI_API_KEY']

import os

if 'OPENAI_API_KEY' in os.environ:
    st.write("API key is set")
else:
    st.write("API key is missing")

