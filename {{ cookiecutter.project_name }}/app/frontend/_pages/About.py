import streamlit as st
import inspect
from {{ cookiecutter.package_name }}.etl.extract import load_data
from {{ cookiecutter.package_name }}.etl.transform import process_data
from {{ cookiecutter.package_name }}.etl.load import save_data
from {{ cookiecutter.package_name }}.utils import logger, reader

saw = []

st.title("About")
st.write("Show the docstrings of my functions.")

tabs = st.tabs(["ETL", "Features", "Models", "Utils"])

def display_docstrings(obj):
    if obj.__name__ not in saw:
        saw.append(obj.__name__)
        """Extracts and displays docstrings for functions and classes."""
        st.subheader(f"Docstring for `{obj.__name__}`")
        st.code(inspect.getdoc(obj), language="markdown")
    
# Function to extract and display function docstrings
def display_function_docstrings(module):
    """Extracts and displays only function docstrings from a given module."""
    for name, obj in inspect.getmembers(module):
        if name not in saw:
            saw.append(name)
            if inspect.isfunction(obj):  # Ensure it's a function
                st.subheader(f"Function: `{name}`")
                st.code(inspect.getdoc(obj), language="markdown")

with tabs[0]:
    st.write("ETL stands for Extract, Transform, Load.")
    
    display_docstrings(load_data)
    display_docstrings(process_data)
    display_docstrings(save_data)
    

with tabs[1]:
    st.write("Features")
    
    
    
with tabs[2]:
    st.write("Models")
    

with tabs[3]:
    st.write("Utils")
    
    display_function_docstrings(logger)
    display_function_docstrings(reader)
    