import streamlit as st
from zhipuai import ZhipuAI
from langchain.memory import ConversationBufferMemory
st.title("欢迎来到帅帅智能绘图")
#构建知普AI大模型
if "memory" not in st.session_state:
    st.session_state.memory = ConversationBufferMemory()
model = ZhipuAI(api_key='a6cad3de867a366b805b25777d9bde0f.R4YTJhaAmWtIQ67m')

if "cache" not in st.session_state:
    st.session_state.cache = []
else:
    for message in st.session_state.cache:
        if message['role'] =='user':
            with st.chat_message(message['role']):
                 st.write(message['content'])
        else:
            with st.chat_message(message['role']):
                 st.image(message['content'],width=200)
# 创建输入框
problem = st.chat_input("请输入图片的描述")
if problem:
    with st.chat_message("user"):
        st.write(problem)
        st.session_state.cache.append({"role": "user", "content": problem})
    response = model.images.generations(
            model='cogview-3-plus',
            prompt=problem,
    )
    image = response.data[0].url
    with st.chat_message("assistant"):
        st.image(image,width=200)
        st.session_state.cache.append({"role": "assistant", "content": image})
