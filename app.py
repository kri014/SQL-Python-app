import streamlit as st
st.sidebar.title("Flights Analytics")
user_option=st.sidebar.selectbox('menu',["Select one","Check Flights", "Analytics"])
if user_option =="Check Flights":
    st.title("Check Flights")
elif user_option == "Analytics":
    st.title ("Analytics")

else :
    st.title("Tell about the project")