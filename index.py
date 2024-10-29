import streamlit as st
vertical_alignment = st.selectbox(
    "对齐方式", ["top", "center", "bottom"], index=2
)
st.title("帅帅智能AI为您服务")
c1, c2, c3 = st.columns([0.7,0.5,0.45],vertical_alignment=vertical_alignment)
with c1:
    st.image('images/lry.jpg')
    if st.button('柳如烟版', use_container_width=True):
        st.switch_page("pages/demo01.py")
with c2:
    st.image('images/zz.jpg')
    if st.button('猪猪版', use_container_width=True):
        st.switch_page("pages/demo02.py")
with c3:
    st.image('images/robot.jpg')
    if st.button('文生图', use_container_width=True):
        st.switch_page("pages/textToimage.py")


# c1, c2, c3, c4, c5, c6 = st.columns(6)
# with c1:
#     if st.button('柳如烟版'):
#         st.switch_page("pages/demo01.py")
# with c2:
#     if st.button('猪猪版'):
#         st.switch_page("pages/demo02.py")
# with c3:
#     if st.button('第三版本'):
#         st.switch_page("pages/demo03.py")
# with c4:
#     if st.button('最终版'):
#         st.switch_page("pages/demo04.py")
# with c5:
#     if st.button('文生图'):
#         st.switch_page("pages/textToimage.py")
# with c6:
#     if st.button('测试'):
#         st.switch_page("pages/demo05.py")

