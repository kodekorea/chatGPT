import streamlit as st
st.title("Streamlit Course :star2:")
st.header("Streamlit 설치")
st.write("terminal에 streamlit 패키지 설치하기")
st.code("pip install streamlit")
st.header("Streamlit 파일 만들기")
st.write("home.py 만들기")
with st.echo():
    import streamlit
    st.write("Hello, There!")
st.header("Streamlit 웹 실행하기")
st.write("파일을 저장하고 터미널에 다음 명령어 치기")
st.code("streamlit run home.py")

