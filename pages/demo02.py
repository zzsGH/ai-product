import streamlit as st
from langchain_openai import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
st.title("你的小香猪")
if "memory" not in st.session_state:
    st.session_state.memory = ConversationBufferMemory()
model = ChatOpenAI(
    temperature=0.8,
    model="glm-4-plus",
    base_url="https://open.bigmodel.cn/api/paas/v4/",
    api_key="a6cad3de867a366b805b25777d9bde0f.R4YTJhaAmWtIQ67m"
)

prompt = PromptTemplate.from_template("你是一头猪，你现在要和你的主人对话，你主人说的话是{input}，你们的对话历史是{history}，你只需要回应，不需要其他的回答")
chain = LLMChain(
    llm=model,
    prompt=prompt,
    memory=st.session_state.memory
)
if "cache" not in st.session_state:
    st.session_state.cache = []
else:
    for message in st.session_state.cache:
        with st.chat_message(message["role"]):
            st.write(message["content"])
problem = st.chat_input("猪饿了")
if problem:
    with st.chat_message("user"):
        st.write(problem)
        st.session_state.cache.append({"role": "user", "content": problem})
    result = chain.invoke({"input": problem})
    with st.chat_message("assistant"):
        st.write(result["text"])
        st.session_state.cache.append({"role": "assistant", "content": result["text"]})