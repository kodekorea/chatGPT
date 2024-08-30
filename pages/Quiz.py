import streamlit as st
# 질문과 선택지
from openai import OpenAI
def chatbot(question):
    client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])
    completion = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": "너는 안동의 명물인지 아닌지 알려주는 봇이야 맞다면 y 아니면 n 으로 대답해줘"},
        {"role": "user", "content": question}
    ]
    )
    return completion.choices[0].message.content


question = "안동에서 유명한 것은?"
answer = st.text_input(question)
if st.button("정답 확인하기"):
    result=chatbot(answer)
    if result == 'y':
        st.success("정답!")
    else:
        st.error("오답!")
