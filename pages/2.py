import streamlit as st
with st.echo():
    if st.button("불러오기"):
        if "이름" in st.session_state:
            st.write(st.session_state.이름)
        else:
            st.write("1페이지 먼저 하세요")

