import streamlit as st

check = st.checkbox('チェックボックス')
st.sidebar.text_input('text_input')
st.sidebar.text_area('text_area')

if check:
    st.button('ボタン')
    st.selectbox('selectbox', ('option1', 'option2', 'option3'))
    st.multiselect('multiselect', ('option1', 'option2', 'option3'))
    st.radio('radio', ('option1', 'option2', 'option3'))
