import streamlit as st

check = st.checkbox('チェックボックス')

if check:
    st.button('ボタン')
    st.selectbox('selectbox', ('option1', 'option2', 'option3'))
    st.multiselect('multiselect', ('option1', 'option2', 'option3'))
    st.radio('radio', ('option1', 'option2', 'option3'))
    st.text_input('text_input')
    st.text_area('text_area')
