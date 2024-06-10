import streamlit as st
import functions

todos = functions.get_todos()

st.title("My Todo App")
st.subheader("This is my app")
st.write("App to increase")

st.checkbox("Buy grocery")

for todo in todos:
    st.checkbox(todo)

st.text_input(label="Enter a todo", placeholder="Add a new todo...")