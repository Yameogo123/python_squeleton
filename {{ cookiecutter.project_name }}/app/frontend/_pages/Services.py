import streamlit as st

st.title("Services")
st.write("Here are the services we offer.")

tabs = st.tabs(["Visualize", "Service 2", "Service 3"])

with tabs[0]:
    st.write("Visualize data here.")
    
with tabs[1]:
    st.write("Service 2 details here.")
    
with tabs[2]:
    st.write("Service 3 details here.")