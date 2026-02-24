import streamlit as st
st.title("Библиотека")
if "books" not in st.session_state:
    st.session_state.books = []
st.header("Добави книга")
title = st.text_input("Заглавие")
author = st.text_input("Автор")
price = st.number_input("Цена", min_value=0.0)
if st.button("Добави книгата"):
    book = {
        "title": title,
        "author": author,
        "price": price
    }
    st.session_state.books.append(book)
    st.success("Книгата е добавена!")
