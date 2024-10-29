import streamlit as st
# 调用大模型，导入langchain的代码
from langchain_openai import ChatOpenAI
# 提示词对象
from langchain.prompts import PromptTemplate
# 映入记忆模块
from langchain.memory import ConversationBufferMemory
# 引入链对象
from langchain.chains import LLMChain
# 构建一个大模型--智普AI公司提供的大模型
st.title('柳如烟♥♥♥')
# 创建记忆模块
if "memory" not in st.session_state:
    st.session_state.memory = ConversationBufferMemory(memory_key="history")
# memory = ConversationBufferMemory(memory_key="history")
model = ChatOpenAI(
    temperature=0.8,#温度，代表创新性
    model="glm-4-plus",#大模型的名字
    base_url="https://open.bigmodel.cn/api/paas/v4/",#大模型的地址
    api_key="a6cad3de867a366b805b25777d9bde0f.R4YTJhaAmWtIQ67m"
)
# 创建提示词对象
prompt = PromptTemplate.from_template("你叫柳如烟，你是一个体贴温柔型的人，你现在扮演的是一个女朋友的角色，你现在要和你的男朋友对话，你男朋友的话是{input}，你需要对你的男朋友做出回应，而且只做回应，你和你男朋友的历史对话为{history}")
# 使用langchain链关联大模型和提示词对象
chain = LLMChain(
    llm=model,
    prompt=prompt,
    memory=st.session_state.memory,
)
# 创建一个聊天输入框
if "cache" not in st.session_state:
    st.session_state.cache = []
else:
    for message in st.session_state.cache:
        with st.chat_message(message['role']):
            st.write(message["content"])
# 创建聊天输入框
problem = st.chat_input("你的如烟正在等待你的回应")
# 判断用来确定用户有没有输入问题
if problem:
    # 1、将用户的问题输出到界面上，以用户的角色输出
    with st.chat_message("user"):
        st.write(problem)
    st.session_state.cache.append({"role": "user", "content": problem})
    # # 2、调用大模型回答问题
    # result = model.invoke(problem)
    # 调用链对象回答问题
    result = chain.invoke({"input": problem})
    # 3、将大模型数据的回答输出到界面上
    with st.chat_message("assistant"):
        st.write(result['text'])
    st.session_state.cache.append({"role": "assistant", "content": result['text']})