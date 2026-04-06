import pandas as pd
import streamlit as st
from streamlit_folium import st_folium

st.markdown("""
    <style>
    .chat-popup {
        position: fixed;
        bottom: 20px;
        right: 20px;
        width: 320px;
        background-color: #ffffff;
        border: 2px solid #ccc;
        border-radius: 12px;
        padding: 15px;
        z-index: 1000;
        box-shadow: 0 4px 12px rgba(0,0,0,0.15);
    }
    .chat-message {
        margin: 8px 0;
        padding: 8px 12px;
        border-radius: 10px;
        max-width: 100%;
    }
    .user-msg {
        background-color: #dbeafe;
        text-align: left;
    }
    .bot-msg {
        background-color: #fef3c7;
        text-align: left;
    }
    </style>
""", unsafe_allow_html=True)

if "page_mode" not in st.session_state:
    st.session_state.page_mode = "지도"
if "selected_category" not in st.session_state:
    st.session_state.selected_category = "전체"
if "selected_restaurant" not in st.session_state:
    st.session_state.selected_restaurant = None
if "show_chat" not in st.session_state:
    st.session_state.show_chat = False
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if "add_shop" not in st.session_state:
    st.session_state.add_shop = "가게추가"


# pip install openai 
# oenai migrate
from openai import OpenAI

# -------------------------------
# 챗봇 로직
# -------------------------------
client = OpenAI(api_key="")
specific_data = pd.read_csv("ansung_restaurants_geocoded.csv")
def ai_reply(text):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": f"""
            너는 안성시의 맛집을 알려주는 인공지능 챗봇이야 {specific_data}
            """},
            {"role": "user", "content": text}
        ],
        max_tokens=200, # 데이터가 길어질 수 있는 경우 token 수 늘리기
        temperature=0.7
    )
    answer = response.choices[0].message.content.strip()
    return answer

# -------------------------------
# 챗봇 토글 버튼
# -------------------------------
if st.button("🤖 챗봇 열기/닫기"):
    st.session_state.show_chat = not st.session_state.show_chat

# -------------------------------
# 챗봇 팝업 렌더링
# -------------------------------
if st.session_state.show_chat:
    with st.container():
        st.markdown('<div class="chat-popup">', unsafe_allow_html=True)
        st.markdown("#### 🤖 기분 챗봇")
        with st.form("chat_form", clear_on_submit=True):
            msg = st.text_input("오늘 기분은?", key="chat_input_popup")
            submitted = st.form_submit_button("보내기")
            if submitted and msg:
                st.session_state.chat_history.append(("user", msg))
                ai_response = ai_reply(msg)
                st.session_state.chat_history.append(("bot", ai_response))
        for sender, text in st.session_state.chat_history[-6:]:
            role_class = "user-msg" if sender == "user" else "bot-msg"
            st.markdown(f'<div class="chat-message {role_class}">{text}</div>', unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

# -------------------------------
# UI 시작
# -------------------------------
st.title("🍱 내리 맛집 안내 시스템")
search = st.text_input("🔍 맛집 검색", placeholder="가게명을 입력하세요")

